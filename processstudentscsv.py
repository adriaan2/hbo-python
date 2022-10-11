from asyncio.windows_events import NULL
import os
import sys
from webbrowser import Elinks


valid_lines =[]
corrupt_lines =[]
def validate_data(line):
    # TYPE YOUR SOLUTION CODE HERE
    #studentnumber, firstname, lastname ,birthday ,inf=map(str,line.split(','))
    studentnumber, firstname, lastname ,birthday ,inf =line.split(',')
    badlines=[]
    if len(studentnumber)==7: 
         
        if studentnumber[0]=='0':
           
            if studentnumber[1]=='9' or studentnumber =='8':
                valid_lines.append(studentnumber)
                   
    elif studentnumber==NULL:
           print("test")
    else:
     corrupt_lines.append(studentnumber)
    if firstname.isalpha()==True:
        pass
    elif firstname==NULL:
        pass
    else :
        corrupt_lines
def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())
            
    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))

if __name__ == "__main__":    
     main('students.csv')