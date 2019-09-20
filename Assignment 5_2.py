smallest = None
largest = None
while True :
    num = input("Enter the number:")
    if num == 'done' :
        break
    try:
        Num = float(num)
    except :
        print("Invalid number")
    else :
        if smallest is None :
            smallest = Num
            largest = Num
        if Num < smallest :
            smallest = Num
        if Num > largest :
            largest = Num
print("The smallest number is" , smallest)
print("The largest number is" , largest)
