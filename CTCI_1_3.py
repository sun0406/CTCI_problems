
def URLify(str1):
	new_str = ""
	for i in range(len(str1)-1):
		if str1[i] != ' ':
			 new_str += str1[i]
		else:
			if str1[i + 1] != ' ':
				new_str += "%20"
	if str1[-1] != ' ':
		new_str += str1[-1]

	return new_str



# test cases #
a = "Mr john Smith    "
b = "aaaa  bbb cccc    dd  ee"
c = "rrrrr eeeeeeee         e"
d = "rrrrr eeeeeeee         e "
e = "rrrrr eeeeeeee         e f"

print URLify(a)
print URLify(b)
print URLify(c)
print URLify(d)
print URLify(e)


'''
print "\n\n"
input = raw_input('Enter a string: ')
print URLify(input)
'''


