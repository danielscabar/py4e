name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_count = dict()

for line in handle:
    wds = line.split()
    if len(wds) == 0 or wds[0] != 'From': continue
    hour = wds[5].split(':')[0]
    hour_count[hour] = hour_count.get(hour, 0) + 1

for k,v in sorted(hour_count.items()):
    print(k, v)
