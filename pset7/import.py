from cs50 import SQL
import csv
import sys

# check the command line validation
if len(sys.argv) != 2:
    print("error")
    exit()

# take the argument of command line the name csv file
csv_f = sys.argv[1]

f = open(csv_f)

# make a connection witg db
db = SQL("sqlite:///students.db")

# iterate in csv file row by row to insert it into db
for row in csv.DictReader(f):

    # get a list of student name
    name = row["name"].split()

    # check the form of the name to insert it into db columns (first, middle, last)
    if len(name) == 3:
        tup = ()
        tup = tup + (name[0],)
        tup = tup + (name[1],)
        tup = tup + (name[2],)
        tup = tup + (row["house"],)
        tup = tup + (int(row["birth"]),)
        db.execute("INSERT INTO students(first,middle,last,house,birth)  VALUES (%s , %s , %s , %s , %s)", tup)

    if len(name) == 2:
        tup = ()
        tup = tup + (name[0],)
        tup = tup + (None,)
        tup = tup + (name[1],)
        tup = tup + (row["house"],)
        tup = tup + (row["birth"],)
        db.execute("INSERT INTO students(first,middle,last,house,birth)  VALUES (%s , %s , %s , %s , %s)", tup)


f.close()