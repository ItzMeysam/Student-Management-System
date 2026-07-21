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