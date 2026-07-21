# Student Management System (CLI)

A clean and modular Python application designed to manage student records using Object-Oriented Programming (OOP) principles. This system allows for adding, searching, removing, and analyzing student academic performance through a Command Line Interface.

## Key Features

- **OOP Architecture:** Organized into `Student` and `StudentManager` classes for better maintainability.
- **Academic Metrics:** Automatic calculation of average scores, highest/lowest grades, and letter-based status (A, B, C).
- **Advanced Search & Filtering:** Case-insensitive search and filtering for failing students.
- **Robust Input Validation:** Uses `try-except` blocks to handle invalid numeric inputs and ensures scores remain within the 0-20 range.
- **Standardized Output:** Implements the `__str__` magic method for clean and consistent student data representation.

## Technical Highlights

- **Static Methods:** Efficient use of `@staticmethod` for utility functions like `display_students`.
- **List Comprehensions:** Used for optimized student removal logic.
- **Error Handling:** Prevention of crashes from empty names, negative counts, or invalid score types.

## How to Run

1. Make sure you have Python installed.
2. Clone this repository or download `main.py`.
3. Run the application:

```bash
python main.py
```

## Sample Interface

```text
=== Student Manager ===
1. Add Student
2. Show All Students
3. Find Student
4. Remove Student
5. Show Failing Students
6. Exit
Enter your choice: 2

Name: Ali
Scores: [18.0, 19.5, 17.0]
Number of scores: 3
Average: 18.17
Status: A
Highest score: 19.5
Lowest score: 17.0
--------------------
```

## Future Improvements

- Implement JSON file persistence to save data permanently.
- Add functionality to edit existing student records.
- Modularize the project into multiple files for better scalability.
