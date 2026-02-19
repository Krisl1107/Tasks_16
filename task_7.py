from itertools import permutations
from typing import NoReturn

def permutations_string(numbers: str) -> NoReturn:
    """
    Given a string of natural numbers separated by spaces,
    prints all permutations of these numbers in lexicographical order.

    Args:
        s (str): Input string containing natural numbers separated by spaces.

    Raises:
        ValueError: If the input contains non-natural numbers or is empty.
    """

    if not numbers.strip():
        raise ValueError("Input string is empty.")

    try:
        numbers_int = list(map(int, numbers.strip().split()))
    except ValueError:
        raise ValueError("Input must contain only integers.")

    if any(n <= 0 for n in numbers_int):
        raise ValueError("All numbers must be natural.")

    numbers_int = sorted(numbers_int)

    for var in permutations(numbers_int):
        print(' '.join(map(str, var)))


if __name__ == "__main__":
    input_string = input("Enter natural numbers : ")
    try:
        permutations_string(input_string)
    except ValueError:
        print("Input error")
