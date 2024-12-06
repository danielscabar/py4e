import re

fname = input("Enter the file name: ")
if len(fname) < 1:
  fname = 'regex_sum_42.txt'

fhandle = open(fname)

num_list = list()

for line in fhandle:
  line = line.rstrip()
  numbers = re.findall('[0-9]+', line)
  if len(numbers) < 1: continue
  for num in numbers:
    num_list.append(int(num))

print(sum(num_list))