def parse_command(command):
    if "schedule" in command:
        return {"intent": "schedule_meeting"}
    elif "turn on" in command:
        return {"intent": "toggle_device", "action": "on"}
    elif "turn off" in command:
        return {"intent": "toggle_device", "action": "off"}
    elif "room" in command and "empty" in command:
        return {"intent": "update_occupancy", "value": False}
    return {"intent": "unknown"}
