from src.state import State


class Maze:
    def __init__(self, states: dict[str:State], agent_state: State):
        self.states = states
        self.agent_action: tuple[int, int]
        self.agent_state = agent_state
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def step(self, state: tuple[int, int], action: tuple[int, int]) -> State:
        """
        determines the next state if a action would take place
        :param state: the coordinate of a state
        :param action: the action the agent wants to take
        :return: the state the agent would land in
        """
        try:
            # adds the coordinate tuple of the input state to the action tuple
            return self.states[f"{tuple(map(sum,zip(state, action)))}"]
        except KeyError:
            return self.states[f"{state}"]

    def get_agent_state(self) -> State:
        """
        :return: the State the agent is currently in
        """
        return self.agent_state

    def __str__(self):
        return f"agent location = {self.agent_state}"
