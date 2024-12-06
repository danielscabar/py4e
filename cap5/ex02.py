largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        i_num = int(num)
        if (largest is None) and (smallest is None):
            largest = i_num
            smallest = i_num
        if i_num > largest:
            largest = i_num
        if i_num < smallest:
            smallest = i_num
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)