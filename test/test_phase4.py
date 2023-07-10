from src.bank_validation import BankValidation

class TestAmbValidatation:
    
    def test_ambs_validation(self):
        expected = [[8, 8, 8, 8, 8, 6, 8, 8, 8], [8, 8, 8, 8, 8, 8, 9, 8, 8], [8, 8, 8, 8, 8, 8, 8, 8, 0]]
        actual = BankValidation.amb_validation([8,8,8,8,8,8,8,8,8])
        
        assert expected == actual

    def test_amb_validation(self):
        expected = [[5, 5, 9, 5, 5, 5, 5, 5, 5], [5, 5, 5, 6, 5, 5, 5, 5, 5]]    
        actual1 = BankValidation.amb_validation([5,5,5,5,5,5,5,5,5])

        assert expected == actual1

    def test_amb_validation(self):
        expected = []    
        actual1 = BankValidation.amb_validation([1,2,3,4,"?",6,7,8,"?"])

        assert expected == actual1     

    