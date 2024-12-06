name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# Counting the frequency of each e-mail
hist = {}

for line in handle:
  words = line.split()
  if len(words) == 0 or not words[0] == 'From':
     continue
  hist[words[1]] = hist.get(words[1], 0) + 1

# Getting the most frequent e-mail
bigcount = None
bigword = None

for word, count in hist.items():
   if bigcount is None or count > bigcount:
      bigcount = count
      bigword = word

print(bigword,bigcount)