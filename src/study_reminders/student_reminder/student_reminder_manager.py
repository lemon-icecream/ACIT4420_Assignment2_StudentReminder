from study_reminders.logger.logger import Logger
from study_reminders.reminder.reminder_generator import ReminderGenerator
from study_reminders.student.student_manager import StudentManager
from study_reminders.student_reminder.student_reminder import StudentReminder


class StudentReminderManager:
    """Manages the creation and storage of reminders for all students."""

    def __init__(self, student_manager: StudentManager, logger: Logger) -> None:
        """Generate reminders for each student and store them as StudentReminder objects."""
        reminder_generator = ReminderGenerator(logger)

        self.__student_reminder_list = []
        for student in student_manager.students:
            student_reminder = StudentReminder(student, reminder_generator.generate(student))
            self.__student_reminder_list.append(student_reminder)

    @property
    def student_reminder_list(self) -> list[StudentReminder]:
        return self.__student_reminder_list