from typing import List, Optional


def check_natural_numbers() -> Optional[List[int]]:
    """
    Prompts the user to input a sequence of natural numbers separated by spaces.
    Validates the input to ensure all entries are positive integers.

    Returns:
        list[int] or None: List of integers if input is valid, otherwise None.
    """
    subsequence = input("Enter a sequence of natural "
                        "numbers separated by spaces: ").strip()
    try:
        num_split = subsequence.split()
        numbers = [int(num) for num in num_split]
        if all(num > 0 for num in numbers):
            return numbers
        else:
            print("All numbers must be natural.")
            return None
    except ValueError:
        print("Invalid input")
        return None


def check_single_number() -> Optional[int]:
    """
    Prompts the user to input a single natural number.
    Validates that the input is a positive integer.

    Returns:
        int or None: The number if input is valid, otherwise None.
    """
    single_number = input("Enter one natural number: ").strip()
    try:
        nat_number = int(single_number)
        if nat_number > 0:
            return nat_number
        else:
            print("The number must be natural.")
            return None
    except ValueError:
        print("Invalid input")
        return None


def main() -> None:
    """
    Checks if the number appears in the list of repeated numbers in the sequence.
    Prints 'Yes' if it does, otherwise 'No'.
    """
    numbers = check_natural_numbers()
    number = check_single_number()

    unique = []
    repeating = set()

    if numbers is None or number is None:
        print("Incorrect input, program terminated.")
    else:
        for num in numbers:
            if num in unique:
                repeating.add(num)
            else:
                unique.append(num)

        if number in repeating:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
