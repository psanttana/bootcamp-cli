import json
import os
from datetime import datetime
import requests


class FoodBridge:
    def __init__(self, db_path="donations.json"):
        self.db_path = db_path
        self.donations = self._load_data()

    def _load_data(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                return json.load(f)
        return []

    def _save_data(self):
        with open(self.db_path, "w") as f:
            json.dump(self.donations, f, indent=4)

    def get_address_by_cep(self, cep):
        """Busca endereço na API ViaCEP."""
        cep = cep.replace("-", "").replace(".", "").strip()
        if len(cep) != 8 or not cep.isdigit():
            raise ValueError("CEP inválido. Deve conter 8 dígitos numéricos.")

        try:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=10)
            response.raise_for_status()
            data = response.json()
            if "erro" in data:
                raise ValueError("CEP não encontrado.")
            return f"{data['logradouro']}, {data['bairro']}, {data['localidade']} - {data['uf']}"
        except requests.RequestException:
            raise ConnectionError("Erro ao conectar com a API ViaCEP.")

    def add_donation(self, donor_name, food_item, quantity, expiry_date, cep=None):
        if not donor_name or not food_item or not quantity or not expiry_date:
            raise ValueError("Todos os campos são obrigatórios.")

        try:
            datetime.strptime(expiry_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data de validade deve estar no formato AAAA-MM-DD.")

        address = "Não informado"
        if cep:
            address = self.get_address_by_cep(cep)

        donation = {
            "id": len(self.donations) + 1,
            "donor": donor_name,
            "item": food_item,
            "quantity": quantity,
            "expiry": expiry_date,
            "address": address,
            "status": "disponível",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.donations.append(donation)
        self._save_data()
        return donation

    def list_donations(self, status="disponível"):
        return [d for d in self.donations if d["status"] == status]

    def claim_donation(self, donation_id, receiver_name):
        for d in self.donations:
            if d["id"] == donation_id:
                if d["status"] == "coletado":
                    raise ValueError("Esta doação já foi coletada.")
                d["status"] = "coletado"
                d["receiver"] = receiver_name
                d["collected_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save_data()
                return d
        raise ValueError("Doação não encontrada.")


def main():
    app = FoodBridge()
    print("=== FoodBridge CLI - Gerenciador de Doações de Alimentos ===")
    print("1. Adicionar Doação")
    print("2. Listar Doações Disponíveis")
    print("3. Coletar Doação")
    print("4. Buscar Endereço por CEP")
    print("5. Sair")

    while True:
        choice = input("\nEscolha uma opção: ")
        if choice == "1":
            donor = input("Nome do Doador: ")
            item = input("Item Alimentar: ")
            qty = input("Quantidade (ex: 5kg, 10 unidades): ")
            expiry = input("Data de Validade (AAAA-MM-DD): ")
            use_cep = input("Deseja informar o CEP para o endereço? (s/n): ").lower()
            cep = None
            if use_cep == 's':
                cep = input("Digite o CEP: ")
            
            try:
                app.add_donation(donor, item, qty, expiry, cep)
                print("✅ Doação registrada com sucesso!")
            except (ValueError, ConnectionError) as e:
                print(f"❌ Erro: {e}")
        elif choice == "2":
            donations = app.list_donations()
            if not donations:
                print("Nenhuma doação disponível no momento.")
            for d in donations:
                addr = d.get('address', 'Não informado')
                print(
                    f"[{d['id']}] {d['item']} - {d['quantity']} "
                    f"(Validade: {d['expiry']}) | Doador: {d['donor']} | Endereço: {addr}"
                )
        elif choice == "3":
            try:
                d_id = int(input("ID da doação para coletar: "))
                receiver = input("Nome da Entidade Receptora: ")
                app.claim_donation(d_id, receiver)
                print("✅ Doação marcada como coletada!")
            except ValueError as e:
                print(f"❌ Erro: {e}")
        elif choice == "4":
            cep = input("Digite o CEP para buscar o endereço: ")
            try:
                address = app.get_address_by_cep(cep)
                print(f"📍 Endereço encontrado: {address}")
            except (ValueError, ConnectionError) as e:
                print(f"❌ Erro: {e}")
        elif choice == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
