from study_reminders.logger.logger import Logger
from study_reminders.reminder.reminder import Reminder
from study_reminders.student.student import Student


class ReminderGenerator:
    """Generates personalized study reminders for students."""

    def __init__(self, logger: Logger) -> None:
        """Initialize the generator with a logger instance."""
        self.__logger = logger

    def generate(self, student: Student) -> Reminder:
        """Create and log a reminder for the given student."""
        reminder = Reminder(f"Hi {student.name}, remember to review {student.course} materials before the deadline!")
        self.__logger.log_generated_reminder(student, reminder)
        return reminder
