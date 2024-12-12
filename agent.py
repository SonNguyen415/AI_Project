"""
This file contains code for the agents themselves and their decisions
"""
import army, map


START_ARMY_SZ = 20000
N_ARMIES = 1
    

class Tree:
    def __init__(self, root):
        self.root = root


class State: 
    def __init__(self, agents):
        # Current armies
        self.armies = dict()
        for agent in agents:
            self.armies[agent] = [START_ARMY_SZ] * N_ARMIES
    

class Node:
    def __init__(self, state: State):
        # A monte carlo node 
        self.state = state
        self.visited = 0
        self.won = 0
        self.parent = None
        self.successors = list()

    def win_rate(self):
        if self.visited == 0:
            return 0
        return self.won / self.visited
   

class Agent:
    def __init__(self, iterations):        
        # Number of iterations for MCTS
        self.iterations = iterations 

    def monte_carlo(self, state: State):       
        # Root is the current state
        root = Node(state)

        for i in range(self.iterations):
            # Select state until we reach a leaf node
            node = root
            while len(node.successors) > 0:
                node = self.select_state(node)

            # Expand the leaf node
            node.successors = self.get_successors()


            # Select one of the leaf nodes 


            # Rollout
            

            # Back-propagate
            pass

        self.take_action(root.successors)
        return 
    

    def take_action(self, successor_nodes: Node):
        """
        Given a list of successor nodes, choose successor based on win rate, return the corresponding action
        """
        pass

    def select_node(self, node: Node):
        """
        Given a node, select the next node from the list of successors
        """
        # I'm just going with first successor for now
        return state.successors[0]

    def get_legal_actions(self, state):
        """
        Returns all successor states given a current state
        :param state: The current state of all armies of the agent
        :return: A list of (army, actions) tuples wheere actions is a list of legal actions the army can take
        """
        return
    

    def get_successors(self, state: BeliefState):
        """
        Given a belief state, return all possible successor states
        :param state: The current belief state
        :return: The successor state
        """

        # Get the possible army positions of all possible actions
        armies = []

        # For each resultant successor, create a new belief state


        # Add the new belief state to the list of successors of the current state

        # Add the current state as the parent of the new belief state

        
        return 
