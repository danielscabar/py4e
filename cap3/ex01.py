hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
  f_hrs = float(hrs)
  f_rate = float(rate)

  if f_hrs <= 40:
    pay_total = f_hrs * f_rate
  else:
    pay_base = 40 * f_rate #Payment until 40
    extra_hrs = f_hrs - 40 # Calculate extra hours
    pay_total = pay_base + extra_hrs * (f_rate * 1.5) # Sum the extra payment to the base payment

  print(pay_total)

except:
  print("The input must be a number")


