import json
import os
import random
from student import Student


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
