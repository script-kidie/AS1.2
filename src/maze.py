import random
import time
from typing import Tuple

from src.agent import Agent
from src.state import State


class Maze:
    def __init__(self, states: dict[str:State], maze_qtable):
        self.states = states
        self.maze_qtable = maze_qtable

    def step(self, state_coordinate: Tuple[int, int], action: Tuple[int, int]) -> State:
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

    def initialize_state_values(self, new_value=None) -> None:
        """
        function to initialize al values of every state in the maze
        """
        if new_value:
            for i in self.states:
                self.states[i].value = new_value
        else:
            for i in self.states:
                self.states[i].value = random.randint(0, 40)

    def visualize_agent_vision(self, state_values: dict) -> None:
        tmp = []
        for i in self.states:
            tmp.append(self.states[i].value)

        for key in state_values:
            self.states[key].value = state_values[key]

        print(f"{self.states['(0, 0)']}{self.states['(0, 1)']}{self.states['(0, 2)']}{self.states['(0, 3)']}\n"
              f"{self.states['(1, 0)']}{self.states['(1, 1)']}{self.states['(1, 2)']}{self.states['(1, 3)']}\n"
              f"{self.states['(2, 0)']}{self.states['(2, 1)']}{self.states['(2, 2)']}{self.states['(2, 3)']}\n"
              f"{self.states['(3, 0)']}{self.states['(3, 1)']}{self.states['(3, 2)']}{self.states['(3, 3)']}")

        counter = 0
        for key in self.states:
            self.states[key].value = tmp[counter]
            counter += 1
        time.sleep(2)

    def visualize_agent_qfunctions(self, agent_qtable: dict):
        self.maze_qtable.update(agent_qtable)

        for i in range(4):
            print(self.maze_qtable[f"({i}, 0)"], self.maze_qtable[f"({i}, 1)"],
                  self.maze_qtable[f"({i}, 2)"], self.maze_qtable[f"({i}, 3)"])
        print("\n")

