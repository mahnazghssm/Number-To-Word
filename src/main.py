from src.constant import ABOVE_100, TENS, UNDER_20


def number_to_word(num: int) -> str:
    if num < 20:
        return UNDER_20[num]

    elif num < 100:
        remainder: int = num % 10

        if remainder == 0:
            return TENS[num // 10]

        return f"{TENS[num // 10]}-{UNDER_20[remainder]}"

    pivot: int = max([key for key in ABOVE_100 if key <= num])

    p1: str = number_to_word(num // pivot)
    p2: str = ABOVE_100[pivot]

    if num % pivot == 0:
        return f"{p1} {p2}"

    return f"{p1} {p2} {number_to_word(num % pivot)}"


if __name__ == "__main__":
    print(number_to_word(1234567890))
    print(number_to_word(123456789))
    print(number_to_word(12345678))
    print(number_to_word(1234567))
    print(number_to_word(123456))
    print(number_to_word(12345))
    print(number_to_word(1234))
    print(number_to_word(123))
    print(number_to_word(12))
    print(number_to_word(1))
    print(number_to_word(0))
    print(number_to_word(100))
    print(number_to_word(1000))
    print(number_to_word(10000))
    print(number_to_word(100000))
    print(number_to_word(1000000))
    print(number_to_word(10000000))
    print(number_to_word(100000000))
    print(number_to_word(1000000000))
    print(number_to_word(10000000000))
    print(number_to_word(100000000000))
    print(number_to_word(1000000000000))