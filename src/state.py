class State:
    def __init__(self, reward, coordinate, terminal):
        self.value = 0
        self.reward = reward
        self.coordinate = coordinate
        self.terminal = terminal
        self.last_chosen_action = ""

    def set_value(self, new_value):
        self.value = new_value

    def set_last_chosen_action(self, new_value):
        self.last_chosen_action = new_value

    def __str__(self):
        return f"[R:{self.reward} V:{self.value} A:{self.last_chosen_action}]"


