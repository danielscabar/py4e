import re

fname = input("Enter the file name: ")
if len(fname) < 1:
  fname = 'regex_sum_42.txt'

fhandle = open(fname)

print(sum( [ int(i) for i in re.findall('[0-9]+',fhandle.read()) ] ))