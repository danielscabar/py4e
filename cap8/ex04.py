fname = input("Enter file name: ")
fhand = open(fname)

lst = list()

for line in fhand:
  line = line.rstrip()
  wds = line.split()
  for wd in wds:
    if wd not in lst:
      lst.append(wd)

lst.sort()
print(lst)
