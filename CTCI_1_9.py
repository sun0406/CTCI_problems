


def stringRotation( s1, s2 ):
	if len(s1) == len(s2):
		return s2 in (s1+s1)
	return False

print stringRotation ( "waterbottle", "erbottlewat" )
print stringRotation ( "wwatrbottle", "erbotlewwat" )


'''
print "\n\n"
input1 = raw_input('Enter the first string: ')
input2 = raw_input('Enter the second string: ')
print stringRotation(input1, input2)
'''
