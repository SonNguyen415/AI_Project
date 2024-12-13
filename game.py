"""
This file will contain the main logic for the game flow
"""
import game_map, army
import agent as ag
import locations as loc


class Game:
    def __init__(self, width, height, iterations, start_sz) -> None:
        self.map = game_map.GameMap(width, height)
        self.width = width
        self.height = height

        # Initialize agents 
        self.agents = list()
        self.agents.append(ag.Agent(0, iterations))
        self.agents.append(ag.Agent(1, 20))

        # Initialize state
        armies = list()
        for i, sz in enumerate(start_sz):
            armies.append(army.Army(self.agents[0], sz, (i,0)))

        for i, sz in enumerate(start_sz):
            armies.append(army.Army(self.agents[1], sz, (height-1-i, width-1)))

        print(armies)
        self.state = ag.State(self.agents, self.map, armies)
       

    def display_map_with_armies(self):    
        """
        This function will print the game map as a grid of characters with armies
        """
        the_map = self.map.map
        armies = self.state.armies
        for army in armies:
            print(army.position)
        for row in the_map:
            for location in row:
                is_army = False
                for army in armies:
                    if location.coordinates == army.position:
                        print("A", end=" ") if army.agent.id == 0 else print("B", end=" ")
                        is_army = True
                        break
                if not is_army:
                    # if location.location_type == loc.LocationType.IMPASSABLE:
                    #     print("X", end=" ")
                    # elif location.terrain == loc.TerrainType.WATER:
                    #     print("~", end=" ")
                    # elif location.terrain == loc.TerrainType.FLATLAND:
                    #     print("_", end=" ")
                    # elif location.terrain == loc.TerrainType.HIGHLAND:
                    #     print("^", end=" ")
                    # elif location.terrain == loc.TerrainType.FORESTS:
                    #     print("T", end=" ")
                    # elif location.terrain == loc.TerrainType.MOUNTAIN:
                    #     print("M", end=" ")
                    # else:
                    print(".", end=" ")
            print()


    def play(self):
        print("Game started")
        # self.display_map_with_armies()

        while not self.state.is_terminate():
            self.display_map_with_armies()
            for army in self.state.armies:
                print(f"Army {army.agent.id} at {army.position} with {army.troops} troops")
            print("\n-------------------------------------------------------------------------\n")
            
            # Each agent performs Monte Carlo rooted at current state
            new_armies = list()
            for i, agent in enumerate(self.agents):
                agent_armies = agent.monte_carlo(self.state)
                if agent_armies == None:
                    print(f"Game over! Agent {i} died from attrition!")
                    self.display_map_with_armies()
                    if(i == 0):
                        print(f"Agent 1 wins!")
                        print("Remaining Agent Troops: ", self.state.evaluate(1))
                        return tuple([1,self.state.evaluate(1)])
                    else: 
                        print(f"Agent 0 wins!")
                        print("Remaining Agent Troops: ", self.state.evaluate(0))
                        return tuple([0,self.state.evaluate(0)])

                new_armies.extend(agent_armies)

            self.state = ag.State(self.agents, self.map, new_armies)
            self.state.true_state = True
           
            # Calculate combat if there's collision. This will also update the state result
            self.state.combat(self.state.armies)

            # Check if the game is over
            for i, agent in enumerate(self.state.agents):
                if self.state.is_terminate() and agent.is_win(self.state):
                    print(f"Agent {i} wins!")
                    print("Remaining Agent Troops: ", self.state.evaluate(i))
                    return tuple([i,self.state.evaluate(i)])


        print("Game over")

    