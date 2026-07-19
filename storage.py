import json

from logic import create_student


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
