import schedule
import time

from study_reminders.student_reminder.student_reminder_sender import StudentReminderSender
from study_reminders.student_reminder.student_reminder_manager import StudentReminderManager


class ReminderScheduler:
    """Schedules and sends reminders to students at their preferred times."""

    def __init__(self, student_reminder_manager: StudentReminderManager, student_reminder_sender: StudentReminderSender,
                 *, is_test=False) -> None:
        """Initialize the scheduler with reminder and sender managers."""
        self.__student_reminder_list = student_reminder_manager.student_reminder_list
        self.__student_reminder_sender = student_reminder_sender
        self.__is_test = is_test

    def run(self) -> None:
        """Run the scheduler in normal or test mode."""
        if not self.__is_test:
            self.__run_scheduler()
        else:
            self.__run_test()

    def __run_scheduler(self):
        """Schedule reminders to be sent at each student’s preferred time."""
        for student_reminder in self.__student_reminder_list:
            schedule.every().day.at(student_reminder.student.preferred_time).do(
                lambda sr=student_reminder: self.__student_reminder_sender.send(sr))

        while True:
            schedule.run_pending()
            time.sleep(60)

    def __run_test(self):
        """Immediately send all reminders (used for testing)."""
        for student_reminder in self.__student_reminder_list:
            self.__student_reminder_sender.send(student_reminder)
