def triangle_number():
    sums = 0
    i = 1

    while True:
        sums += i
        if derive(sums) >= 11:
            return sums
        i += 1

def derive(number):
    counter = 0
    sqrt_n = int(number**0.5)
    for i in range(1, sqrt_n + 1):
        if number % i == 0:
            counter += 2
    if sqrt_n * sqrt_n == number:
        counter -= 1
    return counter

def main():
    print(triangle_number())

if __name__ == "__main__":
    main()
