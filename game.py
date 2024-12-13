"""
This file will contain the main logic for the game flow
"""
import game_map, random, army, agent as ag

ITERATIONS = 1000
START_ARMY_SZ = 20000
N_ARMIES = 1

class Game:
    def __init__(self, width, height) -> None:
        self.map = game_map.GameMap(width, height)
        self.width = width
        self.height = height

        # Initialize agents 
        self.agents = list()
        self.agents.append(ag.Agent(0, ITERATIONS))
        self.agents.append(ag.Agent(1, ITERATIONS))

        # Initialize state
        armies = list()
        armies.append(army.Army(self.agents[0], START_ARMY_SZ, (0,0)))
        armies.append(army.Army(self.agents[1], START_ARMY_SZ, (height-1, width-1)))
        self.state = ag.State(self.agents, self.map, armies)
       


    def play(self):
        print("Game started")
        self.map.display_map_coordinates()
        
        while True:
            # Each agent performs Monte Carlo rooted at current state
            for agent in self.agents:
                agent.monte_carlo(self.state)

            # Get successor states of agent actions


            # Calculate combat if there's collision. This will also update the state result
            self.state.combat(self.agents)

            pass
            
        
    