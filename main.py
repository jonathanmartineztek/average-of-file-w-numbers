"""
File Name: main.py
Developer: Jonathan Martinez
Date last modified: December 12, 2017
Description: This program reads all of numbers and calculates the
              average of all the numbers stored in the file numbers.txt
email address: jonathanmartineztek@gmail.com
"""
import sys
import os

path = os.path.join(sys.path[0],'numbers.txt')

sum = 0
count = 0

if os.path.exists(path):
  
  print('Reading in file...\n')
  with open('numbers.txt', 'r') as file:
    contents = file.readlines()
    print('Calculating average...')
    for num in contents:
      sum += int(num)
      count += 1
      
else:
  
  print('NOT FOUND! \n\'numbers.txt\' does not exist \nor not in current directory.')
  sys.exit(1)
  
print('Avgerage value:', sum / count)
