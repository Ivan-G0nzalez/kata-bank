class FormatColums:
    __instance = None

    @staticmethod
    def get_instance():
        if FormatColums.__instance == None:
            FormatColums()
        return FormatColums.__instance

    def __new__(cls):
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
                return cls.__instance
            else:
                raise Exception("This class is a singleton!")

    def create_columns(self, lines_without_format:str)-> list[str]:
        lines = lines_without_format.split("\n")
        columns = []
        for i in range(0,len(lines[0]), 3):
            column = ''.join(line[i:i+3] for line in lines)
            columns.append(column)
        return columns           


def test_format_columns():
    format_colum = FormatColums()
    
    