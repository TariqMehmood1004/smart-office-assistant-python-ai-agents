from datetime import datetime


# Utility function to check for scheduling conflicts
def check_conflict(schedule, time, participants):
    """
    Checks if the given time and participants conflict with existing meetings.

    Args:
        schedule (list): The current meeting schedule.
        time (str): The proposed meeting time (e.g., "3PM").
        participants (list): List of participants (e.g., ["Alice", "Bob"]).

    Returns:
        bool: True if there's a conflict, False otherwise.
    """
    # Convert time to datetime object for comparison
    proposed_time = datetime.strptime(time, "%I%p")  # Assuming time is given like "3PM"

    # Check if the proposed time overlaps with existing meetings for the same participants
    for meeting in schedule:
        meeting_time = datetime.strptime(meeting["time"], "%I%p")

        # Compare times (can be extended to compare participants as well)
        if meeting_time == proposed_time:
            return True
    return False
