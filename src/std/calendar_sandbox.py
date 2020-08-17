import calendar

c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2020, 1, 0, 0)
print(st)

hc = calendar.HTMLCalendar(calendar.MONDAY)
st = hc.formatmonth(2020, 1)
print(st)

for i in c.itermonthdays(2020, 8):
    print(i)