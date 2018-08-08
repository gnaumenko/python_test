months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#day = range(1, 31, 1)
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for month in months:
    print("---- " + month + " ----")
    for day in range(1,32):
        if day != 32:
            for week_day in range(1,8):
                if week_day%7 != 1:
                    continue
                print (str(day) + " of " + month + "," + week_days[week_day])


