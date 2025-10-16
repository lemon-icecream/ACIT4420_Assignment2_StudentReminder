import unittest
from unittest.mock import MagicMock

from study_reminders.logger.logger import Logger
from study_reminders.reminder.reminder import Reminder
from study_reminders.student.student import Student
from study_reminders.student_reminder.student_reminder import StudentReminder
from study_reminders.student_reminder.student_reminder_sender import StudentReminderSender


class TestStudentReminderSender(unittest.TestCase):

    def setUp(self):
        self.mock_logger = MagicMock(spec=Logger)
        self.sender = StudentReminderSender(self.mock_logger)

    def test_send_logs_successfully(self):
        student = Student("Alice", "alice@example.com", "Programming")
        reminder = Reminder("Don't forget to review for tomorrow's quiz!")
        student_reminder = StudentReminder(student, reminder)

        self.sender.send(student_reminder)
        self.mock_logger.log_sent_reminder.assert_called_once_with(student, reminder)

    def test_send_raises_error_when_email_missing(self):
        student_no_email = Student("Bob", "", "Math")
        reminder = Reminder("Study calculus before the exam!")
        student_reminder = StudentReminder(student_no_email, reminder)

        with self.assertRaises(ValueError) as context:
            self.sender.send(student_reminder)

        self.assertEqual(str(context.exception), "Email address is missing")
        self.mock_logger.log_sent_reminder.assert_not_called()
