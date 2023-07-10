import time
from dataclasses import dataclass
@dataclass
class HandleFile():
    input_file: str
    output_file: str

    def read_data(self)-> str:
        data = ""
        with open(self.input_file, "r") as file:
            for line in file:
                data += line 
        return data
    
    def _convert_data_str(self, result_list:list[int])-> list[str]:
        if len(result_list) == 0:
            return ["No data found"]
        return ["".join(list(map(str, element))) for element in result_list]  

    
    def _write_information(self, Tittle:str, list_data:list, file, text="") -> None:
        file.write(f"{Tittle}\n")
        for line in list_data:
            file.write(f"==> {line} {text}\n")

    def write_data(self, correct_data:list[list[int]], data_err:list[list[int]], data_ill:list[list[int,str]], amb_number: list[tuple[int, list[str]]]) -> None:
        actual_time = time.strftime('%d%m%Y%H%M%S')
        correct_data = self._convert_data_str(correct_data)
        data_err = self._convert_data_str(data_err)
        data_ill = self._convert_data_str(data_ill)

        with open(f"{self.output_file}/{actual_time}.txt", "w") as file:
            self._write_information("Correct data", correct_data, file)
            self._write_information("Err data", data_err, file, " ERR")
            self._write_information("Ilegit Number", data_ill, file, " ILL")
            file.write("Ambiguos number\n")
            for element in amb_number:
                key_num, value_num = element
                file.write(f"==> {key_num} AMB {value_num}\n")

    @staticmethod
    def format_number(numbers:int)->str: 
        return "\n".join(map(str, numbers)) 


    #TODO: Implement a better logic in the ambiguos_number
    @staticmethod
    def ambiguous_number_format(numbers:int, possible_numbers:list)->str:
        key_number = "".join(map(str, numbers)) 
        values_posible_number = ["".join(list(map(str, element))) for element in possible_numbers]
        return (key_number, values_posible_number)