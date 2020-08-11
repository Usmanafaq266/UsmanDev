import datetime  # this library is used for using date and time manipulations e.g creating a data of certain time zone
import pytz  # this library is use for global ti

''' Y = year, M = month, D = date, h = hour, m = minute, s = seconds ; these terms are used in comments for understanding syntax'''

nowday = datetime.date.today()  # today() func. used for printing todays date and by using .date with it gives
print(nowday)

my_birthday = datetime.date(2000, 1, 19)  #for printing the date given to it syntax: date(Y, M, D)
print(my_birthday)

days_since_born = nowday - my_birthday
print(days_since_born)

days_since_born = (nowday - my_birthday).days  #by using .days it will print only the date and not timeline
print(days_since_born)

time_delta = datetime.timedelta(days=5)  # timedelta() func. is used for manipulating time difference
print(nowday - time_delta)

print(nowday.day)  # this will print the present day date suppose today is 13th and so it will print 13

print(nowday.weekday())  # this will print the day of the week that is present day like mon = 0, tues = 1, wed =2....

print(datetime.time(7 , 8, 6))  # this will print the hour minute and second syntax: time(h, m, s, ms)

hour_differ = datetime.timedelta(hours=6)
print(datetime.datetime.now())  # this will show date and time that is right now

hour_differ = datetime.timedelta(hours=12) # now this will differ your present date and time by 12hours
print(datetime.datetime.now() + hour_differ)

print(datetime.datetime.now(tz=pytz.UTC))  #this will print present date time and time zone but we don't konw time zone so it will bw 00:00

# so if we don't know the current location time zone we can serach for that using for loop
'''for tz in pytz.all_timezones:
    print(tz)'''                 #this will print the global timezone names

present_datetime = datetime.datetime.now(tz=pytz.UTC)
karachi_datetime = present_datetime.astimezone(pytz.timezone("Asia/Karachi")) #this will print the current date and time of the timezone user wants to
print(karachi_datetime)

# BY using above functions we will now do 'STRING FORMATTING' means changing 2020-13-03 to March 13, 2020
print(karachi_datetime.strftime('%B %d, %Y'))  #yeah it will convert 2020-03-13 into March 13,2020 where %B is month %d is date and %Y is year

# Now we reverse above march 13, 2020 to 2020-03-13
reverse = datetime.datetime.strptime('March 13, 2020', '%B %d, %Y')
print(reverse)
#in strftime() f is formatting and in strptime() p is parsing

