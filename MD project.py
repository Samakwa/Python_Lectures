import datetime

users = [["John Robson","1423"],["Michael Peters","2222"],["Jane Truism","8635"]]
with open ('books.txt', 'a') as f:
    enter = f.write()
    f.write("\n")


def enter_book():
    author = input(" Enter author's name: ")
    title = input(" Enter title of the book: ")
    ISBN = input(" Enter ISBN of the book: ")
    ID = input(" Enter ID of the User: ")
    date_returned = datetime.datetime.now()

enter_book()