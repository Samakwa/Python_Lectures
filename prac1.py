"""
num = int(input("Enter the value of n: "))
if (num <=0 ):
    print("Enter a valid Number please")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
        print(sum)
#print ("last sum", sum)
"""
"""
while (True):
   name = input("Please enter your name: ")
   pswlist = ["fish", "lion"]
   namelist =[ "Peter", "Joe","Michael"]
   if name not in namelist:
       print ('You are not a registered user!')
       continue

   psw = input(" Hello," , name, "Enter the password: ")
   if psw in pswlist:
       break
print("Access granted")
"""
"""

names = ["michael",'Jane' ]
n =0
while n <4:
    name = input (" Please enter your name: ")
    if name not in names:
        print ("Not a registered name")
        continue
    else:
        passwordcheck()
        
        
def passwordcheck():
    i=0
    while i <= 3:
    psw = input ("Enter your password:")
        if psw == 'pass':
            print ("Access granted")
            break
        
        else:
            print("Wrong password")
            i=+ 1
            continue
            
                psw = input("Enter your password:")

    if i>3:
        #print ("You have triend more than three times")
"""

#This program loops until the set password policies are met.

#It must have 1digit, special character, lowercase, uppercase, and length of 5 - 15.

"""
import re

while True:

    pword = input("Enter user password : ")

    if ((len(pword))  < 5 or (len(pword)) > 15):

        print("Failed password length validation")

    elif not (re.search (r"\d", pword)):

        print("Failed password digit validation")

        break

    elif not (re.search(r"[A-Z]", pword)):

        print("Failed password Uppercase validation")

    elif not (re.search(r"[a-z]", pword)):

        print("Failed password Lowercase validation")

    elif not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', pword):

        print("Failed password special character")

    else:

        print("Password is valid")

        break
"""
"""
MyVar1 = "Hello"
MyVar2 = "This is Python Programming"
print("MyVar1[0]: ",  MyVar1[0])
print("MyVar2[1:6]: ",  MyVar1[1:6])

name = input( "Enter your name: ")
print("Updated:",MyVar1, str("")+ name, str("!")+ MyVar2)
"""
"""
myval = "Hello World"

print (type (myval))
print (dir(myval))
myval.e

"""
"""
myfile = open("myfile.txt", "wb")
myfile.write( "Python is a great language.\r\nYeah its great!!\r\n")
myfile.close()
"""
"""
file2 = open("text2.txt", 'r+')
str = file2.read()
print(str)

def read_n_lines(fname, n_of_lines):

    list_of_lines = []

    with open(fname, 'r') as f:
        for i in range(n_of_lines):
            list_of_lines.append(f.readline())

    return list_of_lines
"""
"""
def append_to_file(fname, string_in):

    with open(fname, 'a') as f:
        for string in string_in:
            f.write(string)

    with open(fname, 'r') as f:
        data =f.read()
        print(data)

"""
"""
age = int(input (" Please enter your age: "))
if (age < 25):
    rate = 3053.25
elif (age >= 25) and (age < 65):
    rate = 2028.40
else:
    rate = 755.30
print (" Please enter your preferred plan: ")
plan = input (" E for Economy, S for Standard or P for Premium: ")

if plan == 'E':
    final_rate = rate * 1.15
    print("Annual ECONOMY insurance price: $", final_rate)

elif plan == 'S':
    final_rate = rate * 1.7
    print("Annual STANDARD insurance price: $", final_rate)

else:
    final_rate = rate * 2.12
    print("Annual PREMIUM insurance price: $", final_rate)


from math import*
import sys
Min_bal_Chk = 250.0
Min_bal_Sav = 2000.0

Curr_bal_Chk = 0.0
Curr_bal_Sav = 0.0
allowed_bal = 0.0

while True:

    acct = input (" Please S for savings and C for Checking: ")
    transaction_type = input ("Enter W for withdrawal or D for Deposit: ")
    amount = int(input ("Please enter amount for withdrawal or deposit: "))

    if acct == 'S':
        if (transaction_type == "W" ):
            bal = allowed_bal + Curr_bal_Sav + Min_bal_Sav
            if bal < (Min_bal_Sav + abs(amount) ):
                print("Cannot withdraw. Over the limit.")

            else:
                print ("Withdrawal successfully completed")
                allowed_bal = (bal - amount ) - Min_bal_Sav
                bal = allowed_bal + Min_bal_Sav
                print ("Total Balance=$", bal)
                print("Balance  = $",allowed_bal)
        else:
            allowed_bal = Curr_bal_Sav + amount
            print( "Deposit Successfully completed")
            print("Total Savings Balance = $", allowed_bal + Min_bal_Sav)
            print (" Available for withdrawal = $", allowed_bal)

    elif acct == 'C':
        if (transaction_type == "W" ):
            bal = allowed_bal + Curr_bal_Chk + Min_bal_Chk
            if bal < (Min_bal_Chk + abs(amount) ):
                print("Cannot withdraw. Over the limit.")

            else:
                print ("Withdrawal successfully completed")
                allowed_bal = (bal - amount ) - Min_bal_Chk
                bal = allowed_bal + Min_bal_Chk
                print ("Total Balance=$", bal)
                print("Balance  = $",allowed_bal)
        else:
            allowed_bal = Curr_bal_Chk + amount
            print( "Deposit Successfully completed")
            print("Total Savings Balance = $", allowed_bal + Min_bal_Chk)
            print (" Available for withdrawal = $", allowed_bal)
    else:
        print("Wrong Account type entered.")

    resp = input("Do you want to try again? Enter Y to continue: ")
    if resp != "Y" and (resp != "y"):
        break
    else:
        continue

print ("Thanks you! See you next time")
import csv
list1 = [12, 14, 7, 0, 12, 3, 5, 2, 0, 1]
try:
    list1 = str(list1)
    with open('file1.csv', 'w', newline='') as newfile:
        for item in list1:
            newfile.write(item)
except IOError:
    print(" File cannot be opened ")

with open ("test1.txt", "a+") as a:
    str2 = " \n Another popular programming language is Java \n." \
        " Both have large areas of application \n. "\
            "While Java is Static in typing, Python is dynamic"
    contents = a.write(str2)
#print (contents)
with open("text1.txt", "r") as a:
    newfile = a.read()
print(newfile)
color = ['Blue','Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('text3.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)
content = open('text3.txt')
print(content.read())
"""
"""
DB = {'John Robson': '01/07/1757',"Peter Thompson": '03/03/70','Bill Gates': '10/28/1955', "Steve Jobs": "02/24/1955",'Ben Royce': '01/17/1706'}
DB["Peter Thompson"] = ' 03/03/70'
DB["Jane Houston"] = " 08/12/95"
print(DB)

import csv
evenlist = []
for num in range(1,100):
    if num % 2 == 0:
        evenlist.append(num)
with open ( "evenfile.csv", "w") as f:
    cw = csv.writer (f)
    cw.writerow(evenlist)

with open ( "week13.txt", "r") as f:
    newfile = f.read()
print(newfile)

color = ['Blue','Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('text3.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)
content = open('text3.txt')
print(content.read)

with open ("week13.txt", "r+") as f:
        newfile = f.read()
print(newfile)

import csv
evenlist =[]
for x in range (1, 100):
    if x %2 == 0:
        evenlist.append(x)
        with open ("evenfile.csv", "w")as outfile:
            cw =csv.writer(outfile)
            cw.writerow(evenlist)
print (evenlist)


with open ("text2.txt", "r") as myfile:
    contents = myfile.read()
print (contents)

with open ("test1.txt", "a+") as a:
    str2 = " \n Another popular programming language is Java \n." \
        " Both have large areas of application \n. "\
            "While Java is Static in typing, Python is dynamic"
    contents = a.write(str2)

import csv
def home():
    with open('Homes.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            print (row)
home()
"""
"""
import csv
def home2():
    new_homes = [76211,76301, 76401, 76501,76601]
    cost = [ 872123, 902123,  872123, 911123, 678123 ]

    for x in (new_homes, cost):
            with open("Homes.csv", 'a+', newline='\n')as outfile:
                cw = csv.writer(outfile)
                cw.writerow(x)
"""
"""
import csv
def attendees():
    list1 =[]
    with open('attendees1.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            list1.append(row)
            print (row)

    for  x in range(2):
        Firstname = input(" Enter first name: ")
        Lastname = input(" Enter Last Name: ")
        email = input(" Enter Attendees email address: ")

        with open('attendees1.csv', 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([Firstname, Lastname, email])

attendees()
"""
"""
with open ("text2.txt", "r") as myfile:
    contents = myfile.read()
#print (contents)

with open ("text2.txt", "a+") as myfile:
    newstr = "  \n Mr Bean has remained one of the most watched shows globally. \n" \
       "Other shows of similar comedic style are, however, coming up\n"
    new = myfile.write(newstr)
newcontents = open("text2.txt")
print(newcontents.read())

f = open("text2.txt","r+")
d = f.readlines()
f.seek(0)
for i in d:
    if i != "Other shows of similar comedic style are, however, coming up  Mr Bean has remained one of the most watched shows globally. ":
        f.write(i)
f.truncate()
f.close()
f = open("text2.txt")
print(f.read())
"""

"""
import requests
import csv

url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/USA.csv'
response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    ourdata = csv.reader(response.text.strip().split('\n'))
    results = []
    for record in ourdata:
        if record[0] != 'year':
            year = int(record[0])
            value = float(record[1])
            print(year, value)
import csv
with open('Expected_staff.csv')as a:
    csv_f = csv.reader(a)
    staff_emails = []

    for row in csv_f:
        staff_emails.append(row[2])


with open('attendees.csv') as b:
    csv_f = csv.reader(b)

    attendee_emails = []

    for row in csv_f:
        attendee_emails.append(row[2])

staff_emails = set(staff_emails)
attendee_emails = set(attendee_emails)

Those_attended = staff_emails.difference(attendee_emails)

print (Those_attended)

import csv
with open('Expected_staff.csv')as a:
    csv_f = csv.reader(a)
    staff_emails = []

    for row in csv_f:
        name = row[0] + " " + row[1]
        staff_emails.append(name)


with open('attendees.csv') as b:
    csv_f = csv.reader(b)

    attendee_emails = []

    for row in csv_f:
        name = row[0] + " " + row[1]
        attendee_emails.append(name)

staff_emails = set(staff_emails)
attendee_emails = set(attendee_emails)

Those_attended = staff_emails.difference(attendee_emails)

print (Those_attended)



import csv
def attendees():
    list1 =[]
    with open('attendees1.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            list1.append(row)
            print (row)

    for  x in range(2):
        Firstname = input(" Enter first name: ")
        Lastname = input(" Enter Last Name: ")
        email = input(" Enter Attendees email address: ")

        with open('attendees1.csv', 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([Firstname, Lastname, email])

attendees()

with open ("text2.txt", "r") as myfile:
    contents = myfile.read()
print (contents)

with open ("text2.txt", "a+") as myfile:
    newstr = "  \n Mr Bean has remained one of the most watched shows globally. \n" \
                "Other shows of similar comedic style are, however, coming up\n"
    new = myfile.write(newstr)

f= open("text2.txt")
print (f.read())

import csv
from datetime import date, datetime

def borrowed_books():
    author = input(" Enter author's name: ")
    title = input(" Enter title of the book: ")
    ISBN = input(" Enter ISBN of the book: ")
    ID =   input(" Enter ID of the User: ")
    borwd_date = datetime.now()
    date_borrowed = borwd_date.strftime("%d-%m-%Y")
    with open('Borrowed_books.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([author, title, ISBN, ID, borwd_date])


borrowed_books()
"""
"""

x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
a = x+y
print("Sum of x and y: ", a)
z = int(input("Please enter the third number: "))
b = z*a
print("Product of first and third number: ", b)
c = pow(b,2)
print ("Product raise to 2: ", a)
"""

#import numpy
#print (numpy.__file_)
"""
import requests
import csv

url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/USA.csv'
response = requests.get(url)
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    ourdata = csv.reader(response.text.strip().split('\n'))
    results = []
    for record in ourdata:
        if record[0] != 'year':
            year = int(record[0])
            value = round(float(record[1]), 3)
            print(year, value)

import csv
with open('Long_service.csv', "r")as a:
    csv_f = csv.reader(a)
    Longer = []

    for row in csv_f:
        name = row[0]+ " " + row[1]
        Longer.append(name)

with open('new_list.csv', "r") as b:
    csv_f = csv.reader(b)
    newstaff = []

    for row in csv_f:
        name = row[0] + " " + row[1]
        newstaff.append(name)

Longer = set(Longer)
newstaff = set(newstaff)

very_new = Longer.difference(newstaff)
for name in very_new:
    print (name)
"""
import sys
#print (sys.path)


import platform
#print(platform.architecture()[0])
#print(sys.version)
#print(os.name)
#print(platform.system())
#print(platform.release())
#import multiprocessing
#print(multiprocessing.cpu_count())

#import getpass
#print(getpass.getuser())
#import socket
#print(socket.gethostbyname(socket.gethostname()))

import os.path, time
#print("Last modified: %s" % time.ctime(os.path.getmtime("test1.txt")))
#print("Created: %s" % time.ctime(os.path.getctime("test1.txt")))
#print("Last modified: ",  time.ctime(os.path.getmtime("test1.txt")))
#print("Created: " , time.ctime(os.path.getctime("test1.txt")))


import os

#print(os.times().system)
#print (dir(os))
#path = "/var/www/html/"
#print(os.listdir(path))
#print (dir(os))
#print (help(os))
import os
#os.mkdir("prac001")
#os.getcwd
#print (os.getcwd())
#os.chdir("/Users/Sampson/Documents")
#print (os.getcwd())
#os.chdir("/Users/Sampson/Documents/Pycharm Project/prac3")
#print (os.getcwd())
#os.chdir("/Users/Sampson/Documents/Pycharm Project")
#print (os.getcwd())
#os.rename("text2.txt", "demo1.txt")
#os.rename("demo1.txt", "text2.txt")
#print(os.listdir())

"""
os.chdir("/Users/Sampson")
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
"""

#print(os.path.split("/Users/Sampson/Documents/Pycharm Project"))

#os.chdir("/home/newdir")


##os.chdir("/Users/Sampson")
#for dirpath, dirnames, filenamess in os.walk("/Users/Sampson/Documents"):
 #   print ('Current path:', dirpath)
  #  print('Directories:', dirpath)
  #  print('Files:', dirpath)
  #  print()
#print (os.getcwd())

#from datetime import datetime
#print(os.stat("text2.txt"))
#time1 = os.stat("text2.txt").st_mtime
#print(datetime.fromtimestamp(time1))

#print (dir(os.path))
#print(os.path.isfile("/Users/Sampson/Documents/Pycharm Project"))
#print("Current File Name : ",os.path.realpath(__file__))

import numpy
import sys
#print (sys.path)
import subprocess

# specify paths
binary_path = "binDirectory\Eradication.exe"
input_path = "inputDirectory\Namawala\"

# commission job
subprocess.call( [binary_path, "-C", "config.json", "--input", input_path] )