datalist = [10,21,35,14,45,6,47,8]
def bubblesort(datalist):
	for i in range(0,len(datalist)-1):
		for j in range(0, len(datalist)-1-i):
			if datalist[j]>datalist[j+1]:
				datalist[j], datalist[j+1] = datalist[j+1], datalist[j]
	return datalist

print(bubblesort(datalist))