from src.format_columns import FormatColums
from src.bank_validation import BankValidation

import pytest

def test_valid_number():
    assert BankValidation.checksum([0,0,0,0,0,0,0,5,1]) == True, "Should be True"

def test_not_valid_number():
    assert BankValidation.checksum([0,0,0,0,0,0,1,1,1]) == False, "Should be False"


def test_singleton_instance():
    # Verifica que se obtenga la misma instancia en cada llamada a get_instance()
    instance1 = FormatColums.get_instance()
    instance2 = FormatColums.get_instance()
    assert instance1 is instance2

def test_singleton_exception():
    # Verifica que se lance una excepción si se intenta crear una segunda instancia
    with pytest.raises(Exception, match="This class is a singleton!"):
        FormatColums()


