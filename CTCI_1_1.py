


def isUnique(str1):
	checkList = []
	for letter in str1:
		if letter in checkList:
			return False
		else:
			checkList.append(letter)
	return True

print isUnique("abcdefghijk12345[]")
print isUnique("aabcdefga")
print isUnique("mnbvcxz")
print isUnique("zmnzbvzcxz")

'''
print "\n\n"
input = raw_input('Enter a string: ')
print isUnique(input)
'''
