from openpyxl.styles import NamedStyle, Font, Border, Side

class Formating():
    def __init__(self):
        pass
    def template_format1(self):
        ns = NamedStyle(name='highlight1')
        ns.font = Font(name='Times New Roman',bold=True, size=10)
        border = Side(style='thin', color='000000')
        ns.border = Border(left=border, top=border, right=border, bottom=border)
        return ns


    def template_format(self):
        ns = NamedStyle(name='highlight')
        ns.font = Font(name='Times New Roman', bold=True, size=12)
        border = Side(style='thin', color='000000')
        ns.border = Border(left=border, top=border, right=border, bottom=border)
        return ns
