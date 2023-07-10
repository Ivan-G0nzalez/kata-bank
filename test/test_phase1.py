from assertpy import assert_that

from src.format_columns import FormatColums
from src.constanst import number_table

columns_formate = FormatColums()

class TestColumn:
    def test_format_column(self):
        """
        This test validate is the function format_column
        has the correct fortmat or it is organized before 
        it can be interated to get the numbers in integers.
        """
        format_col = columns_formate.create_columns('    _  _     _  _  _  _  _ \n  | _| _||_||_ |_   ||_||_|\n  ||_  _|  | _||_|  ||_| _|')
        expected = ['     |  |', ' _  _||_ ', ' _  _| _|', '   |_|  |', ' _ |_  _|', ' _ |_ |_|', ' _   |  |', ' _ |_||_|', ' _ |_| _|']

        assert format_col == expected, "format is not correct"
        

    def test_format_columns_expected_numbers(self):
        """
        This test validate that once number are formatted correctly
        the number correspond to the expected result
        in order to validate that the information is correct.
        """

        format_col = columns_formate.create_columns('    _  _     _  _  _  _  _ \n  | _| _||_||_ |_   ||_||_|\n  ||_  _|  | _||_|  ||_| _|')

        numbers = []
        for key_number in format_col:
            numbers.append(number_table[key_number])

        expected = [1,2,3,4,5,6,7,8,9]
        assert_that(numbers).is_equal_to(expected), "Incorrect number"
