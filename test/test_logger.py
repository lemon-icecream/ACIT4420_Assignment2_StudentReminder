import unittest
from unittest.mock import patch, mock_open

from study_reminders.logger.logger import Logger


class TestLogger(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    @patch("datetime.datetime")
    def test_write_log(self, mock_datetime, mock_file, mock_print):
        mock_datetime.now.return_value = "2025-10-05 10:00:00"

        logger = Logger(file_path="test_log.txt")
        logger.write_log("Test message")

        mock_file.assert_called_once_with("test_log.txt", "a")
        handle = mock_file()
        handle.write.assert_called_once_with("2025-10-05 10:00:00 - Test message\n")
        mock_print.assert_called_once_with("2025-10-05 10:00:00 - Test message")
