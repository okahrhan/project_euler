def quadratic():
    max_prime_counter = 0
    return_value = 1
    # n*n + n*a + b
    for i in range(-1000, 1000):
        for j in range(-1000, 1001):
            n = 0
            prime_counter = 0
            while True:
                fonk = n*n + n*i + j
                if is_prime(fonk):
                    n += 1
                    prime_counter += 1
                else:
                    if prime_counter > max_prime_counter:
                        max_prime_counter = prime_counter
                        return_value = i * j
                    break
    return return_value

def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def main():
    print(quadratic())

if __name__ == "__main__":
    main()
