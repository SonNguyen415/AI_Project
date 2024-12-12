"""
This file contains code for the agents themselves and their decisions
"""
import army, map, state, itertools



class Tree:
    def __init__(self, root):
        self.root = root



class Node:
    def __init__(self, state: state.State):
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

    def get_legal_actions(self, node: Node, map: map.GameMap):
        """
        Returns all successor nodes given a current node 
        :param state: The current state of all armies of the agent
        :return: A list of list of (army, actions) tuples where actions is a list of legal actions the army can take
        """

        # Retrieves the list of armies
        army_list = node.state.armies

        # Initialize the army legal moves list
        army_legal_moves = list()

        # Loop through the army list to append all army legal moves
        for army in army_list:
            army_legal_moves.append((army, army.get_army_legal_moves(map)))

        # Create list of tuple permutations
        legal_moves = list(itertools.product(*army_legal_moves))

        # Return legal moves as list
        return list(map(list, legal_moves))
    

    def get_successors(self, map: map.GameMap, army_new_positions: list):
        """
        Given a list of army, position tuples, return successor state
        :param state: The list of army, position tuples
        :return: The successor state
        """

        # Initialize list for new army classes
        armies = []

        # Loop through the new positions list
        for army in army_new_positions:
            # Append the successor of the army given the new position
            armies.append(army[0].generate_army_successor(map, army[1]))

        # Return list of successor armies
        return armies
