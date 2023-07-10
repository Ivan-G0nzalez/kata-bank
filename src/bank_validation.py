from src.constanst import possible_results

class BankValidation:
    
    @staticmethod
    def checksum(list_number: list) -> 0 :
        multiply_list_number = [key * value for key,value in enumerate(list_number[::-1], start=1)]
        return sum(multiply_list_number) % 11 == 0

    @staticmethod         
    def amb_validation(list_err_numbes):
        revalidate_numbers = []
        possible_valid_nums = possible_results
        counter_question_mark = list_err_numbes.count("?")
        if counter_question_mark == 1: 
            for index, num in enumerate(list_err_numbes):
                if num == "?":
                        tem_list = list(list_err_numbes)
                        for possible in [0,1,2,3,4,5,6,7,8,9]:
                            tem_list[index] = possible
                            if BankValidation.checksum(tem_list):
                                revalidate_numbers.append(tem_list)
        elif not counter_question_mark:                    
            for index, num in enumerate(list_err_numbes):
                possible_digits = possible_valid_nums.get(num,(0,1,2,3,4,5,6,7,8,9))
                for pos_num in possible_digits:
                    tem_list = list(list_err_numbes)
                    tem_list[index] = pos_num
                    if BankValidation.checksum(tem_list):
                        revalidate_numbers.append(tem_list)   
        return revalidate_numbers

