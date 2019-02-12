num = input("Put the number to check if it is panindrome or not :")

rev = num[::-1]

if rev == num:
	print("Palindrome !")
else:
	print("Not palindrome")