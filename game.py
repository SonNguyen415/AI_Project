"""
This file will contain the main logic for the game flow
"""
import game_map, army
import agent as ag


class Game:
    def __init__(self, width, height, iterations, start_army_sz) -> None:
        self.map = game_map.GameMap(width, height)
        self.width = width
        self.height = height

        # Initialize agents 
        self.agents = list()
        self.agents.append(ag.Agent(0, iterations))
        self.agents.append(ag.Agent(1, iterations))

        # Initialize state
        armies = list()
        armies.append(army.Army(self.agents[0], start_army_sz, (0,0)))
        armies.append(army.Army(self.agents[1], start_army_sz, (height-1, width-1)))
        self.state = ag.State(self.agents, self.map, armies)
       

    def display_map_with_armies(self):    
        """
        This function will print the game map as a grid of characters with armies
        """
        armies = self.state.armies
        for army in armies:
            print(army.position)
        for row in self.map.map:
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


    def play(self):
        print("Game started")
        # self.display_map_with_armies()

        while not self.state.is_terminate():
            self.display_map_with_armies()
            print("\n-------------------------------------------------------------------------\n")
            # Each agent performs Monte Carlo rooted at current state
            for agent in self.agents:
                self.state = agent.monte_carlo(self.state)

            # Calculate combat if there's collision. This will also update the state result
            self.state.combat(self.state.armies)

            # Check if the game is over
            for i, agent in enumerate(self.state.agents):
                if agent.is_win(self.state):
                    print(f"Agent {i} wins!")
                    return

        print("Game over")
        
    