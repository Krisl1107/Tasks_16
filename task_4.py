def input_sets() -> Set[str]:
    """
    Reads a line of input and converts it into a set of strings.
    Ensures that the input is not empty.
    """
    while True:
        line = input("Enter elements of the first set separated by space: ").strip()
        if not line:
            print("Input cannot be empty.")
            continue
        elements = line.split()
        if not elements:
            print("No elements found. Please try again.")
            continue
        return set(elements)


def input_single_element() -> str:
    """
    Reads a single non-empty element from input.
    """
    while True:
        element = input("Enter element: ").strip()
        if element == "":
            print("Input cannot be empty.")
            continue
        if " " in element:
            print("Please enter only one element.")
            continue
        return element


def main() -> None:
    """
    Reads two sets and a single element,
    then checks whether this element belongs to the intersection of the two sets.
    Prints 'Yes' if it does, 'No' otherwise.
    """
    set_1 = input_sets()
    set_2 = input_sets()
    number = input_single_element()

    intersection = set_1.intersection(set_2)

    if number in intersection:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
