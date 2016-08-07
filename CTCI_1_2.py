

def isPermutate(str1, str2):

	if sorted(list(str1)) == sorted(list(str2)):
		return True
	else: return False


print isPermutate("aabbc", "bbaac")
print isPermutate("abcde", "fedcba")
print isPermutate("aaabbb", "ababab")
print isPermutate("aabbcee", "bbaeeac")
print isPermutate("aabbceef", "bbaeeac")

'''
print "\n\n"
input1 = raw_input('Enter the first string: ')
input2 = raw_input('Enter the second string: ')
print isPermutate(input1, input2)
'''
