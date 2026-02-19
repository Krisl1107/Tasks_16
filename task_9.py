from itertools import combinations
from typing import List

def k_subsets(numbers_str: str, k_str: str) -> List[List[int]]:
    """
    Generates all k-element subsets from a set of unique natural numbers provided as strings.

    Args:
        numbers_str (str): A string of natural numbers separated by spaces.
        k_str (str): A string representing the number of elements in each subset.

    Returns:
        List[List[int]]: A list containing all k-element subsets of the set.
    """

    if not numbers_str or not numbers_str.strip():
        raise ValueError("Input set of numbers cannot be empty.")

    try:
        numbers_list = list(set(int(x) for x in numbers_str.strip().split()))
    except ValueError:
        print("All inputs must be natural numbers.")

    if any(num <= 0 for num in numbers_list):
        raise ValueError("All numbers must be natural (positive integers).")

    try:
        k_number = int(k_str)
    except ValueError:
        print("K must be an integer.")
    if k_number <= 0:
        raise ValueError("K must be a positive integer.")
    if k_number > len(numbers_list):
        raise ValueError("K must be less than or equal to the number of elements in the set.")

    numbers_list.sort()

    subsets = [list(comb) for comb in combinations(numbers_list, k_number)]
    return subsets


if __name__ == "__main__":
    try:
        numbers_input = input("Enter a set of unique natural numbers: ").strip()
        k_input = input("Enter the size of subsets (K): ").strip()
        result_subsets = k_subsets(numbers_input, k_input)

        print(f"All {len(result_subsets)} subsets of size {k_input}:")

        for subset in result_subsets:
            print(subset)

    except ValueError:
        print("Input error")
