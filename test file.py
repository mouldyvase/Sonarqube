import time
import unittest
from unittest.mock import patch
from io import StringIO
from your_notification_script import main  # Import your script's main function

class TestNotificationScript(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_notification(self, mock_stdout):
        with patch('plyer.notification.notify') as mock_notify:
            main()

        mock_notify.assert_called_with(
            title="ALERT!!!",
            message="Take a break! It has been an hour!",
            timeout=10
        )

    @patch('time.sleep')
    def test_notification_interval(self, mock_sleep):
        with patch('plyer.notification.notify') as mock_notify:
            main()

        mock_sleep.assert_called_with(3600)

if __name__ == "__main__":
    unittest.main()
