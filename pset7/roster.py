from cs50 import SQL
import csv
import sys

# check the command line validation
if len(sys.argv) != 2:
    print("error")
    exit()

# the forms of outputs
form1 = "{0} {1}, born {2}"

form2 = "{0} {1} {2}, born {3}"

# take the argument of command line the name of house
house = sys.argv[1]

# make a connection witg db
db = SQL("sqlite:///students.db")

# excute a query that access the info of students in the house
lis = db.execute("SELECT first, middle, last, birth FROM students WHERE students.house = %s", house)

# sort a list of dictionary based on last name and first name
lis = sorted(lis, key=lambda i: (i['last'], i['first']))

# iterate in the list to print our info
for dic in lis:
    
# ckeck the middle name to avoid printing None in the output
    if dic["middle"] == None:

        print(form1.format(dic["first"], dic["last"], dic["birth"]))

    else:

        print(form2.format(dic["first"], dic["middle"], dic["last"], dic["birth"]))

