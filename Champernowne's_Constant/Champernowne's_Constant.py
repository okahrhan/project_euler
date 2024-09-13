def find_pos():
    positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1
    string_number = ""
    i = 1

    while len(string_number) <= max(positions):
        string_number += str(i)
        i += 1

    for j in positions:
        product *= int(string_number[j - 1])

    return product

def main():
    print(find_pos())
if __name__ == "__main__":
    main()
