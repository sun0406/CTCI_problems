

def binary_toString ( real ):
    if real > 1 or real < 0:
        return "ERROR"
    else:
        counter = 0
        add_binary = "0."
        n = -1
        while(counter < 32):  # at most 32 char
            divider = 2**n
            if real == divider:
                add_binary += "1"
                break
            elif real > divider:
                add_binary += "1"
                real = real % divider
            else:
                add_binary += "0"
            n -= 1
            counter += 1
            if counter == 31:
                return "ERROR"

        return add_binary

# test cases
print binary_toString( 0.625 )
print binary_toString( 0.5 )
print binary_toString( 0.25 )
print binary_toString( 0.125 )
print binary_toString( 0.0625 )
print binary_toString( 0.75 )
print binary_toString( 0.76 )
