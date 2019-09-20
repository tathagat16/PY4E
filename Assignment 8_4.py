file = input("Enter file name: ")
fl = open(file)
lst = list()
for lines in fl :
	lines = lines.strip()
	lines = lines.split()
	for comp in lines :
		if comp in lst :
			continue
		else :
			lst.append(comp)
lst.sort()
print(lst)
