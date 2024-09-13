def count_sundays_on_first_of_month():

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    day_of_week = 2

    sunday_counter = 0

    for i in range(1901, 2001):
        for month in range(12):
            if day_of_week == 0:
                sunday_counter += 1

            days = months[month]

            if month == 1:
                if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                    days += 1

            day_of_week = (day_of_week + days) % 7

    return sunday_counter

print(count_sundays_on_first_of_month())
