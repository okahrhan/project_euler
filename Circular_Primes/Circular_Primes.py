def is_prime(value):
    for i in range(2 ,int(value**0.5) +1 ):
        if value % i == 0:
            return False
    return True


def circular(value):
    str_value = str(value)
    for i in range(len(str_value)):
        rotated_value = int(str_value[i:] + str_value[:i])
        if not is_prime(rotated_value):
            return False
    return True

def main():
    counter = 0
    for i in range(2,1000000):
        if is_prime(i) and circular(i):
            counter += 1
    print(counter)
if __name__ == "__main__":
    main()
