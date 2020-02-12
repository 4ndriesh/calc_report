# -*- coding: utf-8 -*-
import pandas as pd
import os
from logging_err import Logger
import numpy as np
import openpyxl


class Sheets():
    def __init__(self):
        self.log = Logger()

    # зачитка листа excel
    # --------------------------------------------------------------------------------------------------------------
    def color_negative_red(self,val):
        """
        Takes a scalar and returns a string with
        the css property `'color: red'` for negative
        strings, black otherwise.
        """
        color = 'red'
        return 'merge-cells: B2:B4'

    def highlight_max(self,s):
        '''
        highlight the maximum in a Series yellow.
        '''
        # is_max = s == s.max()

        return 'background-color: yellow'

    def create_df(self):
        self.df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
       ('bird', 'Psittaciformes', 24.0),
      ('mammal', 'Carnivora', 80.2),
        ('mammal', 'Primates', np.nan),
        ('mammal', 'Carnivora', 58)],
        index = ['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                                columns = ('class', 'order', 'max_speed'))

        # np.random.seed(24)
        # self.df = pd.DataFrame({'A': np.linspace(1, 1.2, 10)})
        # self.df = pd.concat([self.df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
        #                axis=1)
        # self.df.iloc[0, 2] = np.nan
    def write_to_excel(self):
        with pd.ExcelWriter('styled.xlsx') as writer:
            # ws = writer.active

            writer.merge_cells('B2:B8')
            self.df.style. \
                applymap(self.color_negative_red). \
                to_excel(writer, sheet_name='Sheet1')



    def read_sheet_by_excel(self):
        work_path_project = "../template/ПО.xlsx"
        workSheets_TC_TU = 'ПрайсПО'
        try:
            # self.DataFrame_Sheet = pd.read_excel(work_path_project,
            #                                      sheet_name=self.workSheets_TC_TU,
            #                                      skiprows=1,
            #                                      usecols=self.work_cols)

            self.DataFrame_Sheet = pd.read_excel(work_path_project,
                                                 sheet_name=workSheets_TC_TU,
                                                 engine='openpyxl')

            print(1)
        except Exception as e:
            self.log.message_error(e)
            return 0

    def DataFarme_to_Json(self):
        self.DataFrame_Sheet.to_json('tmp.json',orient='values', date_format="iso")

    def DataFarme_to_Excel(self):
        self.DataFrame_Sheet.to_excel('tmp.xlsx', engine='openpyxl')