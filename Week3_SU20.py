"""
employee_name= "John Bass"
if employee_name.startswith("J"):

    print(employee_name, 'is a group B member')


str1 = input("Enter a four-digit code please: ")
if str1.endswith("67"):
    print(str1, " is a valid union code")
else:
    print(str1, " is an unknown code")


#Write a Python program to convert the distance (in feet) to inches, yards, and miles.
#Format the outputs.
d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)
"""


from datetime import datetime, timedelta, date
date_today = datetime.now()
print("Todays date", str(date_today))

# Calculating future dates for two years
future_date_after_2yrs = (date_today + timedelta(days=730)).strftime("%y-%m-%d")

# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))

#Calculate number of days before future event
future_date= date(2020, 12,2)
today_ = datetime.today().strftime("%y, %m, %d")
#today_ =date(2020,7,12)

#present = datetime.datetime.now()
future = datetime.datetime(2020, 12, 5)
difference = future - today_
print(difference)

print('There are', difference,' days before next conference:')
