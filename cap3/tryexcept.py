astr = 'Bob'

try:
  print('Hello')
  istr = int(astr)
  print('There') # Not executed if it goes into except
except:
  istr = -1

print('Done', istr)