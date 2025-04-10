def start_cli(agent_system):
    print("Welcome to Smart Office Assistant!")
    while True:
        user_input = input("> ").lower()
        if "exit" in user_input:
            break
        response = agent_system.handle_command(user_input)
        print(response)
