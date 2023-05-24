import random

from src.state import State
from math import inf


class Policy:
    def __init__(self, gamma):
        self.gamma = gamma

    def select_action(self, input_state: State, actions: list, maze_step, epsilon=0) -> tuple:
        highest_value = -inf

        for action in actions:
            state_after_action = maze_step(input_state.coordinate, action)

            value = state_after_action.reward + (self.gamma * state_after_action.value)

            if value > highest_value:
                highest_value = value
                chosen_action = action

            if epsilon < random.randint(0, 1):
                return random.choice(actions)

        return chosen_action
