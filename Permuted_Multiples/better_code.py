def check_multiple(number):
    str_number = sorted(str(number))

    for i in range(2,7):
        m_number = number*i
        if str_number != sorted(str(m_number)):
            return False
    return True

if __name__ == '__main__':
    number = 1
    while True:
        if check_multiple(number):
            print(number)
            break
        number += 1
