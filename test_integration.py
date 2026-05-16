import pytest

from src.app import FoodBridge


@pytest.fixture
def app(tmp_path):
    db = tmp_path / "test_donations.json"
    return FoodBridge(db_path=str(db))


def test_viacep_integration_success(app):
    # Teste com um CEP real conhecido (Praça da Sé, SP)
    cep = "01001-000"
    address = app.get_address_by_cep(cep)
    assert "Praça da Sé" in address
    assert "São Paulo" in address
    assert "SP" in address


def test_viacep_integration_invalid_cep(app):
    # Teste com CEP inválido
    with pytest.raises(ValueError, match="CEP inválido"):
        app.get_address_by_cep("123")


def test_viacep_integration_not_found(app):
    # Teste com CEP que não existe
    with pytest.raises(ValueError, match="CEP não encontrado"):
        app.get_address_by_cep("99999999")


def test_add_donation_with_cep(app):
    # Teste de fluxo completo: adicionar doação com CEP
    donor = "Restaurante Teste"
    item = "Arroz"
    qty = "10kg"
    expiry = "2026-12-31"
    cep = "01001-000"

    donation = app.add_donation(donor, item, qty, expiry, cep)

    assert donation["donor"] == donor
    assert "Praça da Sé" in donation["address"]
    assert donation["status"] == "disponível"
