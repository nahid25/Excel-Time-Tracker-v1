import openpyxl
import Constant

workbook = openpyxl.load_workbook("time.xlsx")
worksheet = workbook["Sheet1"]

headline_variable = ["A", "B", "C", "D", "E", "F", "G", "H"]


def headline_cell_generator():
    number = 1
    headline_cells = []

    for variable in headline_variable:
        headline_cell = variable + str(number)
        headline_cells.append(headline_cell)

    temp_headlines = []
    temp_headlines += Constant.WORK_HEADLINES + Constant.BREAK_HEADLINES

    for (a, b) in zip(headline_cells, temp_headlines): worksheet[a].value = b
    workbook.save("time.xlsx")
