class State:
    def __init__(self, reward, coordinate, terminal):
        self.value = 0
        self.reward = reward
        self.coordinate = coordinate
        self.terminal = terminal
        self.last_chosen_action = ""

    def convert_action_to_str(self, action) -> str:
        if action == "(-1, 0)":
            a = "^"
        elif action == "(1, 0)":
            a = "v"
        elif action == "(0, 1)":
            a = ">"
        elif action == "(0, -1)":
            a = "<"
        else:
            a = "-"

        return f"{a}"

    def convert_str_to_action(self, string) -> tuple:
        if string == "^":
            a = (-1, 0)
        elif string == "v":
            a = (1, 0)
        elif string == ">":
            a = (0, 1)
        elif string == "<":
            a = (0, -1)
        else:
            raise ValueError("no viable action for this enviroment")

        return a

    def __str__(self):
        return "[{:<8} {:>2}]".format(f"Val:{self.value}", f"A:{self.convert_action_to_str(str(self.last_chosen_action))}")


