import sys
import csv
import statistics

# detect function is to open the CSV file and read its contents into memory 
# and return the name of DNA's owner if exist 


def detect(csv_file, lis):
    # open the database file
    f = open(csv_file)
    # create a dectionary which it's key is name of person
    # & value is a list of STR counts
    dic = {}
    # reading each row of database file
    for row in csv.reader(f):
        dic[row[0]] = row[1:]
        
    f.close()
    # check if the list of STR exist in data base    
    for key in dic:
        if lis == dic[key]:
            return key
    return "No match"
   
# STR_cal to calculate the longest consecutive sequence of repeated STR


def STR_cal(file1):
    # open text file (a sequence of STR)
    file = open(file1)
    # put a text file in a string tline
    tline = ""
    for line in file:
        tline = tline + line
        
    cnt = 0
    # 1st loop to find a SRT seq. with 4 char in text file 
    for i in range(0, len(tline)):
        string0 = tline[i: i + 4]
        # check if each 4 char(string) in dic_STR keys
        if string0 in dic_STR:
            temp = i
            while tline[temp: temp + 4] == string0:
                cnt = cnt + 1
                temp = temp + 4
            # append a consecutive sequence of repeated 
            dic_STR[string0].append(cnt)
            cnt = 0
    # 2nd loop to find a SRT seq. with 5 char in text file         
    for i in range(0, len(tline)):    
        string1 = tline[i: i + 5]
        # check if each 4 char(string) in dic_STR keys
        if string1 in dic_STR:
            temp = i
            while tline[temp: temp+5] == string1:
                cnt = cnt + 1
                temp = temp + 5
            # append a consecutive sequence of repeated 
            dic_STR[string1].append(cnt)
            cnt = 0
    # 3rd loop to find a SRT seq. with 8 char in text file     
    for i in range(0, len(tline)): 
        string2 = tline[i: i+8]
        # 1st loop to find a SRT seq. with 8 char in text file 
        if string2 in dic_STR:
            temp = i
            while tline[temp: temp+8] == string2:
                cnt = cnt + 1
                temp = temp + 8
            # append a consecutive sequence of repeated STR    
            dic_STR[string2].append(cnt)
            cnt = 0        
    lis2 = []
    # iterate on dic_STR values(list)
    for k in dic_STR.values():
        # we get longest consecutive sequence of repeated 
        # str() to compare with sting in database
        lis2.append(str(max(k)))   
    file.close()
    return lis2 


dic_STR = {}
# check the command line parameters
if len(sys.argv) == 3:
    CSV_F = sys.argv[1]
    TXT_F = sys.argv[2]
    # we have two different CSV files with different STR standerd
    if CSV_F == "databases/large.csv":
        dic_STR = {"AGATC": [0], "TTTTTTCT": [0], "AATG": [0], "TCTAG": [0], "GATA": [0], "TATC": [0], "GAAA": [0], "TCTG": [0]}
    elif CSV_F == "databases/small.csv":
        dic_STR = {"AGATC": [0], "AATG": [0], "TATC": [0]}
    print(detect(CSV_F, STR_cal(TXT_F)))
else:
    print("Usage: python dna.py data.csv sequence.txt")
