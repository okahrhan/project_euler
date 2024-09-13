def main():
    bellow = int(input(""))
    sum = 0

    for i in range(bellow):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print(sum)

if __name__ == "__main__":
    main()
