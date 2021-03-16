def is_year(y, m, d):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = 0
    for i in range(m-1):
        total_day += days_of_month[i]
    total_day += d
    print(total_day)


is_year(2021, 12, 31)
is_year(1999, 12, 18)
is_year(2004, 7, 5)
