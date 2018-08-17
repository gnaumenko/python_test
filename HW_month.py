year = 2018
month_count = 12
first_day_of_year = 0
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    month_len[1] = 29

day_of_year = first_day_of_year

for x in range (0, month_count):
    print '-- {} --'.format(months [x])
    for date in range (1,month_len[x]+1):
        if date == 13 and day_of_year % 7 == 5:
            print ("Friday 13th")
        elif day_of_year % 7 == 0 or day_of_year % 7 == 6:
            print '{} of {}, {} weekend'.format(date, months[x], week_days[day_of_year % 7])
        else:
            print '{} of {}, {}'.format(date, months[x], week_days[day_of_year%7])
        day_of_year = day_of_year + 1


#    print("---- " + month + " ----")
#    for day in range(1,32):
#        if day != 32:
#            print (str(day) + " of " + month + "," + week_days[0])
#            for week_day in range(1,8):
#                if week_day%7 != 1:
#                    continue
#            print (str(day) + " of " + month + "," + week_days[week_day])


