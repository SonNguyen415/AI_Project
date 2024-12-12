"""
This file contains code for the agents themselves and their decisions
"""
import army, game_map, itertools, random


START_ARMY_SZ = 20000
N_ARMIES = 1
    

class State: 
    def __init__(self, agents, game_map: game_map.GameMap):
        # Current armies
        self.armies = dict()
        self.map = game_map
        for agent in agents:
            self.armies[agent] = [START_ARMY_SZ] * N_ARMIES

    def get_legal_actions(self):
        """
        Returns possible agent actions, which comes in the forms of permutations of army actions
        :param state: The current state of all armies
        :return: A list of list of (army, position) tuples where position is the new position an army can take
        """

        # Retrieves the list of armies
        army_list = self.armies

        # Initialize the army legal moves list
        army_legal_moves = list()

        # Loop through the army list to append all army legal moves
        for army in army_list:
            army_legal_moves.append((army, army.get_army_legal_moves(self.map)))

        # Create list of tuple permutations
        legal_moves = list(itertools.product(*army_legal_moves))

        # Return legal moves as list
        return list(map(list, legal_moves))
    

    def get_successor(self, army_position_pairs: list):
        """
        Given a list of (army, position) tuples, return successor state
        :param list: The list of (army, position) tuples
        :return: The successor state corresponding to the action
        """

        # Initialize list for new army classes
        armies = []

        # Loop through the new positions list
        for army in army_position_pairs:
            # Append the successor of the army given the new position
            armies.append(army[0].generate_army_successor(self.map, army[1]))

        # Return list of successor armies
        return armies

    
    def combat(self, agents: list):
        for army0 in self.armies[agents[0]]:
            for army1 in self.armies[agents[1]]:
                if army0.position == army1.position:
                    probability0 = army0.troops/(army0.troops + army1.troops)
                    probability1 = army1.troops/(army0.troops + army1.troops)
                    choice = random.choices([0, 1], [probability0, probability1])
                    if choice == 0:
                        self.armies[agents[1]].remove(army1)
                    else:
                        self.armies[agents[0]].remove(army0)

        
    def is_terminate(self):
        for agent_armies in self.armies:
            if len(agent_armies) == 0:
                return True
        return False

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

        for _ in range(self.iterations):
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
        return node.successors[0]
