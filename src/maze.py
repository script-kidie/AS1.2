from src.state import State


class Maze:
    def __init__(self, states: dict[str:State], agent_coordinate: tuple[int, int]):
        self.states = states
        self.agent_action: tuple[int, int]
        self.agent_coordinate = agent_coordinate
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def step(self, state: tuple[int, int], action: tuple[int, int]) -> State:
        try:
            return self.states[f"{tuple(map(sum,zip(state, action)))}"]
        except KeyError:
            return self.states[f"{state}"]

    def get_agent_state(self) -> int:
        return self.agent_coordinate
