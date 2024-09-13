def spiral():
    return_value = 1
    for i in range(1, 501):
        an = 4*i*i + 4*i + 1
        bn = 4*i*i + 2*i + 1
        cn = 4*i*i + 1
        dn = 4*i*i - 2*i + 1
        return_value += an + bn + cn + dn
    return return_value

def main():
    print(spiral())

if __name__ == "__main__":
    main()
