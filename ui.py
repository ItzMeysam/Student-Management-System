# ui.py

from logic import (
    find_student_by_name,
    delete_student_by_name,
    is_duplicate_name,
    create_student
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
    print("8. Exit")
