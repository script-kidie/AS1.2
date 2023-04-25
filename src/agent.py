from src.state import State
from src.policy import Policy
from src.maze import Maze


class Agent:

    def __init__(self, maze: Maze, policy: Policy, terminal: bool):
        self.maze = maze
        self.policy = policy
        self.terminal = terminal

    def value_function(self):
        self.maze.get_agent_state()
