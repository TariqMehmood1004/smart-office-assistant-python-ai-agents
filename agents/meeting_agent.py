import json, os
from utils.time_utils import check_conflict

class MeetingAgent:
    def __init__(self, schedule_path="data/schedule.json"):
        self.schedule_path = schedule_path
        self.schedule = self.load_schedule()

    def load_schedule(self):
        if os.path.exists(self.schedule_path):
            with open(self.schedule_path) as f:
                return json.load(f)
        return []

    def save_schedule(self):
        with open(self.schedule_path, "w") as f:
            json.dump(self.schedule, f, indent=2)

    def schedule_meeting(self, time, participants):
        if check_conflict(self.schedule, time, participants):
            return "Schedule conflict detected!"
        self.schedule.append({"time": time, "participants": participants})
        self.save_schedule()
        return "Meeting scheduled successfully."
