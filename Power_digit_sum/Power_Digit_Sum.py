def digit(value):
    return 1 << value

def sum(value):
    str_value = str(value)
    result = 0
    for i in str_value:
        result += int(i)
    return result

def main():
    value = int(input("value:"))
    sum_result = digit(value)
    print(sum(sum_result))
if __name__ == "__main__":
    main()
