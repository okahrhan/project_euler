import itertools as it
def fact():
    vals =["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    permutation = list(it.permutations(vals))

    pos = 1000000
    return permutation[pos-1]

value = fact()
result = ""
for i in value:
    result += i
print(result)
