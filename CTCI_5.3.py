

# runtime complexity : O(N)

def int_to_binary ( int1 ):
    binary = ""
    while int1 > 0:
        if int1 % 2 == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        int1 /= 2
    return binary

def flip_bit ( integer ):
    binary = int_to_binary(integer)
    longest_bit = 0
    one_counter = 0
    zero_counter = 0
    holder = 0

    for bit in binary:
        if bit=="1":
            one_counter += 1
            if zero_counter > 0:
                holder += 1
        elif bit == "0":
            if zero_counter ==0:
                one_counter += 1
            else:
                if one_counter > longest_bit:
                    longest_bit = one_counter
                one_counter = holder + 1
                holder = 0
            zero_counter += 1
    print "binary value: ", binary # to make testcases' outputs look easier
    print "longest sequence of 1s: ",
    if longest_bit < one_counter:
        return str(one_counter) + "\n"
    return str(longest_bit) + "\n"

#testcases
print flip_bit(2)
print flip_bit(4)
print flip_bit(30)
print flip_bit(50)
print flip_bit(80)
print flip_bit(1775)
print flip_bit(3000)
