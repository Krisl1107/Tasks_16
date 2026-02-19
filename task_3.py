from typing import Set, Optional


def check_input_line() -> Set[str]:
    """
    Reads a line of input containing product names separated by spaces.
    Returns a set of product names.
    """
    sweet = input("Enter what Sladkoezhkin or his friend likes: ").strip()
    if sweet:
        return set(sweet.split())
    return set()


def check_natural_number() -> Optional[int]:
    """
    Reads a natural number (positive integer) from input with a prompt.
    Returns the entered number or None if invalid.
    """
    number = input("Enter the number of friends: ").strip()
    try:
        friends = int(number)
        if friends > 0:
            return friends
        else:
            print("Number must be natural.")
            return None
    except ValueError:
        print("Invalid input.")
        return None


def main() -> None:
    """
    Reads Sladkoezhkin's favorite products and preferences of his friends,
    then calculates how many product names are liked only by Sladkoezhkin.

    If the input for the number of friends is invalid, the program prints an error and terminates.
    """
    sweet_products = check_input_line()

    friends = check_natural_number()
    if friends is None:
        print("Invalid input.")
        return

    friends_products: Set[str] = set()

    for _ in range(friends):
        friends_products |= check_input_line()

    only_sweet = sweet_products - friends_products

    print(len(only_sweet))


if __name__ == "__main__":
    main()
