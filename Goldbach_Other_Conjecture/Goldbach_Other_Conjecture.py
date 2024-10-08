import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_written(n):
    for p in range(2, n):
        if is_prime(p):
            kalan = n - p
            if kalan % 2 == 0:
                k = kalan // 2
                root = int(math.sqrt(k))
                if root * root == k:
                    return True
    return False

def main():
    n = 9  
    while True:
        if not is_prime(n) and not is_written(n):
            return n
        n += 2  

if __name__ == "__main__":
    print(main())