# Logic.py

def calculate_status(average):
    if average >= 18:
        return "Excellent"
    elif average >= 10:
        return "Passed"
    else:
        return "Failed"


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


def delete_student_by_name(students, name):
    target_name = name.strip().lower()
    for index, student in enumerate(students):
        if student["name"].strip().lower() == target_name:
            del students[index]
            return True
    return False


def is_duplicate_name(students, name):
    target_name = name.strip().lower()
    for student in students:
        if student["name"].strip().lower() == target_name:
            return True
    return False
