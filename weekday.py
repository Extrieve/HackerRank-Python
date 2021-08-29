from datetime import date
import datetime
week = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
everyOther = week[::2]
day = str(date.today()).split('-')
day = [int(x) for x in day]
week_num = datetime.date(day[0], day[1], day[2]).weekday()
today = week[week_num]

print(everyOther)
