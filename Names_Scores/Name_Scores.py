def counter(name: str, idx: int) -> int:
    dic = {chr(i + 64): i for i in range(1, 27)}
    return_value = sum(dic[ch] for ch in name) * (idx + 1)
    return return_value


def names_score():
    with open("sorted_names.txt", "r") as file:
        names = file.read().replace('"', "").split(",")

    result_value = 0

    for i in range(len(names)):
        result_value += counter(names[i], i)

    return result_value


print(names_score())
