from fractions import Fraction

def same_number(a, b):
    a_str = str(a)
    b_str = str(b)

    for i in a_str:
        if i in b_str and i != '0':
            return True, i

    return False, None

def fraction():
    lst = []

    for pay in range(10, 100):
        for payda in range(pay + 1, 100):
            ortak_var, ortak_rakam = same_number(pay, payda)

            if ortak_var:
                yeni_pay_str = str(pay).replace(ortak_rakam, '', 1)
                yeni_payda_str = str(payda).replace(ortak_rakam, '', 1)

                if yeni_pay_str and yeni_payda_str:  # Boş olmamalı
                    yeni_pay = int(yeni_pay_str)
                    yeni_payda = int(yeni_payda_str)

                    if yeni_payda != 0 and Fraction(pay, payda) == Fraction(yeni_pay, yeni_payda):
                        lst.append(Fraction(pay, payda))

    return lst

def main():
    fractions = fraction()
    product = 1
    for frac in fractions:
        product *= frac


    result = product.limit_denominator()
    print(result)

if __name__ == "__main__":
    main()
