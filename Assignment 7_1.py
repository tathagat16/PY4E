hey = input("Enter the file name")
try:
    hi = open(hey)
except:
    print("File cannot be opened:" , hey )
    exit()
for lines in hi :
    lines = lines.strip()
    oye = lines.upper()
    print(oye)
