def fractionToDecimal(numerator, denominator):
    if numerator == 0:
        return "0"

    result = []
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")
    numerator, denominator = abs(numerator), abs(denominator)
    result.append(str(numerator // denominator))
    remainder = numerator % denominator

    if remainder == 0:
        return "".join(result)

    # Ondalık kısmı ekle
    result.append(".")
    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            result.insert(remainder_map[remainder], "(")
            result.append(")")
            break

        remainder_map[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator

    return "".join(result)


def main():
    result = 0
    return_value = 0
    a = 0
    for i in range(1,1000):
        value = fractionToDecimal(1,i)
        if "(" in value:
            result = len(value) - 4
        if result > return_value:
            return_value = result
            a = i

    print(a)
main()
