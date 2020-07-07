import openpyxl
import excel_headline

workbook = openpyxl.load_workbook("time.xlsx")
worksheet = workbook["Sheet1"]


# Setting the width of the cells
def cell_width():
    for variable in excel_headline.headline_variable: worksheet.column_dimensions[variable].width = 26
    workbook.save("time.xlsx")
