import time

def run_with_timer(func):
    start = time.time()
    result = func()
    end = time.time()
    print(f"Sonuç: {result}")
    print(f"Süre: {end - start:.6f} saniye")

def digit_power(number):
    i = 1
    result = 0
    while True:
        power = len(str(i**number))
        if power == number:
            result += 1
        elif power > number:
            return result
        i+=1

def count_powerful_digits():
    p = 1
    return_value = 0
    while True:
        n = digit_power(p)
        return_value += n
        p += 1
        if n == 0:
            return return_value
if __name__ == '__main__':
    run_with_timer(count_powerful_digits)
