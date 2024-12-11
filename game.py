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
            agent = ag.Agent(i, ITERATIONS, NUM_ARMIES)

            # For each agent, generatese a current belief state
            self.agents.append(agent)

    
    def observation(self):
        # For each army pair (50 such pair for 10 armies / agent)
        # We check if army1 is in any neighbor of army2.
        # Mark corresponding in army1 and army2 neighbors grid.

        # Retrieve all armies
        armies = [[], []]
        for i in range(len(self.agents.armies)):
            for army in self.agents[i]:
                armies[i].append(army)

        # Make observation and update as such for all armies
        for army1 in armies[0]:
            for army2 in armies[1]:
                if army1 != army2:
                    dy =  army1.position[0] - army2.position[0]
                    dx =  army1.position[1] - army2.position[1]       
                    if dy > 1 or dy < -1 or dx > 1 or dx < -1:
                        continue
                    
                    y2, y1 = (0, 2) if dy == -1 else (0, 0) if dy == 0 else (2, 1)
                    x2, x1 = (0, 2) if dx == -1 else (0, 0) if dx == 0 else (2, 1)

                    army1.neighbors[y1, x1] = 1
                    army2.neighbors[y2, x2] = 1
        return 
    


    def play(self):
        print("Game started")
        self.game_map.display_map_coordinates()
        
        while True:
            # Each agent makes an observation and update the current armies
            self.observation()

            # Update belief state given observation

            # Each agent performs Monte Carlo rooted at current belief state

            # Each agent takes an action

            # Calculate combat if there's collision. 
            
        
        print("Game ended")
    