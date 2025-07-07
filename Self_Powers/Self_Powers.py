def self_power(number):
    return number**number



def main():
    print_value = 0
    for i in range(1,1001):
        print_value +=  self_power(i)

    str_pv = str(print_value)[-10:]
    print(str_pv)

if __name__ == '__main__':
    main()
