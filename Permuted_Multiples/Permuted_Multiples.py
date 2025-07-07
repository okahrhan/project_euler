def main():
    find = False
    number = 2
    while not find:
        nbr1 = sorted(str(number))
        if nbr1 == sorted(str(2*number)):
            if nbr1 == sorted(str(3*number)):
                if nbr1 == sorted(str(4*number)):
                    if nbr1 == sorted(str(5*number)):
                        if nbr1 == sorted(str(6*number)):
                            return number
        number += 1
if __name__ == '__main__':
    print(main())
