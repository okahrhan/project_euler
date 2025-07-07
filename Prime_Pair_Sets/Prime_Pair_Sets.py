def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def list_of_primes():
    lst = []
    count = 0
    for i in range(2, 10**4):
        if is_prime(i):
            lst.append(i)
            count += 1 
    return lst  

def is_concat_prime(a, b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

# Verilen grup ile uyumlu asal sayıları döner
def compatible_with_all(group, candidates):
    compatible = []
    for prime in candidates:
        if all(is_concat_prime(prime, g) for g in group):
            compatible.append(prime)
    return compatible

def find_prime_sets(primes, size):
    def dfs(group, candidates):
        if len(group) == size:
            return group
        for i, prime in enumerate(candidates):
            if all(is_concat_prime(prime, g) for g in group):
                new_group = group + [prime]
                result = dfs(new_group, candidates[i+1:])
                if result:
                    return result
        return None
    
    for i, prime in enumerate(primes):
        result = dfs([prime], primes[i+1:])
        if result:
            return result
    return None

def main():
    numbers = list_of_primes()
    result = find_prime_sets(numbers, 5)
    if result:
        print("Uygun asal küme:", result)
        print("Toplam:", sum(result))
    else:
        print("Uygun küme bulunamadı.")






if __name__ == '__main__':
    main()