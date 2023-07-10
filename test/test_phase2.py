import pytest

from src.bank_validation import BankValidation

class TestBankValidation:

    def test_checksum(self):
        """This test validate the checksum of a 
        list of nine numbers if the result is different than
        0 the it throws an exception"""
        account_number = [3,4,5,8,8,2,8,6,5]
        check_sum = BankValidation.checksum(account_number)
        assert check_sum == True, "No checksum available"

    def test_no_checksum(self):
        """This test validate the checksum of a 
        list of nine numbers if the result is different than
        0 the it throws an exception"""
        account_number = [0,0,0,0,0,0,1,1,1]
        check_sum = BankValidation.checksum(account_number)
        assert check_sum != True, "Checksum available"

    def test_invalid_account_number(self):
        """
        This test validate that in case of the list
        have a character different than a number a
        number should fail
        """

        account_number = ["?",0,0,0,0,0,1,1,1]
        with pytest.raises(TypeError):
           BankValidation.checksum(account_number)
