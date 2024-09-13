def triangle(value):
    for a in range(1, value):
        for b in range(a+1, value):
            c = value - a - b
            if a*a + b*b == c*c:
                return a*b*c
def main():
    value = int(input("value:"))
    print(triangle(value))
if __name__ == "__main__":
    main()
