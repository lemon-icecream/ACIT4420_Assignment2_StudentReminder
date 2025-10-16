import unittest
from unittest.mock import MagicMock

from study_reminders.logger.logger import Logger
from study_reminders.reminder.reminder_generator import ReminderGenerator
from study_reminders.student.student import Student


class TestReminderGenerator(unittest.TestCase):

    def test_generate_creates_and_logs_reminder(self):
        mock_logger = MagicMock(spec=Logger)
        reminder_generator = ReminderGenerator(mock_logger)
        student = Student("Alice", "alice@example.com", "Programming")

        reminder = reminder_generator.generate(student)

        expected_message = f"Hi {student.name}, remember to review {student.course} materials before the deadline!"
        self.assertEqual(reminder.message, expected_message)
        mock_logger.log_generated_reminder.assert_called_once_with(student, reminder)
