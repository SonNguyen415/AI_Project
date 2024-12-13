"""
This file contains code for the agents themselves and their decisions
"""
import game_map, itertools, random, math
    

class State: 
    def __init__(self, agents: list, game_map: game_map.GameMap, armies: list):
        # Current armies
        self.armies = armies
        self.map = game_map
        self.agents = agents
        self.true_state = False


    def get_legal_actions(self, army_list: list):
        """
        Returns possible agent actions, which comes in the forms of permutations of army actions
        :param state: The current state of all armies
        :return: A list of list of (army, position) tuples where position is the new position an army can take
        """

        # Initialize the army legal moves list
        agent_legal_moves = list()

        # Loops through armies in the army list
        for army in army_list:
            # List of (army, move) tuple that maps move to an army
            army_legal_moves = list()
            # Get the legal moves of an army
            army_move_list = army.get_army_legal_moves(self.map)
            # Loop through the army move list
            for army_move in army_move_list:
                # Append each move, the army, and the agent to the legal moves for that army
                army_legal_moves.append((army, army_move))
            # Append the list of legal moves for the army to the overall list
            agent_legal_moves.append(army_legal_moves)

        # Find every permutation of moves the armies can make
        legal_moves = list(itertools.product(*agent_legal_moves))

        # Return legal moves as list
        return list(map(list, legal_moves))
    

    def get_successor(self, army_position_pairs: list):
        """
        Given a list of (army, position) tuples, return successor state
        :param list: The list of (army, position) tuples
        :return: The successor state corresponding to the action
        """

        # Initialize list for new army classes
        armies = list()

        
        # if self.true_state:
        #     print("Get successor")
        #     print(f"Army {self.armies[0].agent.id} at {self.armies[0].position} with {self.armies[0].troops} troops")

        # Loop through the new positions list
        for pair in army_position_pairs:
            #Create army successor
            army_successor = pair[0].generate_army_successor(self.map, pair[1])
            # Append the successor of the army given the new position if it exists
            if army_successor != None:
                armies.append(army_successor)

        # Return list of successor armies
        successor = State(self.agents, self.map, armies)

        # if self.true_state:
        #     print(f"Army {successor.armies[0].agent.id} at {successor.armies[0].position} with {successor.armies[0].troops} troops")

        return successor

    def combat_proposition(self, army_list: list, probability):
        army_state_list = list()
        army_list_stack = list()

        army_list_stack.append((army_list, probability))

        while (len(army_list_stack) > 0):
            armies = army_list_stack.pop()

            army_list0 = list()
            army_list1 = list()

            for army in armies[0]:
                if army.agent.id == 0 :
                    army_list0.append(army)
                else:
                    army_list1.append(army)

            for army0 in army_list0:
                for army1 in army_list1:
                    if army0.position == army1.position:
                        p0 = army0.troops/(army0.troops + army1.troops) * armies[1]
                        p1 = army1.troops/(army0.troops + army1.troops) * armies[1]
                        a0 = list(armies[0])
                        a0.remove(army1)
                        a1 = list(armies[0])
                        a1.remove(army0)
                        army_list_stack.append((a0, p0))
                        army_list_stack.append((a1, p1))
                        continue
            
            army_state_list.append(armies)

        state_list = list()
        for army_state in army_state_list:
            state_list.append((State(self.agents, self.map, army_state[0]), army_state[1]))
        return state_list

    def combat(self, army_list: list):
        army_list0 = list()
        army_list1 = list()
        deleted_list = list()

        for army in army_list:
            if army.agent.id == 0 :
                army_list0.append(army)
            else:
                army_list1.append(army)

        if len(army_list0) == 0 or len(army_list1) == 0:
            return
        

        for army0 in army_list0:
            for army1 in army_list1:
                if army0 in deleted_list or army1 in deleted_list:
                    continue

                if army0.position == army1.position:
                    
                    if self.true_state:
                        print("Combat!")
                        print(f"Army {army0.agent.id} at {army0.position} with {army0.troops} troops")
                        print(f"Army {army1.agent.id} at {army1.position} with {army1.troops} troops")

                    choice = random.choices([0, 1], [army0.troops, army1.troops])
                    if choice[0] == 0:
                        deleted_list.append(army1)
                    else:
                        deleted_list.append(army0)
        for army in deleted_list:
            army_list.remove(army)
                        
        
    def is_terminate(self):
        for agent in self.agents:
            count = 0
            for army in self.armies:
                if army.agent.id == agent.id:
                    count += 1
            if count == 0:
                return True
        return False
                    
    #return sum of remaining army sum. 
    def evaluate(self, agent_id):        
        count = 0
        for army in self.armies:
            if army.agent.id == agent_id:
                count += army.troops
        return count

class Node:
    def __init__(self, state: State, action, p_occur):
        # A monte carlo node 
        self.state = state
        if action == None:
            self.visited = 1
            self.won = 0
        else:
            self.visited = 0
            self.won = 0
        
        self.action = action
        self.p_occur = p_occur
        self.parent = None
        self.successors = list()

    def win_rate(self):
        if self.visited == 0:
            return 0.0
        return self.won / self.visited

    def weighted_win_rate(self):
        return self.win_rate() * self.p_occur
   

class Agent:
    def __init__(self, id: int, iterations: int):        
        # Number of iterations for MCTS
        self.iterations = iterations 
        self.id = id
        self.c = math.sqrt(4)

    def is_win(self, state: State):
        our_count = 0
        enemy_count = 0
        for army in state.armies:
            if army.agent.id == self.id:
                our_count += army.troops
            else:
                enemy_count += army.troops
        return our_count > enemy_count
              
    def display_map_with_armies(self, state: State):    
        """
        This function will print the game map as a grid of characters with armies
        """
        armies = state.armies
        for army in armies:
            print(army.position)
        for row in state.map.map:
            for location in row:
                is_army = False
                for army in armies:
                    if location.coordinates == army.position:
                        print("A", end=" ")
                        is_army = True
                        break
                if not is_army:
                    print(".", end=" ")
            print()



    def rollout(self, node: Node):
        terminal = False
        while not terminal:
            actions = node.state.get_legal_actions(node.state.armies)
            action = actions[random.randint(0, len(actions)-1)]
            node.state = node.state.get_successor(action)
            node.state.combat(node.state.armies)
            terminal = node.state.is_terminate()
        
        return 1 if self.is_win(node.state) else 0
    
    def UCB1(self, node: Node, parent_visited: int):
        if node.visited == 0:
            return float('inf')
        return node.weighted_win_rate() + self.c*(math.sqrt((math.log(parent_visited)/node.visited)))
    
    def get_enemy_armies(self, node: Node):
        armies = []
        for army in node.state.armies:
            if army.agent.id != self.id:
                armies.append(army)
        return armies
    
    def expand(self, node: Node):
        actions = node.state.get_legal_actions(node.state.armies)
        successors = list()
        for action in actions:
            successor = node.state.get_successor(action)
            p_occur = 1/len(node.state.get_legal_actions(self.get_enemy_armies(node)))
            combat_successors = node.state.combat_proposition(successor.armies, p_occur)
            agent_action = list()
            for act in action:
                if act[0].agent.id == self.id:
                    agent_action.append(act)
            if (len(combat_successors) == 0):
                successors.append(Node(successor, agent_action, p_occur))
            else:
                for combat_successor in combat_successors:
                    successors.append(Node(combat_successor[0], agent_action, combat_successor[1]))
        
        for successor in successors:
            successor.parent = node

        return successors

    def select_node(self, node: Node):
        """
        Given a node, select the next node from the list of successors
        """
        max_UCB1_node = node.successors[0]
        max_UCB1 = self.UCB1(node.successors[0], node.visited)
        for successor in node.successors:
            if self.UCB1(successor, node.visited) > max_UCB1:
                max_UCB1 = self.UCB1(successor, node.visited)
                max_UCB1_node = successor

        return max_UCB1_node
    
    def backpropagate(self, node: Node, val: int):
        while node.parent != None:
            node.visited += 1
            node.won += val
            node = node.parent

        node.visited += 1
        node.won += val


    def monte_carlo(self, state: State):       
        # Root is the current state
        root = Node(state, None, 1)

        for _ in range(self.iterations):
            # Select state until we reach a leaf node
            node = root
            while len(node.successors) > 0:
                node = self.select_node(node)
                node.visited += 1

            # Expand the leaf node
            node.successors = self.expand(node)
            if len(node.successors) == 0:
                if self.is_win(node.state):
                    self.backpropagate(node, 1)    
                else:
                    self.backpropagate(node, 0)
            else:
                # Select one of the leaf nodes and rollout
                node = self.select_node(node)
                win = self.rollout(node)
        
                # Back-propagate
                self.backpropagate(node, win)
                
        # Generate a dictionary wherein key=action and value=total utility of said action
        total_utils = dict()
        for successor in root.successors:
            action = tuple(successor.action)
            if action in total_utils:
                total_utils[action] += successor.weighted_win_rate()
            else:
                total_utils[action] = successor.weighted_win_rate()

        if len(total_utils) == 0:
            return None
        
        # Best action is action with highest utility
        best_action = max(total_utils, key=total_utils.get)
        result = state.get_successor(best_action).armies
        return result

