from ast import If
import os
import sys
from csv import reader
with open('./students.csv','r')  as file: 
  
    csv_reader=reader(file)
    for row in csv_reader:
       
         if len(row[0])==7:
            print("7")        


valid_lines = []
corrupt_lines = []



def validate_data(line):
    # TYPE YOUR SOLUTION CODE HERE
    ...




print('### VALID LINES ###')
print("\n".join(valid_lines))
print('### CORRUPT LINES ###')
print("\n".join(corrupt_lines))

