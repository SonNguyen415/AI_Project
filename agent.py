"""
This file contains code for the agents themselves and their decisions
"""
import army, map


START_ARMY_SZ = 20000

    

class Tree:
    def __init__(self, root):
        self.root = root


class BeliefState: 
    def __init__(self):
        # A copy of our current armies, which includes their observations
        self.armies = list() 
        self.visited = 0
        self.won = 0
        self.parent = None
        self.successors = list()

    def win_rate(self):
        if self.visited == 0:
            return 0
        return self.won / self.visited
   



class Agent:
    def __init__(self, id, iterations, n_armies):
        self.id = id #index of player

        # These values identify the current state of the agent
        self.armies = [START_ARMY_SZ] * n_armies
        self.enemy_count = n_armies
        self.observations = [] # List of locations

        # Number of iterations for MCTS
        self.iterations = iterations 

    def monte_carlo(self):       
        # Make a copy of the current belief state as root
        root = BeliefState() 
        root.armies = self.armies.copy()
        # We'll also need to store all the states we've visited

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

        return 
    


    def update_state(self):
        """
        Update the current belief state for the next position of enemy of the agent based on observation
        """
        # For each army, get the legal moves and generate the successor states
        for army in self.cur_state.armies:
            legal_moves = army.get_army_legal_moves()
            for move in legal_moves:
                successor = army.generate_army_successor(move)
                self.cur_state.successors.append(successor)

        return

    def select_state(self, state: BeliefState):
        """
        Given a state, select the next state from the list of successors
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
