import pandas as pd

from logging_err import Logger

class Style_pandas():
    def __init__(self):
        self.log = Logger.inst()
        self.log.message_debug("Create class Style_pandas")

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