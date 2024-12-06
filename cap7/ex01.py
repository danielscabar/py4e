fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File doesn't exist")
    quit()

for line in fh:
  line = line.upper().rstrip()
  print(line)