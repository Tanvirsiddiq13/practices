import calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2020))
m,d,y = map(int,input().split())
days = {0:"mon",1:"tue",2:"wed",3:"thur",4:"fri",5:"sat",6:'sun'}
print(days[calendar.weekday(y,m,d)])