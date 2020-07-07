import time

work_time = 5
break_time = 4
minute = 1


def timer(work_title):
    if work_title == "Work":
        # 30 minute timer in second timer
        total = work_time * minute
        for i in range(1, total + 1):
            time.sleep(1)
            print("Seconds: " + str(i))

    if work_title == "Break":
        # 15 minute timer in second timer
        total = break_time * minute
        for i in range(1, total + 1):
            time.sleep(1)
            print("Seconds: " + str(i))
