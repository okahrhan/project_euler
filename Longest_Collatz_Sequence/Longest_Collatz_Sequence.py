def chain():


    result = 0
    max_counter = 1
    for i in range(2,1000000):
        counter = 1
        j = i
        while True:
            if j == 1:
                break
            if j % 2 == 0:
                j = j/2
            else:
                j = 3*j + 1
            counter += 1
        if counter > max_counter:
            result = i
            max_counter = counter

    return result



def main():
    print(chain())
if __name__ == "__main__":
    main()
