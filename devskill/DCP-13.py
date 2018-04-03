T = int(input())
i=1
while T-=1:
	ban1 = int(input())
	ban2 = int(input())
	pak1 = int(input())
	pak2 = int(input())

	if ban1+ban2>pak1+pak2:
		i+=1
	elif i==2:
		print("Banglawash")
	else:
		print("Miss")