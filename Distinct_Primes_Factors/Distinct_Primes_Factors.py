def Find_primes(number):
    i = 2
    lst = []
    n = number
    while i * i <= n:
        if n % i == 0:
            lst.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        lst.append(n)
    return lst


if __name__ == '__main__':

    order = 0
    i = 2
    while True:
        if len(Find_primes(i)) == 4:
            order += 1
            if order == 4:
                print(i - 4 + 1)
                break
        else:
            order = 0
        i += 1
