import argparse

from study_reminders.logger.logger import Logger
from study_reminders.reminder_scheduler import ReminderScheduler
from study_reminders.student.student_manager import StudentManager
from study_reminders.student_reminder.student_reminder_sender import StudentReminderSender
from study_reminders.student_reminder.student_reminder_manager import StudentReminderManager


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Send reminders immediately (should only for testing).")
    args = parser.parse_args()

    logger = Logger()
    logger.write_log(f"Starting application{' in test mode' if args.test else ''}...")

    student_manager = StudentManager(logger, is_test=args.test)
    student_reminder_manager = StudentReminderManager(student_manager, logger)
    reminder_sender = StudentReminderSender(logger)

    reminder_scheduler = ReminderScheduler(student_reminder_manager, reminder_sender, is_test=args.test)
    reminder_scheduler.run()

    logger.write_log("Shutdown application")


if __name__ == "__main__":
    main()
