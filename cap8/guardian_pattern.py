fhand = open('mbox-short.txt')

for line in fhand:
  line = line.rstrip()
  wds = line.split()
  #Guardian Pattern
  if len(wds) == 0 or wds[0] != 'From': 
    continue
  print(wds[2])
