class RoomAgent:
    def __init__(self, room_id):
        self.room_id = room_id
        self.occupied = False
        self.devices = {'lights': False, 'ac': False}

    def update_occupancy(self, is_occupied):
        self.occupied = is_occupied
        if not is_occupied:
            self.devices['lights'] = False
            self.devices['ac'] = False
            return f"Room {self.room_id} is now empty. Devices turned off."
        return f"Room {self.room_id} is occupied."

    def toggle_device(self, device, state):
        self.devices[device] = state
        return f"{device.capitalize()} in Room {self.room_id} turned {'on' if state else 'off'}."
