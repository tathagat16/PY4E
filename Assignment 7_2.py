hey = input("Enter the file name")
count = 0
add = 0
try:
    hi = open(hey)
except :
    print("No such file exists!")
    exit()
for lines in hi :
    lines = lines.rstrip()
    if not lines.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    mn = lines.find(" ")
    num = float(lines[mn:])
    add = add + num
desired = add/count
print("Average spam confidence:", desired)
