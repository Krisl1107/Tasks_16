from typing import Optional, List


def input_natural_number() -> Optional[int]:
    """
    Reads a natural number (positive integer) from user input with a prompt.

    Returns:
        The entered natural number as int if valid, otherwise None.
    """
    number = input("Enter the natural number: ").strip()
    try:
        number_int = int(number)
        if number_int > 0:
            return number_int
        else:
            print("Number must be natural.")
            return None
    except ValueError:
        print("Invalid input.")
        return None


def eratosthenes_algorithm(number: int) -> List[int]:
    """
    Finds all prime numbers up to and including the given number using the Sieve of Eratosthenes.

    Parameters:
        number (int): The upper bound of the range to find primes (natural number).

    Returns:
        List[int]: Sorted list of all prime numbers <= number.
    """
    if number < 2:  # no primes less than 2
        return []

    set_er = set(range(2, number + 1))
    limit = int(number ** 0.5) + 1
    for num in range(2, limit):
        if num in set_er:
            # Remove multiples of num starting from num^2
            set_er -= set(range(num * num, number + 1, num))

    return sorted(set_er)


def main() -> None:
    """
    Main function to run the prime number finder program.
    Reads input, validates it and prints all primes up to the input number.
    """
    number = input_natural_number()
    if number is None:
        return
    primes = eratosthenes_algorithm(number)
    print(primes)


if __name__ == "__main__":
    main()
