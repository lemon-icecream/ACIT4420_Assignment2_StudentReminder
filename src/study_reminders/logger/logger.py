import datetime

from study_reminders.reminder.reminder import Reminder
from study_reminders.student.student import Student


class Logger:
    """Handles application logging for reminders and student records."""

    def __init__(self, file_path="resources/app_log.txt") -> None:
        """Initialize the logger with a file path for storing logs."""
        self.__file_path = file_path

    def write_log(self, message: str) -> None:
        """Write a timestamped message to the log file and print it."""
        message_with_timestamp = f"{datetime.datetime.now()} - {message}"
        with open(self.__file_path, "a") as log_file:
            log_file.write(f"{message_with_timestamp}\n")
        print(message_with_timestamp)

    def log_sent_reminder(self, student: Student, reminder: Reminder) -> None:
        """Log when a reminder is sent to a student."""
        self.write_log(f"Sent to {student.name} ({student.email}): {reminder.message}")

    def log_generated_reminder(self, student: Student, reminder: Reminder) -> None:
        """Log when a reminder is generated for a student."""
        self.write_log(f"Generated a reminder for {student.name}: {reminder.message}")

    def log_student(self, student: Student) -> None:
        """Log student information currently in the record."""
        self.write_log(f"The following student is in the record: {student}")
