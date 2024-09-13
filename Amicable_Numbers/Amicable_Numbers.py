def amicable(value):
    lst = []
    amicable_lst = []
    for i in range(1, value):
        sums1 = 0
        sums2 = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                sums1 += j
                if j != 1 and j != i // j:
                    sums1 += i // j
        if sums1 > i and sums1 < value:
            for k in range(1, int(sums1 ** 0.5) + 1):
                if sums1 % k == 0:
                    sums2 += k
                    if k != 1 and k != sums1 // k:
                        sums2 += sums1 // k
            if sums2 == i:
                amicable_lst.append(i)
                amicable_lst.append(sums1)
    return amicable_lst

def amicable_sums(value_lst):
    result = 0
    for i in value_lst:
        result += i
    return result

def main():
    value = int(input("value = "))
    a = amicable(value)
    b = amicable_sums(a)
    print(b)

if __name__ == "__main__":
    main()
