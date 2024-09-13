def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def div(value):
    str_value = str(value)
    for i in range(1, len(str_value)):
        if not is_prime(int(str_value[i:])):
            return False
    for i in range(len(str_value) - 1, 0, -1):
        if not is_prime(int(str_value[:i])):
            return False
    return True

def sums_of_prime():
    counter = 0
    total_sum = 0
    n = 11  #

    while counter < 11:
        if is_prime(n) and div(n):
            counter += 1
            total_sum += n
        n += 1

    return total_sum
def main():
    print(sums_of_prime())

if __name__ == "__main__":
    main()
