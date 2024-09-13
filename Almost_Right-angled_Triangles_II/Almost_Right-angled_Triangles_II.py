import itertools
import math
def arat(value):
    #|b - c| < a < b + c
    #|a - c| < b < a + b
    #|a - b| < c < a + b
    #a <= b <= c

    counter = 0

    for a in range(1, int(value / 3)):
        for b in range(a + 1, int((value - a) / 2)):
            c2_minus_1 = a * a + b * b
            c = int(math.sqrt(c2_minus_1 + 1))
            if c * c == c2_minus_1 + 1:
                if a < b < c and a + b + c < value:
                    counter += 1

    return counter

value = 75000000
result = arat(value)
print(result)
