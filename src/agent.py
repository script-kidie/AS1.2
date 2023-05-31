import random
import time
from src.state import State
from src.policy import Policy


class Agent:
    def __init__(self, maze, maze_step, policy: Policy, agent_state: State, maze_viz):
        self.maze = maze  # only used for value iteration
        self.maze_step = maze_step
        self.policy = policy
        self.agent_state = agent_state
        self.starting_state = maze.states["(3, 2)"]
        self.seen_states = {}
        self.q_table = {}
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.maze_viz = maze_viz

    def temporal_difference_learning(self, lr, dis) -> None:
        """
        executes temporal difference learning
        :return:
        """
        for i in range(100):
            while not self.agent_state.terminal:
                s = self.agent_state

                if str(s.coordinate) not in self.seen_states.keys():
                    self.agent_state.value = random.randint(0, 40)

                a = self.policy.select_action(s, self.actions, self.maze_step)
                s_prime = self.maze_step(s.coordinate, a)

                self.agent_state.value = s.value + lr * (s_prime.reward + dis * s_prime.value - s.value)
                # update the last chosen action of that state
                self.agent_state.last_chosen_action = str(a)
                # update seen state within the agents memory of discovered states
                self.seen_states[f"{s.coordinate}"] = self.agent_state
                # update current state of the agent
                self.maze_viz(self.seen_states)
                self.agent_state = s_prime

    def add_to_qtable_if_needed(self, state):
        if str(state.coordinate) not in self.q_table.keys():
            self.q_table[str(state.coordinate)] = {"<": 0.0, "v": 0.0, "^": 0.0, ">": 0.0}

    def sarsa(self, lr, dis, eps):
        for i in range(250000):
            while not self.agent_state.terminal:
                s = self.agent_state

                self.add_to_qtable_if_needed(s)

                a = self.policy.select_action(s, actions=["<", "v", "^", ">"], qtable=self.q_table, epsilon=eps)

                a_conv = s.convert_str_to_action(a)

                # let the agent take action
                self.act(a_conv)

                s_pr = self.agent_state
                self.add_to_qtable_if_needed(s_pr)

                a_pr = self.policy.select_action(s_pr, actions=["<", "v", "^", ">"], qtable=self.q_table, epsilon=eps)

                q_func1 = self.q_table[(str(s.coordinate))][a]
                q_func2 = self.q_table[(str(s_pr.coordinate))][a_pr]

                #  calculate new q value and input it to the q table
                self.q_table[(str(s.coordinate))][a] = round(q_func1 + lr * (s_pr.reward + dis*q_func2 - q_func1), 1)

            self.agent_state = self.starting_state

    def value_iteration(self) -> None:
        """
        executes value iteration on the maze for this agent
        :return:
        """
        delta = 0.01
        delta_is_smaller = True

        while delta_is_smaller:
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
                    policy_action = self.policy.select_action(state, self.actions, self.maze_step)
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

    def act(self, action) -> None:
        """
        lets te agent move one step trough the maze, this step is based on what the policy deems best
        :return:
        """
        self.agent_state = self.maze_step(self.agent_state.coordinate, action)
