import datetime
from datetime import date
import csv
import sys
import os


users = [["John Robson","1423"],["Michael Peters","2222"],["Jane Truism","8635"]]

All_books = []

def enter_book():
    add= int(input ('How many books: '))
    for i in range(add):
        author = input(" Enter author's name: ")
        title = input(" Enter title of the book: ")
        ISBN = input(" Enter ISBN of the book: ")
        ID = input(" Enter ID of the User: ")
        rec_date = datetime.datetime.now()
        date_returned = rec_date.strftime("%d-%m-%Y")
        #All_books.update[author] =(title,ISBN,ID,date_returned)

        with open ('books.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([author,title,ISBN, ID, date_returned])




#enter_book()


def check_out():
    found = False
    books_borrowed = 0
    ID = input("Enter users ID:")
    with open('users.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            if ID in row[0]:
                print("User ID found")
                found = True
                row[1] = int(row[1])
                if  (row[1] < 5):
                    enter_book()
                    row[1] = books_borrowed
                    books_borrowed += 1
                    with open('users.csv', 'a', newline='') as rd:
                        writer = csv.writer(rd)
                        writer.writerow([ID, books_borrowed])
                else:
                    print("This user has borrowed up to 5 books")

        else:
            print("Do you want register user?")
            resp = input("Enter Y or N: ")
            if resp == "Y":
                add_users()
            else:
                sys.exit

def add_users():
    missing =[]
    ID = input("Enter users ID:")
    with open('users.csv', 'r+', newline='') as rd:
        reader = csv.reader(rd)
        for row in reader:
            if ID in row:
                print("User already available")
                break
            if ID not in row:
                books_borrowed = 0
                with open('users.csv', 'a+', newline='') as rd2:
                    writer = csv.writer(rd2)
                    writer.writerow([ID, books_borrowed])
                    print("Successfully Added with ID", ID)
                    break



def borrowed_books():
    author = input(" Enter author's name: ")
    title = input(" Enter title of the book: ")
    ISBN = input(" Enter ISBN of the book: ")
    ID =   input(" Enter ID of the User: ")
    borwd_date = datetime.datetime.now()
    date_borrowed = borwd_date.strftime("%d-%m-%Y")
    with open('Borrowed_books.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([author, title, ISBN, ID, borwd_date])


def return_book():
    ISBN = input("Enter ISBN of the book:")
    with open('Borrowed_books.csv', 'r+', newline='') as rd, open ('books.csv', 'a', newline='') as inf:
        reader = csv.reader(rd, delimiter='\t')
        writer = csv.writer(inf)
        for row in reader:
            brd = list(reader)
            bwt = list(writer)
            if 'ISBN' in row[2]:
                print('Book details Found: {}'.format(row))
                writer.writerow([row])
                brd.remove(row)
                bwt.append(row)
                print('Thank you')
                del reader.reader[row]
            else:
                print("Book not found!")
                print("Do you want to register it?")
                resp = input("Enter Y or N: ")
                if resp == "Y":
                    add_users()
                else:
                    sys.exit

""""
print("Welcome to our Document Management System")
while(True):
    print('''Select your Option
                 
            1:Add Books/Content
            2:Check out
            3:Return book
            4:Add User
            5:Update Books Database
            6:Exit or Back''')
    opt=int(input("Please Enter your option:"))
    if opt==1:
        enter_book()
                   
    elif opt==2:
        check_out()
                  
    elif opt==3:
        return_book()
                    
    elif opt==4:
        add_users()
                    
    elif opt==5:
                    name=input("Please Enter Student Name:")
                    pin=input("Please Enter Student R.No:")
                    lib.Delete_Students(name.capitalize(),pin)
                elif opt2==5:
                    lib.Details_Students()
                elif opt2==6:
                    print("Back to Menu")
                    break
                else:
                    print("Wrong input")
                    continue


while your_guess != numb and your_guess != 'quit':
    your_guess = int(input("Enter your guess: "))

    if your_guess.lower() == 'quit':
        break
    your_guess = int(your_guess)
    count += 1

"""


#check_out()
#add_users()
#return_book()
#borrowed_books()
#add_users()