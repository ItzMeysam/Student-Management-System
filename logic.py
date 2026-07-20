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
    return any(student["name"].strip().lower() == name.strip().lower() for student in students)


def get_high_score_students(students, threshold=15):
    return [student for student in students if all(score >= threshold for score in student["scores"])]


def get_failed_students(students):
    return [student for student in students if student["status"] == "Failed"]


def get_class_summary(students):
    a_count = 0
    b_count = 0
    c_count = 0
    for student in students:
        if student["average"] >= 17:
            a_count += 1
        elif student["average"] >= 10:
            b_count += 1
        else:
            c_count += 1
    return a_count, b_count, c_count


def get_lowest_score(students):
    all_scores = []

    for student in students:
        all_scores.extend(student["scores"])

    if not all_scores:
        return None

    return min(all_scores)
