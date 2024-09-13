def fibonacci():
    i = 1
    j = 1
    k = 0
    counter = 2

    while True:
        k = i + j
        i = j
        j = k
        counter += 1

        if len(str(k)) >= 1000 :
            return counter

print(fibonacci())
