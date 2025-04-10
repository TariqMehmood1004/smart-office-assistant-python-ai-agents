import unittest
from utils.time_utils import check_conflict

class TestTimeUtils(unittest.TestCase):

    def setUp(self):
        # Sample meeting schedule for testing
        self.schedule = [
            {"time": "3PM", "participants": ["Alice", "Bob"]},
            {"time": "4PM", "participants": ["Alice", "Sarah"]}
        ]

    def test_no_conflict(self):
        # Test case where no conflict occurs
        result = check_conflict(self.schedule, "2PM", ["Alice", "Bob"])
        self.assertFalse(result, "Expected no conflict, but found one.")

    def test_time_conflict(self):
        # Test case where a time conflict occurs (same time, same participants)
        result = check_conflict(self.schedule, "3PM", ["Alice", "Bob"])
        self.assertTrue(result, "Expected conflict, but no conflict was found.")

    def test_participant_conflict(self):
        # Test case where there is no conflict in time, but the same participants are already scheduled
        result = check_conflict(self.schedule, "5PM", ["Alice", "Bob"])
        self.assertFalse(result, "Expected no conflict, but found one.")

    def test_participant_time_conflict(self):
        # Test case where a time conflict occurs for the same participants
        result = check_conflict(self.schedule, "4PM", ["Alice", "Sarah"])
        self.assertTrue(result, "Expected conflict, but no conflict was found.")

    def test_different_time_no_conflict(self):
        # Test case where time does not conflict, even with different participants
        result = check_conflict(self.schedule, "5PM", ["John", "Eve"])
        self.assertFalse(result, "Expected no conflict, but found one.")

    def test_empty_schedule(self):
        # Test case with an empty schedule (should return no conflict)
        empty_schedule = []
        result = check_conflict(empty_schedule, "3PM", ["Alice", "Bob"])
        self.assertFalse(result, "Expected no conflict, but found one.")

if __name__ == '__main__':
    unittest.main()
