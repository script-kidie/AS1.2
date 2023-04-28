import sys

from src.state import State
from src.policy import Policy
from src.maze import Maze


class Agent:

    def __init__(self, maze: Maze, policy: Policy, current_state: State):
        self.maze = maze
        self.policy = policy
        self.current_state = current_state

    def value_iteration(self) -> None:
        values = []
        policy_actions = []
        state_coordinates = []
        for state_key in self.maze.states:
            state = self.maze.states[state_key]

            if not state.terminal:

                policy_action = self.policy.select_action(state, self.maze)
                state_after_policy_action = self.maze.step(state.coordinate, policy_action)

                v = state_after_policy_action.reward + (self.policy.gamma * state_after_policy_action.value)

                values.append(v)
                policy_actions.append(policy_action)
                state_coordinates.append(state.coordinate)

        for i in range(len(values)):
            self.maze.states[f"{state_coordinates[i]}"].value = values[i]
            self.maze.states[f"{state_coordinates[i]}"].last_chosen_action = policy_actions[i]

    def act(self) -> None:
        action = self.policy.select_action(self.current_state, self.maze)
        self.current_state = self.maze.step(self.current_state, action)
