import tkinter as tk
from tkinter import messagebox
from utils.time_utils import check_conflict
import json

class MeetingSchedulerApp:
    def __init__(self, root, agent_system):
        self.root = root
        self.root.title("Smart Office Meeting Scheduler")
        self.root.geometry("400x300")

        # Initialize the agent system passed from main.py
        self.agent_system = agent_system

        # Meeting Schedule List (Initial load)
        self.schedule = self.load_schedule_from_json()  # Load existing schedule from JSON file

        # Title Label
        self.title_label = tk.Label(self.root, text="Meeting Scheduler", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Time Entry
        self.time_label = tk.Label(self.root, text="Enter Time (e.g., 3PM):")
        self.time_label.pack(pady=5)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack(pady=5)

        # Participants Entry
        self.participants_label = tk.Label(self.root, text="Enter Participants (comma separated):")
        self.participants_label.pack(pady=5)
        self.participants_entry = tk.Entry(self.root)
        self.participants_entry.pack(pady=5)

        # Check Conflicts Button
        self.check_button = tk.Button(self.root, text="Check for Conflicts", command=self.check_for_conflict)
        self.check_button.pack(pady=20)

    def check_for_conflict(self):
        # Get the user input for time and participants
        time = self.time_entry.get()
        participants = self.participants_entry.get().split(",")
        participants = [p.strip() for p in participants]  # Clean up extra spaces

        # Check for conflict using the check_conflict function from utils
        if check_conflict(self.schedule, time, participants):
            messagebox.showinfo("Conflict Detected", "There is a scheduling conflict!")
        else:
            messagebox.showinfo("Meeting Scheduled", "Meeting scheduled successfully.")

            # Add the new meeting to the agent system and the schedule
            self.agent_system.schedule_meeting(time, participants)

            # Update the schedule in the GUI after adding
            self.schedule = self.agent_system.get_schedule()

            # Save the updated schedule (both previous and new meetings)
            self.save_schedule_to_json(self.schedule)

    def save_schedule_to_json(self, schedule):
        # Define the path where the schedule JSON file will be saved
        json_file_path = 'data/schedule.json'

        # Write the updated schedule to the JSON file (append new records to the old ones)
        with open(json_file_path, 'w') as json_file:
            json.dump(schedule, json_file, indent=4)

    def load_schedule_from_json(self):
        # Define the path where the schedule JSON file is stored
        json_file_path = 'data/schedule.json'

        # Check if the file exists to prevent errors on first run
        try:
            with open(json_file_path, 'r') as json_file:
                schedule = json.load(json_file)
        except FileNotFoundError:
            schedule = []  # If the file doesn't exist, return an empty list

        return schedule
