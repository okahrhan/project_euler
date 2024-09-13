def product():
    lst = []
    for i in range(1,100):
        value = 1
        for j in range(100,10000):
            value = i * j
            if is_pandigital(i,j,value):
                lst.append(value)

    return sum(set(lst))
def is_pandigital(i, j, value):
    control = str(i) + str(j) + str(value)

    if len(control) == 9 and set(control) == set('123456789'):
        return True
    return False

def main():
    print(product())
if __name__ == "__main__":
    main()
