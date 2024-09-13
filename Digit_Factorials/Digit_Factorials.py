def is_it():
    lst = []
    for i in range(10, 50000):
        if i == sums(i):
            lst.append(i)
    return sum(lst)

def factorial(value):
    result = 1
    for i in range(2, value + 1):
        result *= i
    return result

def sums(value):
    str_value = str(value)
    result = 0
    for i in str_value:
        result += factorial(int(i))
    return result

def main():
    print(is_it())

if __name__ == "__main__":
    main()
