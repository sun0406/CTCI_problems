
def compare(str1, str2):
	shorter_str = min([str1,str2], key = len)
	longer_str = max([str1,str2], key = len)
	
	for i in range(len(shorter_str)):
		if str1[i] != str2[i]:
			if len(str1)==len(str2):
				return str1[i+1:], str2[i+1:]
			else:
				return longer_str[i+1:], shorter_str[i:]

	return shorter_str, longer_str[:-1]
			
def OneAway(str1, str2):
	if abs(len(str1) - len(str2)) > 1:
		return False
	elif str1 == str2:
		return True
	else:
		new_str1, new_str2 = compare(str1,str2)
		return new_str1 == new_str2

#test cases
print(OneAway("plfea", "ple"))
print(OneAway("pale", "ple"))
print(OneAway("ple", "pale"))
print(OneAway("pales", "pale"))
print(OneAway("pale", "bale"))
print(OneAway("pale", "bake"))

'''
print "\n\n"
input1 = raw_input('Enter the first string: ')
input2 = raw_input('Enter the second string: ')
print OneAway(input1, input2)
'''


