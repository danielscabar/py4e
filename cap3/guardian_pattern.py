#https://www.py4e.com/html3/03-conditional

# Short-circuiting the evaluation

x = 1
y = 0

print(x >= 2 and (x/y) > 2)

x = 6
y = 0

print(x >= 2 and (x/y) > 2)

# Guardian Pattern: Using the short_circuting concept 
# to ensure that the code will not cause a error

x = 6
y = 0

print(x >= 2 and y != 0 and(x/y) > 2)



