def fight():
    #
    lst = []
    i = 2
    while True:
        if i == is_it(i):
            lst.append(i)
        i += 1
        if i >= 999999:
            return sum(lst)
    return sum(lst)
def is_it(value):
    str_value = str(value)
    result = 0
    for i in str_value:
        result += int(i)**5
    return result

def main():
    print(fight())
if __name__ == "__main__":
    main()
