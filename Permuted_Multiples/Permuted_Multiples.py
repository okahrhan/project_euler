if __name__ == '__main__':
    number = 2
    while True:
        nbr1 = sorted(str(number))
        if nbr1 == sorted(str(2 * number)):
            if nbr1 == sorted(str(3 * number)):
                if nbr1 == sorted(str(4 * number)):
                    if nbr1 == sorted(str(5 * number)):
                        if nbr1 == sorted(str(6 * number)):
                            print(number)
                            break
        number += 1
