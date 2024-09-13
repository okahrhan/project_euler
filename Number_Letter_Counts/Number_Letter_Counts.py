def number_to_words(n):
    num_words_1_to_19 = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    num_words_tens = [
        'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]

    if n == 1000:
        return "onethousand"
    elif n >= 100:
        if n % 100 == 0:
            return num_words_1_to_19[n // 100 - 1] + "hundred"
        else:
            return num_words_1_to_19[n // 100 - 1] + "hundredand" + number_to_words(n % 100)
    elif n >= 20:
        if n % 10 == 0:
            return num_words_tens[n // 10 - 2]
        else:
            return num_words_tens[n // 10 - 2] + num_words_1_to_19[n % 10 - 1]
    else:
        return num_words_1_to_19[n - 1]

def total_letter_count(limit):
    total = 0
    for i in range(1, limit + 1):
        total += len(number_to_words(i))
    return total

limit = 1000
print(total_letter_count(limit))
