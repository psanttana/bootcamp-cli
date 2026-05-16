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
            url = f"https://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if "erro" in data:
                raise ValueError("CEP não encontrado.")
            address = (
                f"{data['logradouro']}, {data['bairro']}, "
                f"{data['localidade']} - {data['uf']}"
            )
            return address
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


def handle_add_donation(app):
    donor = input("Nome do Doador: ")
    item = input("Item Alimentar: ")
    qty = input("Quantidade (ex: 5kg, 10 unidades): ")
    expiry = input("Data de Validade (AAAA-MM-DD): ")
    use_cep = input("Deseja informar o CEP para o endereço? (s/n): ").lower()
    cep = None
    if use_cep == "s":
        cep = input("Digite o CEP: ")

    try:
        app.add_donation(donor, item, qty, expiry, cep)
        print("✅ Doação registrada com sucesso!")
    except (ValueError, ConnectionError) as e:
        print(f"❌ Erro: {e}")


def handle_list_donations(app):
    donations = app.list_donations()
    if not donations:
        print("Nenhuma doação disponível no momento.")
    for d in donations:
        addr = d.get("address", "Não informado")
        print(
            f"[{d['id']}] {d['item']} - {d['quantity']} "
            f"(Validade: {d['expiry']}) | Doador: {d['donor']} | "
            f"Endereço: {addr}"
        )


def handle_claim_donation(app):
    try:
        d_id = int(input("ID da doação para coletar: "))
        receiver = input("Nome da Entidade Receptora: ")
        app.claim_donation(d_id, receiver)
        print("✅ Doação marcada como coletada!")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def handle_search_address(app):
    cep = input("Digite o CEP para buscar o endereço: ")
    try:
        address = app.get_address_by_cep(cep)
        print(f"📍 Endereço encontrado: {address}")
    except (ValueError, ConnectionError) as e:
        print(f"❌ Erro: {e}")


def main():
    app = FoodBridge()
    print("=== FoodBridge CLI - Gerenciador de Doações de Alimentos ===")

    menu = {
        "1": ("Adicionar Doação", handle_add_donation),
        "2": ("Listar Doações Disponíveis", handle_list_donations),
        "3": ("Coletar Doação", handle_claim_donation),
        "4": ("Buscar Endereço por CEP", handle_search_address),
        "5": ("Sair", None),
    }

    while True:
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")

        choice = input("\nEscolha uma opção: ")

        if choice == "5":
            print("Saindo... Até logo!")
            break

        if choice in menu:
            _, func = menu[choice]
            func(app)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
