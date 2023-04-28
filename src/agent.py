from src.state import State
from src.policy import Policy
from src.maze import Maze


class Agent:

    def __init__(self, maze: Maze, policy: Policy):
        self.maze = maze
        self.policy = policy

    def value_iteration(self) -> None:
        """
        executes value iteration on the maze for this agent
        :return:
        """
        delta = 0.01
        delta_is_smaller = True

        while delta_is_smaller:
            self.show_agent_valuation()
            values = []
            policy_actions = []
            state_coordinates = []
            max_dif = 0

            # fetch a state from the mazes state dictionary so whe can acces its information
            for state_key in self.maze.states:
                state = self.maze.states[state_key]

                # check if the state is not a end state
                if not state.terminal:

                    # determine what action the agent would make
                    policy_action = self.policy.select_action(state, self.maze)
                    # store the state the agent would land in
                    state_after_policy_action = self.maze.step(state.coordinate, policy_action)

                    # value calculation
                    v = state_after_policy_action.reward + (self.policy.gamma * state_after_policy_action.value)

                    values.append(v)
                    policy_actions.append(policy_action)
                    state_coordinates.append(state.coordinate)

                    # store the biggest difference between two iteration of a value so the agent can determine when
                    # to stop the value iteration
                    if abs(self.maze.states[state_key].value - v) > max_dif:
                        max_dif = abs(self.maze.states[state_key].value - v)

            # update all state values
            for i in range(len(values)):
                self.maze.states[f"{state_coordinates[i]}"].value = values[i]
                self.maze.states[f"{state_coordinates[i]}"].last_chosen_action = policy_actions[i]

            if max_dif <= delta:
                delta_is_smaller = False

        else:
            print("Agent ended value iteration")

    def act(self) -> None:
        """
        lets te agent move one step trough the maze, this step is based on what the policy deems best
        :return:
        """
        agent_state = self.maze.get_agent_state()
        action = self.policy.select_action(agent_state, self.maze)
        self.maze.agent_state = self.maze.step(agent_state, action)

    def show_agent_valuation(self) -> None:
        """
        prints the reward, value and action chosen for every state the agent can see
        :return:
        """
        print(f"{self.maze.states['(0, 0)']}{self.maze.states['(0, 1)']}{self.maze.states['(0, 2)']}{self.maze.states['(0, 3)']}")
        print(f"{self.maze.states['(1, 0)']}{self.maze.states['(1, 1)']}{self.maze.states['(1, 2)']}{self.maze.states['(1, 3)']}")
        print(f"{self.maze.states['(2, 0)']}{self.maze.states['(2, 1)']}{self.maze.states['(2, 2)']}{self.maze.states['(2, 3)']}")
        print(f"{self.maze.states['(3, 0)']}{self.maze.states['(3, 1)']}{self.maze.states['(3, 2)']}{self.maze.states['(3, 3)']}\n")
