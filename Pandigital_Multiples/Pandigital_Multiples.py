def is_pandigital(num):
    num_str = str(num)
    return len(num_str) == 9 and set(num_str) == set("123456789")

def find_largest_pandigital():
    largest_pandigital = 0

    for i in range(1, 10000):
        concatenated_product = ""
        n = 1
        while len(concatenated_product) < 9:
            concatenated_product += str(i * n)
            n += 1

 def cozum_sayisini_hesapla(max_p):
     cozumler = {}  # Çevre değerine göre çözüm sayısını tutacak sözlük

     for a in range(1, max_p // 2):
         for b in range(a, max_p // 2):
             c = (a ** 2 + b ** 2) ** 0.5
             if c == int(c):  # c tam sayı mı kontrol et
                 p = a + b + int(c)
                 if p <= max_p:
                     if p not in cozumler:
                         cozumler[p] = 1
                     else:
                         cozumler[p] += 1

     en_fazla_cozum_p = max(cozumler, key=cozumler.get)
     return en_fazla_cozum_p, cozumler[en_fazla_cozum_p]

 max_p = 1000
 sonuc = cozum_sayisini_hesapla(max_p)
 print(f"Çözüm sayısının en fazla olduğu p değeri: {sonuc[0]}, Çözüm sayısı: {sonuc[1]}")
       if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
            largest_pandigital = max(largest_pandigital, int(concatenated_product))

    return largest_pandigital

def main():
    print(find_largest_pandigital())

if __name__ == "__main__":
    main()
