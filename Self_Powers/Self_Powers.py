def self_power(number):
    return number**number



if __name__ == '__main__':
    print_value = 0
    for i in range(1,1001):
        print_value +=  self_power(i)

    str_pv = str(print_value)[-10:]
    print(str_pv)
