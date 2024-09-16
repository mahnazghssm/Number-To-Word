# List of words for numbers 0 through 19
UNDER_20: list[str] = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", 
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
    "sixteen", "seventeen", "eighteen", "nineteen"
]

# List of words for tens multiples (20, 30, 40, ... 90)
TENS: list[str] = [
    "", "", "twenty", "thirty", "forty", "fifty", 
    "sixty", "seventy", "eighty", "ninety"
]

# Dictionary to map powers of 10 and above (e.g., 100, 1000) to their word equivalents
ABOVE_100: dict[int, str] = {
    100: "hundred", 
    1000: "thousand", 
    1000000: "million", 
    1000000000: "billion", 
    1000000000000: "trillion"
}