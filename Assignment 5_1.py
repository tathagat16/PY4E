count = 0
tot = 0
while True :
    num = input("Enter the number:")
    if num == 'done' :
        break
    try:
        Num = float(num)
    except :
        print("Invalid number")
    tot = tot + Num
    count = count + 1
    average = tot / count
print("There are" , count ,"numbers and the average is" , average)
