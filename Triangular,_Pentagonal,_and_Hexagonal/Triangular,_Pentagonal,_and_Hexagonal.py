def Triangle(value1):
    # n(n+1)/2
    return value1 * (value1 + 1) // 2

def Pentagonal(value2):
    # n(3n-1)/2
    return value2 * (3 * value2 - 1) // 2

def Hexagonal(value3):
    # n(2n-1)
    return value3 * (2 * value3 - 1)

def is_pentagonal(n):
    return (1 + (24 * n + 1)**0.5) % 6 == 0

def is_hexagonal(n):
    return (1 + (8 * n + 1)**0.5) % 4 == 0

def main():
    value1 = 286  
    while True:
        triangle_number = Triangle(value1)
        if is_pentagonal(triangle_number) and is_hexagonal(triangle_number):
            print(triangle_number)
            break
        
        value1 += 1

if __name__ == "__main__":
    main()
