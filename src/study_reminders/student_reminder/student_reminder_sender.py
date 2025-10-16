from study_reminders.logger.logger import Logger
from study_reminders.student_reminder.student_reminder import StudentReminder


class StudentReminderSender:
    """Handles sending reminders to students and logging the action."""

    def __init__(self, logger: Logger) -> None:
        """Initialize the sender with a logger instance."""
        self.__logger = logger

    def send(self, student_reminder: StudentReminder) -> None:
        """Send a reminder to a student and log the event."""
        student = student_reminder.student
        reminder = student_reminder.reminder
        if not student.email:
            raise ValueError("Email address is missing")
        self.__logger.log_sent_reminder(student, reminder)
