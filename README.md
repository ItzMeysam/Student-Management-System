# Student Management System (CLI)

A modular, Object-Oriented Python application designed to manage student records, track academic scores, calculate statistics, and persist data using JSON files.

## Features

- **Object-Oriented Programming (OOP):** Built using distinct classes for `Student` and `StudentManager` models to enforce encapsulation and separation of concerns.
- **Modular Architecture:** The codebase is split into reusable modules (`student.py`, `manager.py`, and `main.py`) for clean code practices.
- **Data Persistence:** Automatically saves and loads student profiles to/from a local `students.json` file.
- **Unique Identifier (ID) System:** Generates random, non-repeating 4-digit IDs for each student to prevent identity conflicts (e.g., handling students with identical names).
- **Academic Performance Analysis:** Calculates averages, grades students (A, B, C), and extracts highest, lowest, and failing scores.
- **Robust Error Handling:** Validates user inputs (numeric check, range checks for scores between 0 and 20) and handles potential file IO / JSON parsing errors gracefully.

## Project Structure

- `main.py`: Application entry point and CLI menu loop.
- `manager.py`: Handles student collection operations (add, remove, search, JSON I/O).
- `student.py`: Student class representation and statistical calculations.
- `students.json`: Persistent JSON data storage (auto-generated).

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Git (optional, for cloning the repository).

### Installation & Execution
1. Clone this repository to your local machine:
   git clone <YOUR_REPOSITORY_URL>

2. Navigate to the project directory:
   cd pythonProject2

3. Run the application:
   python main.py

## How to Use
Upon execution, a menu will prompt you with the following choices:
1. **Add Student:** Enter student name and input their scores. The system generates a unique 4-digit ID automatically.
2. **Show All Students:** Display all registered students with their ID, name, list of scores, average, status grade, and min/max scores.
3. **Find Student:** Search for students by name.
4. **Remove Student:** Delete a student profile. If duplicate names exist, the system will prompt you for the specific 4-digit ID to ensure precise removal.
5. **Show Failing Students:** Filters and displays students with an average score below 10 (Status C).
6. **Exit:** Safely exit the application.
