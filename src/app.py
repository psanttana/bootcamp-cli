import json
import os
from datetime import datetime


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

    def add_donation(self, donor_name, food_item, quantity, expiry_date):
        if not donor_name or not food_item or not quantity or not expiry_date:
            raise ValueError("Todos os campos são obrigatórios.")

        try:
            datetime.strptime(expiry_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data de validade deve estar no formato AAAA-MM-DD.")

        donation = {
            "id": len(self.donations) + 1,
            "donor": donor_name,
            "item": food_item,
            "quantity": quantity,
            "expiry": expiry_date,
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
    print("4. Sair")

    while True:
        choice = input("\nEscolha uma opção: ")
        if choice == "1":
            donor = input("Nome do Doador: ")
            item = input("Item Alimentar: ")
            qty = input("Quantidade (ex: 5kg, 10 unidades): ")
            expiry = input("Data de Validade (AAAA-MM-DD): ")
            try:
                app.add_donation(donor, item, qty, expiry)
                print("✅ Doação registrada com sucesso!")
            except ValueError as e:
                print(f"❌ Erro: {e}")
        elif choice == "2":
            donations = app.list_donations()
            if not donations:
                print("Nenhuma doação disponível no momento.")
            for d in donations:
                print(
                    f"[{d['id']}] {d['item']} - {d['quantity']} "
                    f"(Validade: {d['expiry']}) | Doador: {d['donor']}"
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
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
