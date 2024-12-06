rawinp = input("Enter a number: ")

try:
  ival = int(rawinp)
except:
   ival = ""

if type(ival) == int:
  print("Nice job!")
else:
  print("Not a number")
