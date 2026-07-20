# Python Number to Words Converter

This project is a Python utility that converts integers into their English word representation. It supports a wide range of numbers from 0 to trillions and efficiently handles edge cases such as round tens, hundreds, and large numbers.

## Features

- Converts integers to their English word equivalent.
- Supports numbers from 0 to trillions.
- Handles numbers like 100, 1000, 1,000,000 with correct word formatting.
- Efficient for both small and large numbers.

## How It Works

The main function `number_to_word(num: int) -> str` recursively breaks down an integer and maps it to its English word equivalent using pre-defined lists (`UNDER_20`, `TENS`) and a dictionary (`ABOVE_100`).

#### Example:

```python
from src.number_to_word import number_to_word

print(number_to_word(123456789))   # Output: "one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine"
print(number_to_word(1001))        # Output: "one thousand one"
print(number_to_word(1000000))     # Output: "one million"
```
### Installation
To use this project in your environment:

1.	Clone the repository:
    git clone https://github.com/mahnazghssm/number_to_word.git
2.	Navigate to the project directory:
    cd number_to_word
3.	Install dependencies (if any) using:

    pip install -r requirements.txt

4.	Run the script:

    python main.py

### Project Structure
•	src/constant.py: Defines constants used for number-to-word mappings like UNDER_20, TENS, and ABOVE_100.
•	src/number_to_word.py: Contains the logic for converting numbers to words.
•	main.py: A sample script for testing the number_to_word function with different inputs.

### Usage

The project can be used for applications such as:

•	Converting financial amounts to words for reporting.
•	Generating check amounts in words.
•	Any other task requiring the conversion of numbers into human-readable text.

### Running the Examples

To run the predefined examples, simply execute:
python main.py

You’ll see output like:

one billion two hundred thirty-four million five hundred sixty-seven thousand eight hundred ninety
twelve thousand three hundred forty-five
zero
one hundred trillion

### License

This project is licensed under the MIT License. See the LICENSE file for more information.