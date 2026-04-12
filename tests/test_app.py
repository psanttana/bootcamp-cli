import os
import unittest

from src.app import FoodBridge


class TestFoodBridge(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_donations.json"
        self.app = FoodBridge(db_path=self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_donation_success(self):
        donation = self.app.add_donation("Restaurante A", "Arroz", "5kg", "2024-12-31")
        self.assertEqual(donation["donor"], "Restaurante A")
        self.assertEqual(donation["item"], "Arroz")
        self.assertEqual(donation["status"], "disponível")

    def test_add_donation_invalid_date(self):
        with self.assertRaises(ValueError):
            self.app.add_donation("Restaurante A", "Arroz", "5kg", "31-12-2024")

    def test_add_donation_missing_fields(self):
        with self.assertRaises(ValueError):
            self.app.add_donation("", "Arroz", "5kg", "2024-12-31")

    def test_list_donations(self):
        self.app.add_donation("Restaurante A", "Arroz", "5kg", "2024-12-31")
        donations = self.app.list_donations()
        self.assertEqual(len(donations), 1)

    def test_claim_donation_success(self):
        d = self.app.add_donation("Restaurante A", "Arroz", "5kg", "2024-12-31")
        claimed = self.app.claim_donation(d["id"], "ONG Esperança")
        self.assertEqual(claimed["status"], "coletado")
        self.assertEqual(claimed["receiver"], "ONG Esperança")

    def test_claim_already_collected(self):
        d = self.app.add_donation("Restaurante A", "Arroz", "5kg", "2024-12-31")
        self.app.claim_donation(d["id"], "ONG Esperança")
        with self.assertRaises(ValueError):
            self.app.claim_donation(d["id"], "Outra ONG")

    def test_claim_non_existent(self):
        with self.assertRaises(ValueError):
            self.app.claim_donation(999, "ONG Esperança")


if __name__ == "__main__":
    unittest.main()
