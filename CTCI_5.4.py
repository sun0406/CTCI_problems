
def count_ones( binary ):
    return bin(binary).count("1")

def next_number ( integer ):
    binary_num = count_ones(integer)
    smaller = integer
    bigger = integer
    while( smaller >= 0 ):
        smaller -= 1
        if count_ones(smaller) == binary_num:
            break
    while(True):
        bigger += 1
        if count_ones(bigger) == binary_num:
            break

    return smaller, bigger

print next_number(30)
