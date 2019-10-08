# 12 = 1 1 0 0
# basically you check right one first, and if 'ands' with 1, you INCR num_bits
# then you 'shift' to the next
# if you look at value at each step, it's strange because after first shift you would get '6' (1 1 0)

def countBits(value):
    num_bits = 0
    while value:
        num_bits += value & 1
        value >>= 1
    return num_bits

result = countBits(12)

# standard bitwise operators work in Python as well
# & AND
# | OR
# << >> 
# ~ FLIP
# ^ XOR