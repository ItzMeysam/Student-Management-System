import json


def save_students_to_file(students):
    try:
        data_to_save = [
            {
                "name": student["name"],
                "scores": student["scores"]
            }
            for student in students
        ]

        with open("students.json", "w") as file:
            json.dump(data_to_save, file, indent=4)
    except IOError:
        print("Error: Could not save data to file.")


def load_students_from_file():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            if not isinstance(data, list):
                return []

            students = []
            for item in data:
                if not isinstance(item, dict):
                    continue

                name = item.get("name")
                scores = item.get("scores")

                if not name or not isinstance(scores, list) or not scores:
                    continue

                if not all(isinstance(score, (int, float)) and 0 <= score <= 20 for score in scores):
                    continue

                students.append(create_student(name, scores))

            return students

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File is corrupted. Starting with empty student list.")
        return []


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


def calculate_status(average):
    if average >= 18:
        return "Excellent"
    elif average >= 10:
        return "Passed"
    else:
        return "Failed"


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


def create_student(name, scores):
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    status = calculate_status(average)

    return {
        "name": name,
        "scores": scores,
        "highest": highest,
        "lowest": lowest,
        "average": average,
        "status": status
    }


def get_class_average(students):
    if not students:
        return 0

    return sum(student["average"] for student in students) / len(students)


def get_best_students(students):
    if not students:
        return []

    highest_average = max(student["average"] for student in students)
    return [student for student in students if student["average"] == highest_average]


def find_student_by_name(students, name):
    target_name = name.strip().lower()
    for student in students:
        if student["name"].strip().lower() == target_name:
            return student
    return None


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


def delete_student_by_name(students, name):
    target_name = name.strip().lower()
    for index, student in enumerate(students):
        if student["name"].strip().lower() == target_name:
            del students[index]
            return True
    return False


def handle_delete_student(students):
    delete_name = input("\nEnter student name to delete: ").strip()
    deleted = delete_student_by_name(students, delete_name)

    if deleted:
        save_students_to_file(students)
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def is_duplicate_name(students, name):
    target_name = name.strip().lower()
    for student in students:
        if student["name"].strip().lower() == target_name:
            return True
    return False


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


def main():
    print("Welcome!")
    students = load_students_from_file()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = get_student_name()

            if is_duplicate_name(students, name):
                print("Student already exists.")
            else:
                scores = student_score()
                student = create_student(name, scores)

                display_student(student)
                students.append(student)
                save_students_to_file(students)

        elif choice == "2":
            if students:
                sorted_students = sorted(students, key=lambda student: student["average"], reverse=True)
                show_all_students(sorted_students)
            else:
                print("No students found.")

        elif choice == "3":
            if students:
                class_average = get_class_average(students)
                print(f"\nClass Average: {class_average:.2f}")
            else:
                print("No students found.")

        elif choice == "4":
            if students:
                print("\nBest student(s):")
                best_students = get_best_students(students)
                for student in best_students:
                    print(f"Name: {student['name']}")
                    print(f"Average: {student['average']:.2f}")
                    print(f"Status: {student['status']}")
                    print("-" * 20)
            else:
                print("No students found.")

        elif choice == "5":
            if students:
                search_name = input("\nEnter student name to search: ").strip()
                found_student = find_student_by_name(students, search_name)

                if found_student:
                    print("\nStudent found:")
                    display_student(found_student)

                else:
                    print("Student not found.")
            else:
                print("No students found.")

        elif choice == "6":
            if students:
                edit_name = input("\nEnter student name to edit: ").strip()
                edited = edit_student(students, edit_name)

                if edited:
                    print("Student updated successfully.")
                    save_students_to_file(students)
                else:
                    print("Student not found.")
            else:
                print("No students found.")

        elif choice == "7":
            if students:
                handle_delete_student(students)
            else:
                print("No students found.")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
# this is a test for git