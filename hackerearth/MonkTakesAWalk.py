def isVowel(ch):
    # check the conditions for vowels
    if(ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e'
       or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o'
       or ch == 'U' or ch == 'u'):
        return True
    else:
        return False


def countVowel(s):
    count = 0
    for i in mylist:
        if(isVowel(i) == True):
            count += 1
    return count


test = int(input())
for j in range(test):
    mylist = str(input())
    print(countVowel(mylist))

# First checked the vowel
# count the vowel
# from the given input and return count
