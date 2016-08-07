
def insertion (N, M, i, j):
	M_len = len(str(M))

	if j - M_len +1 >= i:
		str_N, str_M = str(N), str(M)
		new_str = str_N[:-j-1] + str_M + str_N[-i:]
		return int(new_str)

	else:
		return False



print insertion(10000000000, 10011, 2, 6)
