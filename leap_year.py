def is_year_leap(leap):
    if leap % 4 == 0 and leap % 100 != 0 or leap % 400 == 0:
        leap = True
    else:
        leap = False

print(is_year_leap(int(input)))