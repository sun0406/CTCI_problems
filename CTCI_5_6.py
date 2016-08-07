
def int_to_binary ( int1 ):
    binary = ""
    while int1 > 0:
        if int1 % 2 == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        int1 /= 2
    return binary


def add_zeros(bit, length):
    length = length - len(bit)
    for i in range(length):
        bit = "0" + bit
    return bit

def conversion ( int1, int2 ):
    (binary1, binary2) = (int_to_binary(int1), int_to_binary(int2) )
    shorter_bit = min([binary1, binary2], key = len)
    longer_bit = max([binary1, binary2], key = len)

    if len(longer_bit) > len(shorter_bit):
        shorter_bit = add_zeros(shorter_bit, len(longer_bit))
    counter = 0
    for b1, b2 in zip(shorter_bit, longer_bit):
        if b1 != b2:
            counter += 1
    return counter

print conversion(29, 15)
