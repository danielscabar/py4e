# Sorted by frequency

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

for v,k in sorted([(v, k) for k, v in hour_count.items()], reverse=True)[:5]:
    print("Hora:", k, "| Frequencia:",v)
