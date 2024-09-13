def is_palindromic(s):
    return s == s[::-1]

def sum_palindromes(n):
    total_sum = 0
    for i in range(1, n):
        decimal_str = str(i)
        binary_str = bin(i)[2:]
        if is_palindromic(decimal_str) and is_palindromic(binary_str):
            total_sum += i
    return total_sum

def main():
    n = 1000000
    result = sum_palindromes(n)
    print(result)
if __name__ == "__main__":
    main()
