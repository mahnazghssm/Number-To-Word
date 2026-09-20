# Python Number to Words Converter

A simple Python project that converts non-negative integers into their English word representation.

## Features

- Converts numbers from 0 up to 999 trillion
- Handles units, tens, hundreds, thousands, millions, billions, and trillions
- Uses recursion to convert larger numbers
- Includes basic tests with pytest

## How It Works

The `number_to_word()` function converts a number into words by breaking it down into smaller parts.

It uses three lookup tables from `constant.py`:

- `UNDER_20`: words for numbers from 0 to 19
- `TENS`: words for the tens from 20 to 90
- `ABOVE_100`: words for hundred, thousand, million, billion, and trillion

For numbers from 20 to 99, the function combines a tens word with a units word. For numbers 100 or greater, it finds the largest matching unit, converts the part before it, and then converts the remainder recursively.

## Example

```python
print(number_to_word(123456789))
print(number_to_word(1001))
print(number_to_word(1000000))
```

Output:

```text
one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
one thousand one
one million
```

## Project Structure

```text
.
├── .gitignore
├── README.md
├── tests
│   └── test_main.py
└── src
    ├── constant.py
    └── main.py
```

- `src/constant.py`: the word lists and number mappings
- `src/main.py`: the number-to-word function and example numbers
- `tests/test_main.py`: basic tests for the number-to-word function
- `README.md`: project documentation
- `.gitignore`: files and folders ignored by Git

## Requirements

- Python 3.9 or later
- pytest

## Installation

Clone the repository:

```bash
git clone https://github.com/mahnazghssm/Number-To-Word.git
cd Number-To-Word
```

Install pytest:

```bash
pip install pytest
```

## Usage

Run the example file from the project root:

```bash
python -m src.main
```

## Testing

Run the tests from the project root:

```bash
pytest
```

## License

This project is licensed under the MIT License.
