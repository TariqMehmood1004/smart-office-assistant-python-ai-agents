from core.controller import AgentSystem
from interface.cli_interface import start_cli
from gui.scheduler_gui import MeetingSchedulerApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    from core.controller import AgentSystem

    agent_system = AgentSystem()
    app = MeetingSchedulerApp(root, agent_system)
    root.mainloop()
