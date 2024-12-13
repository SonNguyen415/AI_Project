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
        armies.append(army.Army(self.agents[1]), START_ARMY_SZ, (height, width))
        self.state = ag.State(self.agents, self.map, armies)
       


    def play(self):
        print("Game started")
        self.map.display_map_coordinates()
        
        while not self.state.is_terminate():
            # Each agent performs Monte Carlo rooted at current state
            for agent in self.agents:
                self.state = agent.monte_carlo(self.state)

            # Calculate combat if there's collision. This will also update the state result
            self.state.combat(self.state.armies)

            # Check if the game is over
            for agent, i in enumerate(self.state.agents):
                if agent.is_win():
                    print(f"Agent {i} wins!")
                    return

        print("Game over")
        
    