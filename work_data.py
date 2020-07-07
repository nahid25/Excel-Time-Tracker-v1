import openpyxl
import Constant

workbook = openpyxl.load_workbook("time.xlsx")
worksheet = workbook["Sheet1"]

# Headline variable for the work data.
headline_variable = ["A", "B", "C", "D", "E", "F", "G", "H"]
# Break variable for the break data.
break_variable = ["E", "F", "G", "H"]


def cell_check(cell_position):
    number = 1
    work_cells = []

    while True:
        if worksheet[cell_position + str(number)].value is None:
            break
        else:
            number += 1

    if cell_position == "A":
        for (a, b) in zip(headline_variable, Constant.WORK_HEADLINES): work_cells.append(a + str(number))
    if cell_position == "E":
        for (a, b) in zip(break_variable, Constant.BREAK_HEADLINES): work_cells.append(a + str(number))

    return work_cells


# Date month year
# Time:time am or pm

def work_data():
    work_cells = cell_check("A")
    print("\nYour data is added to this location: " + str(work_cells))
    worksheet[work_cells[0]].value = Constant.TODAY.strftime("%d %b %Y")
    worksheet[work_cells[1]].value = Constant.TODAY.strftime("%I:%M %p")
    worksheet[work_cells[2]].value = (Constant.WORK_TIME.total_seconds() / 60)
    worksheet[work_cells[3]].value = Constant.ADD_WORK_TIME.strftime("%I:%M %p")

    workbook.save("time.xlsx")


def break_data():
    work_cells = cell_check("E")
    print("\nYour data is added to this location: " + str(work_cells))
    worksheet[work_cells[0]].value = Constant.TODAY.strftime("%d %b %Y")
    worksheet[work_cells[0]].number_format = 'DD MMM YYYY'

    worksheet[work_cells[1]].value = Constant.TODAY.strftime("%I:%M %p")
    worksheet[work_cells[2]].value = (Constant.BREAK_TIME.total_seconds() / 60)
    worksheet[work_cells[3]].value = Constant.ADD_BREAK_TIME.strftime("%I:%M %p")

    workbook.save("time.xlsx")
