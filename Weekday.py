# A program to tell the weekday of a particular date.
from calendar import weekday
from time import sleep

print("This program tells you the weekday of the inputed date...")
sleep(2)
while True:
    given_date = input("Enter the desired date you want to check in this format(dd/mm/yyyy):\n")
    try:
        day, month, year  = (given_date.split("/"))
        if int(day) > 31 or int(day) <= 0:
            raise KeyError("Invalid number of days in a month...")
        elif int(month) > 12 or int(month) <= 0:
            raise KeyError("Invalid number of months in a year...")
        elif int(year) <= 0:
            raise KeyError("Invalid value for years...")
        elif int(month) in (9, 4, 6, 11) and int(day) > 30:
            raise ArithmeticError
        elif int(month) == 2 and int(day) > 28:
            if int(year) % 4 == 0 and int(day) == 29:
                pass
            else:
                raise ArithmeticError
        sleep(0.4)
        break
    except ValueError:
        sleep(0.2)
        print("Please fill in the desired date with the day first, then the month, then the year seperated by a '/'.")
        sleep(1)
    except KeyError as Key:
        sleep(0.2)
        print(Key)
        sleep(1)
    except ArithmeticError:
        sleep(0.2)
        print("Invalid number of days in the month, please type in the correct date.")
        sleep(1)

week_day = weekday(int(year), int(month), int(day))
if week_day == 0:
    print("This date is a Monday.")
elif week_day == 1:
    print("This date is a Tuesday.")
elif week_day == 2:
    print("This date is a Wednesday.")
elif week_day == 3:
    print("This date is a Thursday.")
elif week_day == 4:
    print("This date is a Friday.")
elif week_day == 5:
    print("This date is a Saturday.")
else:
    print("This date is a Sunday.")
sleep(5)
