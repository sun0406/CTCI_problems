
def compress(str1):
	counter = 1
	new_str = ""
	for i in range(len(str1)-1):
		if str1[i] == str1[i+1]:
			counter += 1
		else:
			new_str += str1[i] + str(counter)
			counter = 1
			
	return new_str + str1[-1] + str(counter)

print "\n\n" + compress("aaabbbccccc")
print compress("xxxxzzzzeeqqqhhhq")
print compress("lmnop")		
print compress("ttteeeeqqqqqddddd")
print compress("llllllddddddwwwwwww") + "\n\n"

'''
print "\n\n"
input = raw_input('Enter a string: ')
print compress(input)
'''

