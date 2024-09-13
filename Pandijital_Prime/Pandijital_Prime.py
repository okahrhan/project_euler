def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def permutasyon(rakamlar):
    if len(rakamlar) == 1:
        return [rakamlar]

    permutasyonlar = []
    for i in range(len(rakamlar)):
        kalan_rakamlar = rakamlar[:i] + rakamlar[i+1:]
        for p in permutasyon(kalan_rakamlar):
            permutasyonlar.append(rakamlar[i] + p)

    return permutasyonlar

def main():
    max_result = 0
    digit = "7654321"
    permutations = permutasyon(digit)

    for p in permutations:
        num = int(p)
        if is_prime(num):
            max_result = max(max_result, num)

    return max_result

print(main())
