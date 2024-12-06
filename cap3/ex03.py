score = input('Enter Score: ')

f_score = float(score)
allow = -1

if f_score >= 0 and f_score <= 1:
  allow = 1

if allow > 0:
  if f_score >= 0.9:
    print("A")
  elif  f_score >= 0.8:
    print("B")
  elif  f_score >= 0.7:
    print("C")
  elif  f_score >= 0.6:
    print("D")
  else:
    print("F")
else:
  print("Score out of range 0 to 1")