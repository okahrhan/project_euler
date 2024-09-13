from os import abort


def abound():
    lst = []
    lst2 = set()

    for i in range(1, 28124):
        sum = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                sum += j

        if sum > i:
            lst.append(i)

    for i in lst:
        for j in lst:
            value = i + j
            if value <= 28123:
                lst2.add(value)

    result = 0
    for i in range(1, 28124):
        if i not in lst2:
            result += i

    return result


def main():
    print(abound())

if __name__ == "__main__":
    main()
