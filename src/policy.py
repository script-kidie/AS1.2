import random

from src.state import State
from math import inf


class Policy:
    def __init__(self, gamma):
        self.gamma = gamma

    def select_action(self, input_state: State, actions: list, maze_step=None, epsilon=0, qtable=None) -> tuple:
        highest_value = -inf
        viable_actions = []
        rand_float = random.random()

        # ---------- q table greedy policy  -----------#
        if qtable:
            q_functions = qtable[str(input_state.coordinate)]
            max_qval = max(q_functions.values())
            highest_actions = []

            if epsilon >= rand_float:
                chosen_action = random.choice(actions)

            else:
                for action in q_functions:
                    if q_functions[action] == max_qval:
                        highest_actions.append(action)

                chosen_action = random.choice(highest_actions)

            return chosen_action

        # ---------- non q table greedy policy ------------ #
        else:
            if epsilon >= rand_float:
                chosen_action = random.choice(actions)

            else:
                for action in actions:
                    state_after_action = maze_step(input_state.coordinate, action)
                    value = state_after_action.reward + (self.gamma * state_after_action.value)

                    if value > highest_value:
                        viable_actions = []
                        highest_value = value
                        chosen_action = action

                    elif value == highest_value:
                        viable_actions.append(action)
                        chosen_action = random.choice(actions)

        return chosen_action
