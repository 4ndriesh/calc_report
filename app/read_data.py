import pandas as pd

from logging_err import Logger
from openpyxl import load_workbook, Workbook
class Read_data():
    def __init__(self):
        self.log=Logger()
        self.log.message_debug("Create class Read_data")


    def read_file_excel(self,path= "../template/ПО V2.xlsx",sheet= 'ПрайсПО'):
        try:
            # self.DataFrame_Sheet = pd.read_excel(work_path_project,
            #                                      sheet_name=self.workSheets_TC_TU,
            #                                      skiprows=1,
            #                                      usecols=self.work_cols)

            DataFrame = pd.read_excel(path,
                                                 sheet_name=sheet,
                                                 engine='openpyxl'
                                      )

            self.log.message_debug("Read file path: {}".format(path))
            return DataFrame
        except Exception as e:
            self.log.message_error(e)
            return 0