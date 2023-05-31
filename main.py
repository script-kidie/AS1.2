import random

from src.maze import Maze
from src.policy import Policy
from src.agent import Agent
from src.state import State


greedy_policy = Policy(1)

maze_states_dict = {"(0, 0)": State(-1, (0, 0), False),
                    "(0, 1)": State(-1, (0, 1), False),
                    "(0, 2)": State(-1, (0, 2), False),
                    "(0, 3)": State(40, (0, 3), True),
                    "(1, 0)": State(-1, (1, 0), False),
                    "(1, 1)": State(-1, (1, 1), False),
                    "(1, 2)": State(-10, (1, 2), False),
                    "(1, 3)": State(-10, (1, 3), False),
                    "(2, 0)": State(-1, (2, 0), False),
                    "(2, 1)": State(-1, (2, 1), False),
                    "(2, 2)": State(-1, (2, 2), False),
                    "(2, 3)": State(-1, (2, 3), False),
                    "(3, 0)": State(10, (3, 0), True),
                    "(3, 1)": State(-2, (3, 1), False),
                    "(3, 2)": State(-1, (3, 2), False),
                    "(3, 3)": State(-1, (3, 3), False)}

maze_q_table = {"(0, 0)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(0, 1)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(0, 2)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(0, 3)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(1, 0)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(1, 1)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(1, 2)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(1, 3)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(2, 0)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(2, 1)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(2, 2)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(2, 3)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(3, 0)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(3, 1)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(3, 2)": {"<": 0, "v": 0, "^": 0, ">": 0},
                "(3, 3)": {"<": 0, "v": 0, "^": 0, ">": 0}}

main_maze = Maze(maze_states_dict, maze_q_table)

main_agent = Agent(main_maze, main_maze.step, greedy_policy, maze_states_dict["(3, 2)"], main_maze.visualize_agent_vision)

main_agent.sarsa(0.3, 0.9, 0.1)

main_maze.visualize_agent_qfunctions(main_agent.q_table)

# main_agent.value_iteration()

# main_maze.visualize_agent_vision(main_agent.seen_states)

# main_agent.temporal_difference_learning(0.1, 1)
