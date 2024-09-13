import sys

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python script.py <sayı>")
        return

    number = int(sys.argv[1])
    largest_number = 0
    is_prime = False

    i = 2
    while i < number // 2:
        if number % i == 0:
            j = 2
            while j < i:
                if i % j == 0:
                    is_prime = False
                    break
                is_prime = True
                j += 1
            if is_prime:
                largest_number = i
        i += 1

    print(largest_number)

if __name__ == "__main__":
    main()
