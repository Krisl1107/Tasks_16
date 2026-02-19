from itertools import combinations
from typing import List


def subsets(numbers: str) -> List[List[int]]:
    """
    Generate all subsets of unique natural numbers from an input string.

    Args:
        s (str): A string of natural numbers separated by spaces.

    Returns:
        List[List[int]]: A list containing all subsets (as lists) of the unique numbers.
    """

    if not numbers or not numbers.strip():
        return [[]]


    try:
        numbers = list(set(int(x) for x in numbers.strip().split()))
    except ValueError:
        raise ValueError("Input must contain only natural numbers.")

    if any(num <= 0 for num in numbers):
        raise ValueError("All numbers must be natural.")

    numbers = sorted(numbers)
    len_number = len(numbers)
    list_subset = []

    for num in range(len_number + 1):
        subsets_r = [list(comb) for comb in combinations(numbers, num)]
        list_subset.extend(subsets_r)

    return list_subset


if __name__ == "__main__":
    try:
        input_str = input("Enter natural numbers").strip()
        subsets = subsets(input_str)
        print("All subsets:")
        for sub in subsets:
            print(sub)
    except ValueError:
        print(f"Input error")
