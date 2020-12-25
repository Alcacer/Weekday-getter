# A program to tell the weekday of a particular date.
from calendar import weekday
from time import sleep


while True:
    given_date = input("Please input your date of birth in this format(dd/mm/yyyy):\n")
    try:
        day, month, year  = (given_date.split("/"))
        if int(day) > 31:
            raise KeyError("You exceeded the number of days in the month...")
        elif int(month) > 12:
            raise KeyError("You exceeded the number of months in a year...")
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
        print("Please fill in your date of birth with the day first, then the month, then the year seperated by a '/'.")
        sleep(1)
    except KeyError as Key:
        sleep(0.2)
        print(Key)
        sleep(1)
    except ArithmeticError:
        sleep(0.2)
        print("You exceeded the number of days in the month, please type in the correct date.")
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
