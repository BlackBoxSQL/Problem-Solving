def bubblesort(datalist):
	for i in range(0,len(datalist)-1):
		for j in range(0, len(datalist)-1-i):
			if datalist[j]>datalist[j+1]:
				datalist[j], datalist[j+1] = datalist[j+1], datalist[j]
	return datalist

if __name__ == '__main__':
	
	print("Choose A for insert Character Type Data B for Integer Type Data : ")
	opt = str(input())

	if opt == 'A':
		datalist = []
		print("Put 10 Strings for Ascending Sorting : ")
		for d in range(0,10):
			data = str(input(""))
			datalist.append(data)

	if opt == 'B':
		datalist = []
		print("Put 10 Numbers for Ascending Sorting : ")
		for d in range(0,10):
			data = int(input(""))
			datalist.append(data)

	print(bubblesort(datalist))