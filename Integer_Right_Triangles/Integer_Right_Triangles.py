def count_p(max_p):
    dic = {}
    for i in range(1, max_p // 2):
        for j in range(1 , max_p // 2):
            c = (i ** 2 + j ** 2) ** 0.5
            if c == int(c):
                p = i + j + int(c)
                if p <= max_p:
                    if p not in dic:
                        dic[p] = 1
                    else:
                        dic[p] += 1
    max_p = max(dic, key=dic.get)
    return max_p, dic[max_p]

def main():
    print(count_p(1000))
    #cozum sayisinin en fazla oldugu p degeri: argv [0], cozum sayisi: argv [1]}
if __name__ == "__main__":
    main()
