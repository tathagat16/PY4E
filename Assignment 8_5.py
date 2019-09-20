mbox = input("Enter the file name:")
lt = list()
count = 0
try :
    hi = open(mbox)
except :
    print("File doesn't exists!")
    exit()
for lines in hi :
    lines.rstrip()
    if lines.startswith("From "):
        words = lines.split()
        print (words[1])
        count = count + 1
print ("There were", count, "lines in the file with From as the first word")
