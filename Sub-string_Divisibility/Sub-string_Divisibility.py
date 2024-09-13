import itertools

def has_sub_string_divisibility(num_str):

    primes = [2, 3, 5, 7, 11, 13, 17]

    for i in range(7):
        sub_num = int(num_str[i+1:i+4])
        if sub_num % primes[i] != 0:
            return False
    return True

def find_sum_of_pandigital_numbers():
    digits = '0123456789'
    permutations = itertools.permutations(digits)

    total_sum = 0
    for perm in permutations:
        num_str = ''.join(perm)
        if has_sub_string_divisibility(num_str):
            total_sum += int(num_str)

    return total_sum
result = find_sum_of_pandigital_numbers()
print(result)
