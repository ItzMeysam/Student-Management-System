import json
import os
import random


class Student:
    def __init__(self, student_id, name, scores):
        self.student_id = student_id
        self.name = name
        self.scores = scores

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "scores": self.scores
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["student_id"], data["name"], data["scores"])

    def calculate_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_status(self):
        average = self.calculate_average()
        if average >= 17:
            return "A"
        elif average >= 10:
            return "B"
        else:
            return "C"

    def get_highest_score(self):
        if not self.scores:
            return None
        return max(self.scores)

    def get_lowest_score(self):
        if not self.scores:
            return None
        return min(self.scores)

    def __str__(self):
        return (
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Scores: {self.scores}\n"
            f"Number of scores: {len(self.scores)}\n"
            f"Average: {self.calculate_average():.2f}\n"
            f"Status: {self.get_status()}\n"
            f"Highest score: {self.get_highest_score()}\n"
            f"Lowest score: {self.get_lowest_score()}\n"
        )


class StudentManager:
    def __init__(self, filepath="students.json"):
        self.students = []
        self.filepath = filepath
        self.load_from_file()

    def generate_unique_id(self):
        while True:
            new_id = random.randint(1000, 9999)
            if not any(student.student_id == new_id for student in self.students):
                return new_id

    def save_to_file(self):
        try:
            serialized_students = [student.to_dict() for student in self.students]
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(serialized_students, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_from_file(self):
        if not os.path.exists(self.filepath):
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.students = [Student.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load data... ({e})")
            self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.save_to_file()

    def show_all_students(self):
        self.display_students(self.students)

    def get_failing_students(self):
        failing_students = []
        for student in self.students:
            if student.get_status() == "C":
                failing_students.append(student)
        return failing_students

    def find_student_by_name(self, name):
        matched_students = []
        for student in self.students:
            if student.name.strip().lower() == name.strip().lower():
                matched_students.append(student)
        return matched_students

    def remove_student_by_id(self, student_id):
        original_length = len(self.students)
        self.students = [student for student in self.students if student.student_id != student_id]
        if len(self.students) < original_length:
            self.save_to_file()
            return True
        return False

    @staticmethod
    def display_students(students):
        for student in students:
            print(student)
            print("-" * 20)


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
