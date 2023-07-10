import pytest
import os

from dotenv import load_dotenv
from kata_bank_number import KataBankNumber



@pytest.fixture
def bank_numbers():
    load_dotenv()
    return KataBankNumber("data/source_data.txt", os.getenv("PATH_WRITER"))



def test_read_file(bank_numbers):
    data = bank_numbers.read_file()
    bank_numbers.validate_bank_numbers(data)

    assert isinstance(data, list)
    assert len(data) == 7
    assert len(bank_numbers.correct_numbers) == 4
    assert len(bank_numbers.ilegit_numbers) == 0
    assert len(bank_numbers.error_numbers) == 2
    assert len(bank_numbers.ambiguous_numbers) == 0

def test_format_number(bank_numbers):
    formated_line = [" _ | ||_|"," _ | ||_|"," _ | ||_|"," _ | ||_|"," _ | ||_|"," _ | ||_|"," _ | ||_|"," _ | ||_|"," _ | ||_|"]
    formated_number, is_ill = bank_numbers.format_number(formated_line)
    assert formated_number == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert not is_ill


    