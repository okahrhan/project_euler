def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_primes(value):
    total = 0
    for num in range(2, value + 1):
        if is_prime(num):
            total += num
    return total + 2


def main():
   value = int(input("value:"))
   print(sum_of_primes(value))
if __name__ == "__main__":
        main()
