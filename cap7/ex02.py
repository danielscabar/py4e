# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print("File doesn't exist")
    quit()

count = 0
acc_value = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    value = float(line[line.find(":")+1:])
    count = count + 1
    acc_value = acc_value + value
print("Average spam confidence:", acc_value/count)
