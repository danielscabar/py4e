def computepay(h, r):
    if h <= 40:
      pay_total = h * r
    else:
      pay_base = 40 * r #Payment until 40
      extra_hrs = h - 40 # Calculate extra hours
      pay_total = pay_base + extra_hrs * (r * 1.5) # Sum the extra payment to the base payment

    return pay_total
    

hrs = input("Enter Hours:")
r = input("Enter Rate:")

try:
  p = computepay(float(hrs), float(r))
  print("Pay", p)
except:
  print("The input must be a number")