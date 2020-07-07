import openpyxl
import work_data
import excel_headline
import style_main
import timer

workbook = openpyxl.load_workbook("time.xlsx")
worksheet = workbook["Sheet1"]

work_time = 5
break_time = 4
minute = 1

# Adding the title
excel_headline.headline_cell_generator()
# Setting the width of the cells
style_main.cell_width()

while True:
    userInput = input('\nQ to quit the program'
                      '\nPlease enter "work" or "break": ')

    """ work Det Cell Function"""
    if userInput.title() == "Work":
        work_data.work_data()

        work_message = "Date added.\n" \
                       "Time added.\n" \
                       "Work duration added.\n" \
                       "After work duration added.\n"
        print(work_message)
        user_input_timer = input("You can start the timer if you want.\n"
                                 "... To start the timer enter ('S'') or press any key: ")

        if user_input_timer.title() == "S": timer.timer("Work")

    elif userInput.title() == "Break":
        work_data.break_data()

        break_message = "Date added.\n" \
                        "Time added.\n" \
                        "Break duration added.\n" \
                        "After work duration added\n"
        print(break_message)
        user_input_timer = input("You can start the timer if you want.\n"
                                 "... To start the timer enter ('S''): ")

        if user_input_timer.title() == "S": timer.timer("Break")

    elif userInput.title() == "Q":
        print("Exiting the program")
        break
