# Import constants for numbers and word mappings
from src.constant import ABOVE_100, TENS, UNDER_20


def number_to_word(num: int) -> str:
    """
    Converts a given integer (num) into its English word representation.
    
    Args:
        num (int): The integer to convert.
        
    Returns:
        str: The English word representation of the number.
    """
    
    # Handle numbers less than 20 by directly referencing the UNDER_20 list
    if num < 20:
        return UNDER_20[num]
    
    # Handle numbers between 20 and 99
    elif num < 100:
        remainder: int = num % 10  # Get the ones digit
        if remainder == 0:  # If no remainder, return the tens word only
            return TENS[num // 10]
        # Otherwise, combine the tens and ones word
        return TENS[num // 10] + " " + UNDER_20[remainder]
    
    # Handle numbers greater than or equal to 100
    # Find the largest key in ABOVE_100 that is less than or equal to the number
    pivot: int = max([key for key in ABOVE_100 if key <= num])
    
    # Recursively call number_to_word for the quotient part (the larger number)
    p1: str = number_to_word(num // pivot)
    
    # Get the word for the current magnitude (e.g., "hundred", "thousand")
    p2: str = ABOVE_100[pivot]

    # If the number is a multiple of the current pivot (e.g., 200, 5000), return without remainder
    if num % pivot == 0:
        return f"{p1} {p2}"

    # Otherwise, recursively call number_to_word for the remainder part
    return f"{p1} {p2} {number_to_word(num % pivot)}"


if __name__ == "__main__":
    print(number_to_word(1234567890))  # Expected: "one billion two hundred thirty-four million five hundred sixty-seven thousand eight hundred ninety"
    print(number_to_word(123456789))   # Expected: "one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine"
    print(number_to_word(12345678))    # Expected: "twelve million three hundred forty-five thousand six hundred seventy-eight"
    print(number_to_word(1234567))     # Expected: "one million two hundred thirty-four thousand five hundred sixty-seven"
    print(number_to_word(123456))      # Expected: "one hundred twenty-three thousand four hundred fifty-six"
    print(number_to_word(12345))       # Expected: "twelve thousand three hundred forty-five"
    print(number_to_word(1234))        # Expected: "one thousand two hundred thirty-four"
    print(number_to_word(123))         # Expected: "one hundred twenty-three"
    print(number_to_word(12))          # Expected: "twelve"
    print(number_to_word(1))           # Expected: "one"
    print(number_to_word(0))           # Expected: "zero"
    print(number_to_word(100))         # Expected: "one hundred"
    print(number_to_word(1000))        # Expected: "one thousand"
    print(number_to_word(10000))       # Expected: "ten thousand"
    print(number_to_word(100000))      # Expected: "one hundred thousand"
    print(number_to_word(1000000))     # Expected: "one million"
    print(number_to_word(10000000))    # Expected: "ten million"
    print(number_to_word(100000000))   # Expected: "one hundred million"
    print(number_to_word(1000000000))  # Expected: "one billion"
    print(number_to_word(10000000000)) # Expected: "ten billion"
    print(number_to_word(100000000000))# Expected: "one hundred billion"
    print(number_to_word(1000000000000))# Expected: "one trillion"