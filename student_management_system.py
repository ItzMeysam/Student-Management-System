class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

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
            f"Name: {self.name}\n"
            f"Scores: {self.scores}\n"
            f"Number of scores: {len(self.scores)}\n"
            f"Average: {self.calculate_average():.2f}\n"
            f"Status: {self.get_status()}\n"
            f"Highest score: {self.get_highest_score()}\n"
            f"Lowest score: {self.get_lowest_score()}\n"
        )


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

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

    def remove_student_by_name(self, name):
        self.students = [student for student in self.students if student.name.strip().lower() != name.strip().lower()]

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

            new_student = Student(name, scores)
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
                    manager.remove_student_by_name(name)
                    print("The specified student has been removed!")

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
