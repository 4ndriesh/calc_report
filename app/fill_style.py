import pandas as pd
import ast

from logging_err import Logger

class Style_pandas():
    def __init__(self):
        self.log = Logger()
        self.log.message_debug("Create class Style_pandas")


    def pars_style_from_dataframe(self,str_format):
        try:
            list_format=str_format.split(';')
            for format in list_format:
                dict_format = ast.literal_eval(format)

                if type(dict_format) == dict:
                    for key in dict_format.keys():
                        style_from_column=dict_format[key].items()
                        for col,style in style_from_column:
                            yield key,col,style
        except Exception as e:
            self.log.message_error(e)
            return 0

    def highlight_max(self, s):
        '''
        highlight the maximum in a Series yellow.
        '''
        # is_max = s == s.max()

        return 'background-color: yellow'

    def color_negative_red(self, val):
        """
        Takes a scalar and returns a string with
        the css property `'color: red'` for negative
        strings, black otherwise.
        """
        color = 'red'
        return 'merge-cells: B2:B4'

    def fill_style(self, DataFrame):
        DataFrame.style. \
                        applymap(self.color_negative_red)