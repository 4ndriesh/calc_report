# -*- coding: utf-8 -*-
__author__ = 'BiziurAA'
from collect_json import Sheets
from read_data import Read_data
from write_data import Write_data

if __name__ == "__main__":
    s=Sheets()
    r=Read_data()
    w=Write_data()
    DataFrame=r.read_file_excel()
    w.DataFarme_to_Excel(DataFrame)
    # s.create_df()
    # s.write_to_excel()
    # s.read_sheet_by_excel()
    # s.DataFarme_to_Excel()
    # s.DataFarme_to_Json()
