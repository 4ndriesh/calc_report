
from logging_err import Logger

class Write_data():
    def __init__(self):
        self.log = Logger.inst()
        self.log.message_debug("Create class Write_data")

    def DataFarme_to_Excel(self,DataFrame,path='tmp.xlsx'):
        DataFrame.to_excel(path, engine='openpyxl')
        self.log.message_debug("Write file: {}".format(path))

    def write_to_excel(self):
        with pd.ExcelWriter('styled.xlsx') as writer:
            # ws = writer.active

            writer.merge_cells('B2:B8')
