import json

from study_reminders.logger.logger import Logger
from study_reminders.student.student import Student


class StudentManager:
    """Manages student data loading, storage, and logging."""

    def __init__(self, logger: Logger, file_path="resources/students.json", *, is_test=False) -> None:
        """Initialize the manager, loading students from a file or test data."""
        if not is_test:
            try:
                with open(file_path, "r") as file:
                    students_json = json.load(file)
            except FileNotFoundError:
                raise ValueError("Student file not found")
        else:
            students_json = [
                {"name": "Alice", "email": "alice@example.com", "course": "Programming", "preferred_time": "22:37"},
                {"name": "Bob", "email": "bob@example.com", "course": "Mathematics", "preferred_time": "22:38"},
                {"name": "Charlie", "email": "charlie@example.com", "course": "Physics", "preferred_time": "22:39"}
            ]
        self.__students = StudentManager.load_student(students_json)
        self.__logger = logger
        self.log_student_list()

    @staticmethod
    def load_student(students_json: dict) -> list[Student]:
        """Convert a JSON list of student data into Student objects."""
        students = []
        for student_json in students_json:
            student = Student(
                student_json["name"],
                student_json["email"],
                student_json["course"],
                student_json["preferred_time"]
            )
            students.append(student)
        return students

    def log_student_list(self) -> None:
        """Log all students currently loaded in the system."""
        for student in self.__students:
            self.__logger.log_student(student)

    @property
    def students(self) -> list[Student]:
        return self.__students
