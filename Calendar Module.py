# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date=input().split()
day=calendar.weekday(int(date[2]),int(date[0]),int(date[1]))
print(calendar.day_name[day].upper())