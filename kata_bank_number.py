import os
from dotenv import load_dotenv

from src.handle_file import HandleFile
from src.constanst import number_table
from src.format_columns import FormatColums
from src.bank_validation import BankValidation

class KataBankNumber:
    def __init__(self, path_reader, path_writer):
        self.path_reader = path_reader
        self.path_writer = path_writer
        self.correct_numbers = []
        self.ilegit_numbers = []
        self.error_numbers = []
        self.ambiguous_numbers = []
        self.handle_file = HandleFile(self.path_reader, self.path_writer)


    def read_file(self):
        data = self.handle_file.read_data().split('\n\n')
        return data


    def format_number(self, formated_line):
        is_ill = False
        formated_number = []

        for key_number in formated_line:
                digit = number_table.get(key_number, "?")
                if digit == "?":
                     is_ill = True
                formated_number.append(digit)

        return formated_number, is_ill        
    

    def _validate_err_and_ilegit_number(self, list_number)->None:
        for number in list_number:
            possible_numbers = BankValidation.amb_validation(number)
            if len(possible_numbers) == 1:
                self.correct_numbers.extend(possible_numbers)
                list_number.remove(number)
            elif len(possible_numbers) > 1:
                amb_number = self.handle_file.ambiguous_number_format(number, possible_numbers)
                self.ambiguous_numbers.append(amb_number)
                list_number.remove(number)       

    def validate_bank_numbers(self, data):
        format_column = FormatColums()
        
        for line in data:
            formated_line = format_column.create_columns(line)
            formated_number, is_ill = self.format_number(formated_line)
            
            if is_ill:
                self.ilegit_numbers.append(formated_number)

            elif formated_number:
                if BankValidation.checksum(formated_number):
                    self.correct_numbers.append(formated_number)    
                else:
                    if formated_number not in self.error_numbers:
                        self.error_numbers.append(formated_number)
        
        self._validate_err_and_ilegit_number(self.ilegit_numbers)
        self._validate_err_and_ilegit_number(self.error_numbers)


    def write_data(self)-> None:
        self.handle_file.write_data(self.correct_numbers, self.error_numbers, self.ilegit_numbers, self.ambiguous_numbers) 


def run()-> None:
    load_dotenv()

    PATH_READER = os.environ.get('PATH_READER')
    PATH_WRITER = os.environ.get('PATH_WRITER')


    handle_bank_number = KataBankNumber(PATH_READER, PATH_WRITER)

    data = handle_bank_number.read_file()
    handle_bank_number.validate_bank_numbers(data)
    handle_bank_number.write_data()

if __name__=="__main__":
    run()