standofdna = open('rosalind_revc.txt', 'r')
myfile = standofdna.readline()
standofdna.close()

revmyfile = myfile[::-1]
for i in revmyfile:
	if(i == "A"):print("T")
	elif(i == "T"):print("A")
	elif(i == "C"):print("G")
	elif(i == "G"):print("C")