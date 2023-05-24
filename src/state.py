class State:
    def __init__(self, reward, coordinate, terminal):
        self.value = 0
        self.reward = reward
        self.coordinate = coordinate
        self.terminal = terminal
        self.last_chosen_action = ""

    def convert_action(self, action) -> str:
        if self.last_chosen_action == "(-1, 0)":
            a = "^"
        elif self.last_chosen_action == "(1, 0)":
            a = "v"
        elif self.last_chosen_action == "(0, 1)":
            a = ">"
        elif self.last_chosen_action == "(0, -1)":
            a = "<"
        else:
            a = "-"

        return f"{a}"

    def __str__(self):
        return f"[V:{self.value} A:{self.convert_action(self.last_chosen_action)}]"


