def factoriel(value):
    result = 1
    for i in range(1,value):
        result *= i
    return result
def sum(value):
    str_value = str(value)
    result = 0
    for i in str_value:
        result += int(i)
    return result

if __name__ =="__main__":
    value = int(input("value ="))
    a = factoriel(value)
    b = sum(a)
    print(b)
