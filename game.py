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
        armies.append(army.Army(self.agents[1]), start_army_sz, (height, width))
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
        
    