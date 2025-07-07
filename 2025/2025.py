def is_it(number):
    str_number = str(number)
    for i in range(1, len(str_number)):
        s1 = str_number[:i]
        s2 = str_number[i:]
        if (s1.startswith('0') and s1 != '0') or (s2.startswith('0') and s2 != '0'):
            continue
        try:
            n1 = int(s1)
            n2 = int(s2)
            if n2 > 0 and (n1 + n2) ** 2 == number:
                return True
        except ValueError:
            continue
    return False

def main():
    lst = []
    i = 1
    while True:
        square = i * i
        if square >= 10**16:
            break
        if is_it(square):
            lst.append(square)
        i += 1
    return sum(lst)

if __name__ == '__main__':
    print(main())
#20 dk da bitti
