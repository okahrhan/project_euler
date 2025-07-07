def is_prime(number):
    for i in range(3,int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def main():
    primes = []
    for i in range(1000, 10000):
        if is_prime(i):
            primes.append(i)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            a = primes[i]
            b = primes[j]
            c = 2 * b - a
            if c > 9999:
                continue
            if is_prime(c):
                if sorted(str(a)) == sorted(str(b)) == sorted(str(c)):
                    triplet = (a, b, c)
                    if triplet != (1487, 4817, 8147):
                        return f"{a}{b}{c}"


if __name__ == '__main__':
    print(main())
