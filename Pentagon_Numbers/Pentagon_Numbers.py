def Pentagonal(value):
    return (value * (value * 3 - 1)) // 2

def is_pentagonal(n):
    if (1 + (24 * n + 1)**0.5) % 6 == 0:
        return True
    return False

def main():
    flag = True
    i = 1
    while flag:
        for j in range(1, i):
            a = i * (3 * i - 1) // 2
            b = j * (3 * j - 1) // 2
            if is_pentagonal(a + b) and is_pentagonal(a - b):
                print(a - b)
                flag = False
                break
        i += 1  

if __name__ == "__main__":
    main()
