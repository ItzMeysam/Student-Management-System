from student import Student
from manager import StudentManager


def main():
    manager = StudentManager()

    while True:
        print("\n=== Student Manager ===")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Find Student")
        print("4. Remove Student")
        print("5. Show Failing Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            try:
                count = int(input("How many scores? "))
            except ValueError:
                print("Invalid input.")
                continue

            if count < 0:
                print("Number of scores cannot be negative.")
                continue

            scores = []
            while len(scores) < count:
                try:
                    score = float(input(f"Score {len(scores) + 1}: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if 0 <= score <= 20:
                    scores.append(score)
                else:
                    print("Score must be between 0 and 20.")

            unique_id = manager.generate_unique_id()
            new_student = Student(unique_id, name, scores)
            manager.add_student(new_student)
            print("Student added successfully.")

        elif choice == "2":
            if not manager.students:
                print("No students found yet.")
            else:
                manager.show_all_students()
        elif choice == "3":
            if not manager.students:
                print("No students found yet.")
            else:
                name = input("Enter name: ").strip()
                matched_students = manager.find_student_by_name(name)
                if not matched_students:
                    print("No student found with that name.")
                else:
                    manager.display_students(matched_students)

        elif choice == "4":
            if not manager.students:
                print("No students found yet.")
            else:
                name = input("Enter name: ").strip()
                matched_students = manager.find_student_by_name(name)
                if not matched_students:
                    print("No student found with that name.")
                else:
                    if len(matched_students) == 1:
                        target_student = matched_students[0].student_id
                        manager.remove_student_by_id(target_student)
                        print("The specified student has been removed!")
                    else:
                        print(f"Multiple students found with the name '{name}':")
                        manager.display_students(matched_students)

                        try:
                            target_id = int(input("Enter the 4-digit ID of the student you want to remove: "))
                        except ValueError:
                            print("Invalid ID format. Must be a number.")
                            continue
                        if any(student.student_id == target_id for student in matched_students):
                            manager.remove_student_by_id(target_id)
                            print(f"Student with ID {target_id} has been removed!")
                        else:
                            print("The entered ID does not match any of the found students.")

        elif choice == "5":
            if not manager.students:
                print("No students found yet.")
            else:
                failing_students = manager.get_failing_students()
                if not failing_students:
                    print("No failed students.")
                else:
                    manager.display_students(failing_students)
                    if len(failing_students) == 1:
                        print(f"1 student has failed.")
                    else:
                        print(f"{len(failing_students)} students have failed.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
