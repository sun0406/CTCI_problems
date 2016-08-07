
def odd_counter(map1):
	counter = 0
	for value in map1.values():
		if value%2 != 0:
			counter += 1
		if counter > 1:
			return False
	return True

def map_store(str1):
	map1 = {}
	for letter in str1:
		if letter != ' ':
			if letter not in map1.keys():
				map1[letter] = 1
			else:
				map1[letter] += 1
	return map1

def palindrome_permutation(str1):
	str1 = str1.lower()
	new_map = map_store(str1)

	if odd_counter(new_map) == True:
		return True
	else:
		return False


a = "aabbfcc"
b = "racecar"
print palindrome_permutation(a)
print palindrome_permutation(b)

'''
print "\n\n"
input = raw_input('Enter a string: ')
print palindrome_permutation(input)
'''

