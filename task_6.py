from itertools import permutations


def hod_mat() -> None:
    """
    Solves the cryptarithm where:
    ХОD + ХОD + ХОD = МАТ,
    each letter represents a unique digit,
    Х and М cannot be zero (leading digits).

    The function finds and prints all solutions where the equation holds.

    No parameters.

    Prints:
        Each solution in the format 'ХОД+ХОД+ХОД=МАТ'.
    """
    digits = range(10)
    letters = ('Х', 'О', 'D', 'М', 'А', 'Т')

    solutions: List[Tuple[int, int]] = []

    for var in permutations(digits, len(letters)):
        X, O, D, M, A, T = var

        if X == 0 or M == 0:
            continue

        if len(set(var)) != len(letters):
            continue

        hod = X * 100 + O * 10 + D
        mat = M * 100 + A * 10 + T

        if 3 * hod == mat:
            solutions.append((hod, mat))

    solutions.sort(key=lambda x: x[0])

    for hod, mat in solutions:
        print(f"{hod}+{hod}+{hod}={mat}")


if __name__ == "__main__":
    hod_mat()
