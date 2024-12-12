"""
This file will contain the main logic for the game flow
"""
import map, manager, army, agent as ag

NUM_ARMIES = 1
ITERATIONS = 1000
class Directions:
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'
    STOP = 'Stop'

    LEFT =       {NORTH: WEST,
                SOUTH: EAST,
                EAST:  NORTH,
                WEST:  SOUTH,
                STOP:  STOP}

    RIGHT =      dict([(y,x) for x, y in LEFT.items()])

    REVERSE = {NORTH: SOUTH,
            SOUTH: NORTH,
            EAST: WEST,
            WEST: EAST,
            STOP: STOP}


        
class Game:
    def __init__(self, width, height) -> None:
        self.game_map = map.GameMap(width, height)
        self.width = width
        self.height = height

        # Initialize agents 
        self.agents = list()
        for i in range(2):
            agent = ag.Agent(i)
            self.agents.append(agent)

        # Initialize state
        self.state = ag.State(self.agents)


    def play(self):
        print("Game started")
        self.game_map.display_map_coordinates()
        
        while True:
            # Each agent performs Monte Carlo rooted at current state
            for agent in self.agents:
                agent.monte_carlo(self.state)

            # Each agent takes an action

            # Calculate combat if there's collision. 

            # Update state of each agent
            pass
            
        
    