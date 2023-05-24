import random
from src.agent import Agent
from src.state import State


class Maze:
    def __init__(self, states: dict[str:State]):
        self.states = states

    def step(self, state_coordinate: tuple[int, int], action: tuple[int, int]) -> State:
        """
        determines the next state if a action would take place
        :param state_coordinate: the coordinate of a state
        :param action: the action the agent wants to take
        :return: the state the agent would land in
        """
        try:
            # adds the coordinate tuple of the input state to the action tuple
            return self.states[f"{tuple(map(sum,zip(state_coordinate, action)))}"]
        except KeyError:
            return self.states[f"{state_coordinate}"]

    def visualize_agent_vision(self, seen_states: dict):
        self.states.update(seen_states)
        print(f"{self.states['(0, 0)']}{self.states['(0, 1)']}{self.states['(0, 2)']}{self.states['(0, 3)']}\n"
              f"{self.states['(1, 0)']}{self.states['(1, 1)']}{self.states['(1, 2)']}{self.states['(1, 3)']}\n"
              f"{self.states['(2, 0)']}{self.states['(2, 1)']}{self.states['(2, 2)']}{self.states['(2, 3)']}\n"
              f"{self.states['(3, 0)']}{self.states['(3, 1)']}{self.states['(3, 2)']}{self.states['(3, 3)']}\n")

