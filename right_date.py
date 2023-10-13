users_day = int(input('Введите день :'))
users_month = int(input('Введите месяц :'))
users_year = int(input('Введите год :'))
user_date = {users_day: users_month}



def date(day, month, year):

    month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                 11: 30, 12: 31
                 }
    real_year = (range(2020))

    if year % 4 == 0:
        month_day = 29
    if year % 4 == 0 and year % 100 == 0:
        month_day = 28
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        month_day = 29
    if user_date in month_day:
        print("Верная дата")
    else:print("не верная дата")

print(date(users_day, users_month, users_year))