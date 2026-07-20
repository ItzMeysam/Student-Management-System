# ui.py

from logic import (
    find_student_by_name,
    delete_student_by_name,
    is_duplicate_name,
    create_student,
    get_high_score_students,
    get_failed_students,
    get_class_summary,
    get_lowest_score
)
from storage import save_students_to_file


def handle_delete_student(students):
    delete_name = input("\nEnter student name to delete: ").strip()
    student = find_student_by_name(students, delete_name)

    if student:
        confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ").strip().lower()
        if confirm == "y":
            delete_student_by_name(students, delete_name)
            save_students_to_file(students)
            print("Student deleted successfully.")
        else:
            print("Deletion Cancelled")
    else:
        print("Student not found.")


def edit_student(students, name):
    student = find_student_by_name(students, name)
    if student is None:
        return False

    edit_name_choice = input("Do you want to change name? (y/n) ").strip().lower()

    if edit_name_choice == "y":
        new_name = get_student_name()

        if new_name.strip().lower() != student["name"].strip().lower() and is_duplicate_name(students, new_name):
            print("Student already exists.")
            return False
    elif edit_name_choice == "n":
        new_name = student["name"]
    else:
        print("Invalid choice.")
        return False

    scores = student_score()
    updated_student = create_student(new_name, scores)
    student.update(updated_student)
    return True


def get_number_of_scores():
    while True:
        try:
            number_of_scores = int(input("How many scores? "))
            if number_of_scores > 0:
                return number_of_scores
            else:
                print("Number must be greater than 0.")
        except ValueError:
            print("Please enter a valid score number.")


def get_scores(number_of_scores):
    scores = []
    while len(scores) < number_of_scores:
        try:
            score = float(input(f"Enter score {len(scores) + 1}: "))
            if 0 <= score <= 20:
                scores.append(score)
            else:
                print("Score must be between 0 and 20.")
        except ValueError:
            print("Please enter a valid score.")

    return scores


def get_student_name():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty.")


def student_score():
    number_of_scores = get_number_of_scores()
    return get_scores(number_of_scores)


def display_student(student):
    print("-" * 20)
    print(f"Name: {student['name']}")
    print(f"Scores: {student['scores']}")
    print(f"Count: {len(student['scores'])}")
    print(f"Highest: {student['highest']}")
    print(f"Lowest: {student['lowest']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Status: {student['status']}")
    print("-" * 20)


def show_all_students(students):
    print("\nAll Students:")
    for student in students:
        display_student(student)


def show_menu():
    print("\n--- Student Management Menu ---")
    print("1. Add student")
    print("2. Show all students")
    print("3. Show class average")
    print("4. Show best students")
    print("5. Search student")
    print("6. Edit student")
    print("7. Delete student")
    print("8. Student logs")
    print("9. Exit")


def show_student_list(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        display_student(student)


def student_logs(students):
    while True:
        print("\n" + "-" * 20)
        print("1. Top students")
        print("2. Failed students")
        print("3. Class summary (A, B, C)")
        print("4. Lowest score")
        print("5. Back to main menu")
        print("-" * 20)

        choice = input("Please choose a number: ").strip()
        if choice == "1":
            high_score_students = get_high_score_students(students, threshold=15)
            show_student_list(high_score_students)

        elif choice == "2":
            failed_students = get_failed_students(students)
            show_student_list(failed_students)

        elif choice == "3":
            a_count, b_count, c_count = get_class_summary(students)
            print(f"A Students: {a_count}\n")
            print(f"B Students: {b_count}\n")
            print(f"C Students: {c_count}")

        elif choice == "4":
            lowest_score = get_lowest_score(students)

            if lowest_score is None:
                print("No scores found")
            else:
                print(f"Lowest score: {lowest_score}")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
