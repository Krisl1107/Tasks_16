def check_natural_number(prompt):
    """
    Reads a natural number (positive integer) from input with a prompt.
    Returns the entered number or None if invalid.
    """
    number = input(prompt).strip()
    try:
        students = int(number)
        if students > 0:
            return students
        else:
            print("Number must be natural.")
            return
    except ValueError:
        print("Invalid input.")
        return

def check_courses():
    """
    Reads a line of input representing courses taken by a student.
    Returns a set of course names (strings).
    """
    courses = input().strip()
    if courses:
        return set(courses.split())
    else:
        return set()

def main():
    """
     Main function to determine how many courses are chosen by all students.
     If the input for the number of students is invalid, the program terminates with a message.
     """
    students = check_natural_number("Enter the number of students: ")
    if students is None:
        return

    common_courses = set()

    for _ in range(students):
        courses = check_courses()
        if len(common_courses) == 0:
            common_courses = courses
        else:
            common_courses = common_courses.intersection(courses)

    print(len(common_courses))

if __name__ == "__main__":
    main()
