import random
import math
"""
x = int (input ("enter the first number: "))
y = int (input ("Enter the second number: "))
a =x+y
print (" Sum of First and Second Number:", a)
z= int (input ("enter the third number: "))
"""

#name = input (" Please enter your name: ")
#loc = int(input (" Please enter your location: "))
#dest = 125 - loc
#print ("Hello", name, ', You have ', dest, "miles until your destination")

#pi = 3.142
"""
r = int(input("Please enter the radius of the cylinder: "))
h = int(input("Please nter the height of the cylinder: - "))
b_area = 2* math.pi *r **2
s_area = h * 2* math.pi* r
Surface_area = b_area + s_area
print ("Base Area:", b_area)
print("Side Area:", s_area)
print("Surface Area:", Surface_area)
print ("Surface Area:", round(Surface_area,2))


x= True
y= False

print ("X and Y:", x and y)
print ('X or Y:', x or y)
print ("not of x:", not x)


x =5
print (x is 5)



ourrand = random.randint(0, 99)
count =0
while (True):
    your_num = int(input("Enter your favorite number :"))
    count += 1
    if your_num < ourrand:
        print("You number",your_num, "is lower than our system's number")
    elif your_num > ourrand:
        print("You number", your_num, "is greater than our system's number")
    else:
        print(" Hurray!!, You got it in", count, "trials")
        break


import random
d = random.randrange(2,43,3)
ch = random.choice("Every_Step")
print (str(d) + ch)


import datetime
print ("Current date and time: " , datetime.datetime.now() )
print ("Current date and time: " , datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))


pi = 3.142
r = int(input("Please enter the radius of the cylinder: "))
h = int(input("Please enter the height of the cylinder: - "))
b_area = 2* pi *r **2
s_area = h * 2* pi* r

Surface_area = b_area + s_area
print ("Base Area:", b_area)
print("Side Area:", s_area)
print ("Total Surface Area:", Surface_area)

a = [1,3,4,6,7,8]
print(4 in a)
print (4 not in a)

import datetime as dt
from datetime import date, timedelta

curr_time = dt.datetime.now().time().strftime('%H:%M:%S')
#curr_time = dt.datetime.now()

close ="23:00:00"
curr_dt2 = dt.datetime.strptime(curr_time, '%H:%M:%S')
end_dt = dt.datetime.strptime(close, '%H:%M:%S')
diff = (end_dt - curr_dt2)
#diff.seconds/60
print (diff)

import datetime as dt
from datetime import date, timedelta
Now = dt.datetime.now()
print("Welcome to 9-Solutions Shopping Center")
print("Current time: ")
print(Now.strftime("%H:%M"))
print("Closing time for today is 11:00pm")
close = (timedelta(hours=23) - (Now- Now.replace(hour=0, minute=0)))
print("You have", close, "hours for your shopping today")
n
import random
a = random.randint(1,10)
d = random.randrange(2,43,3)
ch = random.choice("Python is an interesting Language".split())
print ("random integer pick 1 to 10:", a)
print ("random pick from 2 to 43 range :", d)
print ("random choice:", ch)

var1 = 'Hello World'
for item in dir(var1):
    print (item)


speed = "500 m/s"
x = speed[:5]
print(x)
fruit = "banana"
print ("n" in fruit)


import datetime as dt
from datetime import date, timedelta

today = dt.datetime.today().strftime('%Y:%m:%d')
print ("Today's date is: ", today)
curr_time = dt.datetime.now().strftime('%H:%M:%S')
print ("Current time: ", curr_time)
remaining = 145-27
print (" You have ", remaining, ("miles remaining on this road"))
#close ="23:00:00"
#curr_dt2 = dt.datetime.strptime(curr_time, '%H:%M:%S')
#end_dt = dt.datetime.strptime(close, '%H:%M:%S')


first = "maryland"
a =first[3:]
b = first[:3]

second = "England"
c = second[:3]
d = second[3:]
str1 = (b + d)
str2 = (c+ a)
print ("After swapping, we have ", str1, ",",str2)

wrd = input ("Please enter a word: ")
rvs= wrd[::-1]
if wrd == rvs:
    print( "Your word ",wrd, " is a palindrome")
else:
    print("Your word ", wrd, " is not a palindrome")


str1 ="Please do not throw sausage pizza way"
str2 = "the quick brown fox jumps over the lazy "
str1= str1.split()
str2= str2.split()
counts = dict()

for word in str1: #str2:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print (counts)

Mystr = "Python is awesome....yeah!!!"
print("Padded string : ",Mystr.zfill(40))
print ("Padded String : ",Mystr.zfill(50))


x = input("Enter a number: ")
if x.isdigit():
    print("Inputs are numbers...")
else:
    print("Wrong input")


import string

print ("Special Chracters:", string.punctuation)

psw = input('Enter a password to validate: ')
spec_chars = list()
upper = list()

for letter in psw:
    if letter.isupper():
        upper.append(letter)
    if letter in string.punctuation:
        spec_chars.append(letter)

if (len(psw) >= 6) and (len(psw) <= 8) and\
    (len(spec_chars) >= 1) and (len(upper) >= 1) :
    print('Valid Password!')
else:
    print('Invalid Password')

def fib_gen():
    num = int(input("The number of items in the sequence:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib


print(fib_gen())
input()


fund = 100000.0

level = input (" Please S for Senior, or J for Junior, SH for Sophomore or F for Freshmen: ")
CGPA = float(input("Enter your grade: "))

if level == 'S':
    if CGPA >= 3.5:
        pay = (0.37 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.24 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.26 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'J':
    if CGPA >= 3.5:
        pay = (0.33 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.37 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.37 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'SH':
    if CGPA >= 3.5:
        pay = (0.37 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.37 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.37 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
elif level == 'F':
    if CGPA >= 3.5:
        pay = (0.37 * fund)* 0.15 *  CGPA
        print ( "Your scholarship amount is ", pay)
    elif CGPA > 2.4 and CGPA < 3.5:
        pay = (0.37 * fund) * 0.10 * CGPA
        print("Your scholarship amount is ", pay)
    else:
        pay = (0.37 * fund) * 0.05 * CGPA
        print("Your scholarship amount is ", pay)
else:
    print ("Wrong input")

#print ('string to list', list ('tin'))
#print ('list string', ''.join(['g', 'o','l','d']))

element = 'helium'
print (element[-1])
print ('list string', ''.join(['g', 'o','l','d']))
a = range (1,20)
our_list =[]

for num in a:
    sqd_items = num **2
    our_list.append(sqd_items)

print (our_list)


a = range (1,50)
list1 =[]

for num in a:
    if num %2 != 0:
        list1.append(num)

print (list1)

str1 = "9-Solutions"
cnt=0
list1=[]
for i in str1[0:]:
    if (cnt%2)!=0:
        cnt=cnt+1
    else:
        list1.append(i)
        cnt=cnt+1
print(list1)
print ("".join(list1))

lst = [1, 9, 21, 10, 16]

print (9 in lst)

names = ['Adam', 'Carol', 'Henry', 'Maggy', 'Phil']
names.insert(2, "kate")
print(names)


x = 1.16
y = 2.05
High_performers =[]
Good_performers =[]
Average_performers =[]

while (True):
    name = input( "Enter the Staff name please: ")
    a = int(input("Enter the number of previous promotions: "))
    b = int(input("How many endorsement have you received? : "))
    c = int(input("Enter number of years : "))


    rating = (a * x **3 ) + (b * y*2) + c
    if rating > 19:
        print (" Congratulations!", name, "You belong to first class performers")
        High_performers.append(name)
    elif rating >= 11:
        print(" Congratulations!", name, "You will be promoted, as a middle-class performer")
        Good_performers.append(name)
    else:
        print(" Please work harder next time!")
        Average_performers.append(name)

    resp = input("More staff? Enter 0 to quit:")
    if resp == "0" :
        break
    else:
        continue

print( "High Performers:", High_performers)
print( "Good Performers:", Good_performers)
print( "Average Performers:", Average_performers)



num = [10,20,30,(10,20),40]
for i in num:
    if type(i)==tuple:
        print("tuple found at ", num.index(i))

str = "The rain in Spain falls mainly in the plane"
tokens = string.split(str)
print (tokens)


event_a  = [ "Peters", "Mary", 'John', "Jerry", "Greg"]
event_b  = [ "Jill",  "Jane", "Mary", "Gab", "Jerry", "Greg"]
a = set(event_a)
b = set(event_b)

not_attend = a.difference(b)

print (not_attend)


dict1 = {'a':2, 3:['x', 'y'], 'joe':"smith"}
for key in dict1:
    print (key)
for k,v in dict1.items():
    print([k,v])
counts = {}
print ("Enter a line of text:")
line = input('')
words = line.split()

print("Counting...")

for word in words:
    counts[word] = counts.get(word,0) + 1
print (counts)


Empl = {"John Robson": 7,"Bill Gates": 10, "Steve Jobs": 20,"Ben Royce": 16, "Mike Thompson": 3,
         "peter Hen": 	9, "Sam Peterson" : 21, "Bet Johnson":21, "Michael Clairs": 4, "Gem Becks":18}

print ("Total service year by all employees: ", sum(Empl.values()))
print ("Employee with highest number of years: ", max (Empl.items(), key= lambda  k: k[1]))
print ("Employee with least number of years: ", min (Empl.items(), key= lambda  k: k[1]))
print ("Average number of years: ",(sum(Empl.values())/len(Empl) ))

def ExponFunc ():
    list1 = range (1,30)
    list2= []
    for item in list1:
        item= item**3
        list2.append(item)
    print (list2)
    return

ExponFunc ()


def InsuranceFunc():

    age = int(input (" Please enter your age: "))
    if (age < 25):
        rate = 3053.25
    elif (age >= 25) and (age < 65):
        rate = 2028.40
    else:
        rate = 755.30
    while (True):
        print (" Please enter your preferred plan: ")
        plan = input (" E for Economy, S for Standard or P for Premium: ")

        if plan == 'E':
            final_rate = rate * 1.15
            print("Annual ECONOMY insurance price: $", final_rate)

        elif plan == 'S':
            final_rate = rate * 1.7
            print("Annual STANDARD insurance price: $", final_rate)

        elif plan == "P":
            final_rate = rate * 2.12
            print("Annual PREMIUM insurance price: $", final_rate)
        else:
            if (plan == "E") or (plan == "S") or (plan == "P"):
                print ("Thank you")
                break
            else:
                continue

InsuranceFunc()

"""

import  OS
#print (help(OS))
os.chdir("newdir")

