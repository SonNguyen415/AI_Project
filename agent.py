"""
This file contains code for the agents themselves and their decisions
"""
import army
from game import Directions


START_ARMY_SZ = 20000


class State: 
    def __init__(self):
        self.armies = list() 
        self.visited = 0
        self.won = 0

    def win_rate(self):
        if self.visited == 0:
            return 0
        return self.won / self.visited
    

class Agent:
    def __init__(self, id, depth, iterations):
        self.id = id #index of player
        self.armies = [army.Army(START_ARMY_SZ)]
        self.depth = depth # Rollout depth
        self.iterations = iterations # Number of iterations for MCTS

    def monte_carlo(self):
        # Select state 

        # Expand state

        # Take output of get_successors and create the states corresponding to them

        return 
    

    def get_successor_states(self, state):
        """
        Given a state, return the successor states
        """
        state.visited += 1
        return

    def select_state(self):
        return

    def get_legal_actions(self, state: State):
        """
        Returns all the legal actions the agent can take in the current state
        :param state: The current state of all armies of the agent
        :return: A list of (army, actions) tuples wheere actions is a list of legal actions the army can take
        """
        return 
    

    def get_new_successors(self, legal_actions: list):
        """
        Given a list of legal actions, expand and create new successor states. 
        :param action: The action list which consists of the moves of each armies
        :return: The successor state
        """
    
        # 
        return 
