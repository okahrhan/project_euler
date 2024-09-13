def power_number():
    # 1 < a < 101 1 < b < 101
    lst = []
    for i in range(2,101):
        value = i
        for j in range(2,101):
            value *= i
            if value not in lst:
                lst.append(value)

    return len(lst)
def main():
    print(power_number())
if __name__ == "__main__":
    main()
