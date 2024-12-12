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

        # Retrieve all adversary armies
        adversary_armies = [None for _ in range(len(self.agents))]
        for agent, i in enumerate(self.agents):
            for other in self.agents:
                if agent != other:
                    adversary_armies[i] = other.armies


        # For each agent, check adversary armies
        for agent, i in enumerate(self.agents):
            for army in self.agents[i].armies:
                for enemy in adversary_armies[i]:
                    if army != enemy:
                        dy =  army.position[0] - enemy.position[0]
                        dx =  army.position[1] - enemy.position[1]       
                        if dy > 1 or dy < -1 or dx > 1 or dx < -1:
                            continue
                        agent.observations.append(enemy.position)
        
        return 
    

    def play(self):
        print("Game started")
        self.game_map.display_map_coordinates()
        
        while True:
            # Each agent makes an observation and update the current armies
            self.observation()

            # Each agent performs Monte Carlo rooted at current belief state

            # Each agent takes an action

            # Calculate combat if there's collision. 
            
        
        print("Game ended")
    