
def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_list_and_prefix():
    lst = []
    prefix_lst = []
    total = 0
    for i in range(2, 1000000):
        if is_prime(i):
            lst.append(i)
            total += i
            prefix_lst.append(total)
    return lst, prefix_lst

def C_Prime_Sum():
    primes, prefix_sums = prime_list_and_prefix()

    max_length = 0
    result = 0
    n = len(primes)


    for i in range(n):
            for j in range(i + max_length, n):
                total = prefix_sums[j] if i == 0 else prefix_sums[j] - prefix_sums[i - 1]
                if total >= 1000000:
                    break
                if is_prime(total):
                    length = j - i + 1
                    if length > max_length:
                        max_length = length
                        result = total

    return result, max_length

if __name__ == '__main__':
    print(C_Prime_Sum())
