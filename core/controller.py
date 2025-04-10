from agents.room_agent import RoomAgent
from agents.meeting_agent import MeetingAgent
from nlp.parser import parse_command


class AgentSystem:
    def __init__(self):
        self.room = RoomAgent("MeetingRoom1")
        self.meeting = MeetingAgent()
        self.schedule = []  # Initialize with an empty schedule

    def handle_command(self, text):
        command = parse_command(text)
        intent = command.get("intent")

        if intent == "schedule_meeting":
            time = command.get("time", "3PM")
            participants = command.get("participants", ["Alice", "Bob"])
            return self.schedule_meeting(time, participants)

        elif intent == "toggle_device":
            device = command.get("device", "lights")
            action = command.get("action", "on")
            return self.toggle_device(device, action)

        elif intent == "update_occupancy":
            value = command.get("value", 0)
            return self.update_occupancy(value)

        return "Sorry, I didn't understand that."

    def schedule_meeting(self, time, participants):
        meeting = {"time": time, "participants": participants}
        self.schedule.append(meeting)  # Add to the schedule
        return meeting

    def toggle_device(self, device, action):
        return self.room.toggle_device(device, action == "on")

    def update_occupancy(self, value):
        return self.room.update_occupancy(value)

    def get_schedule(self):
        # Return the current schedule
        return self.schedule
