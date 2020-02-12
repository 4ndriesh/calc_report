ef create_marks(self, write_to_report, list_mark):
        tmp = write_to_report.sheets.get('ПрайсПО')
        import itertools
        # row = list(map(lambda row: row, tmp.iter_rows()))
        for row in tmp.iter_rows():
            # for mark in list_mark:
                # cel = list(filter(lambda x: x.value == mark, list(itertools.chain(*row))))
            for cell in row:
                if cell.value in list_mark:
                    # for cell in cel:
                    mark_in_excel = {'startcol': cell.column, 'startrow': cell.row}
                    # mark_in_excel=list(map(lambda args: {args[0]: {'startcol':args[1].column,'startrow':args[1].row}},
                    #                 enumerate(cel)))
                    yield cell.value, mark_in_excel.values()


def write_to_excel(self, DataFrame, path='', file_name='', list_columns=None):
    mv = load_workbook(os.path.join(path, file_name))
    mv.template = False
    file_name = 'document.xlsx'
    mv.save(file_name)
    with pd.ExcelWriter(os.path.join(path, file_name), engine='openpyxl', keep_date_col=True) as write_to_report:
        write_to_report.book = mv
        write_to_report.sheets = dict(map(lambda ws: (ws.title, ws), mv.worksheets))
        # mv.close()
        self.template_format(write_to_report.book)
        for sheet in write_to_report.sheets:
            get_descript_sheet = write_to_report.sheets.get(sheet)
            tmp_startrow = 0
            for columns in list_columns:
                for mark, (startcol, startrow) in self.create_marks(get_descript_sheet, columns):
                    self.log.message_debug("Finde mark: {}".format(mark))

                    if startrow != tmp_startrow:
                        tmp_startrow = startrow
                        self.format_excel(write_to_report, startrow + 1, sheet, len(DataFrame))

                    # DataFrame.loc[:, [mark]].to_excel(write_to_report, engine='openpyxl',
                    #                                   sheet_name=sheet,
                    #                                   startrow=startrow-1,
                    #                                   startcol=startcol - 1,
                    #                                   header=False,
                    #                                   index=False)

                    sh = mv[sheet]
                    # DT = DataFrame(index=False, header=False)
                    for index, row in DataFrame.loc[:, [mark]].iterrows():
                        sh.cell(row=startrow + index, column=startcol, value=row[mark])

                    write_to_report.book[sheet].cell(startrow, startcol).style = 'highlight'
        write_to_report.save()
        self.log.message_debug("Write file: {}".format(path))

def pars_style_from_dataframe(self, dict_format):
    print(type(dict_format))
    if type(dict_format) == dict:
        # n = json.dumps(dict_format)
        # o = json.loads(n)
        for key in dict_format.keys():
            style_from_column = dict_format[key].items()
            # style_from_column = o['merge_cell'].items()
            for col, style in style_from_column:
                yield key, col, style
    return 0, ''
