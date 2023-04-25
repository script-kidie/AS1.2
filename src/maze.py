from src.state import State


class Maze:
    def __init__(self, state: dict[str:State], agent_action: tuple[int, int], agent_coordinate: tuple[int, int]):
        self.states = state
        self.agent_action = agent_action
        self.agent_coordinate = agent_coordinate

    def step(self, state: tuple[int, int], action: tuple[int, int]):
        return self.states[f"{state + action}"]

    def get_agent_state(self):
        return self.agent_coordinate

