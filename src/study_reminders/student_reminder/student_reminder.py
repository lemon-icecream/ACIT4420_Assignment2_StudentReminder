from study_reminders.reminder.reminder import Reminder
from study_reminders.student.student import Student


class StudentReminder:
    """Represents a pairing of a student with a specific reminder."""

    def __init__(self, student: Student, reminder: Reminder) -> None:
        """Initialize with a student and their associated reminder."""
        self.__student = student
        self.__reminder = reminder

    @property
    def student(self) -> Student:
        return self.__student

    @property
    def reminder(self) -> Reminder:
        return self.__reminder
