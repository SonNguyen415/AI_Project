import game_map, army
import agent as ag


class Game:
    def __init__(self, width, height, iterations, start_sz,verbose) -> None:
        self.map = game_map.GameMap(width, height)
        self.width = width
        self.height = height
        self.agent1_iterations = 1
        # Initialize agents 
        self.agents = list()
        self.agents.append(ag.Agent(0, iterations))
        self.agents.append(ag.Agent(1, self.agent1_iterations))
        self.verbose = verbose

        # Initialize state
        armies = list()
        for i, sz in enumerate(start_sz):
            armies.append(army.Army(self.agents[0], sz, (i,0)))

        for i, sz in enumerate(start_sz):
            armies.append(army.Army(self.agents[1], sz, (height-1-i, width-1)))
        self.state = ag.State(self.agents, self.map, armies)
       

    def display_map_with_armies(self):    
        """
        This function will print the game map as a grid of characters with armies
        """
        the_map = self.map.map
        armies = self.state.armies
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
        print("\tGame started")
        moves = 0

        while not self.state.is_terminate():
            moves += 1
            if self.verbose:
                self.display_map_with_armies()
                for army in self.state.armies:
                    print(f"Army {army.agent.id} at {army.position} with {army.troops} troops. Correspond to map above.")
                
            # Each agent performs Monte Carlo rooted at current state
            new_armies = list()
            for i, agent in enumerate(self.agents):
                agent_armies = agent.monte_carlo(self.state)
                if agent_armies is None:
                    winner = 0 if i == 1 else 1
                    print(f"\tAgent {winner} wins after {moves} moves. Last enemy died from attrition!")
                    if self.verbose:
                        print("\tRemaining Agent Troops:", self.state.evaluate(i))
                    return tuple([winner,self.state.evaluate(winner)])
                new_armies.extend(agent_armies)

            self.state = ag.State(self.agents, self.map, new_armies)
            self.state.true_state = True

            # Check if the game is over
            for i, agent in enumerate(self.state.agents):
                if self.state.is_terminate() and agent.is_win(self.state):
                    print(f"\tAgent {i} wins after {moves} moves. Last enemy died from attrition!")
                    if self.verbose:
                        print("\tRemaining Agent Troops:", self.state.evaluate(i))
                    return tuple([i,self.state.evaluate(i)])
                
            self.state.combat(new_armies)
           
            # Check if the game is over
            for i, agent in enumerate(self.state.agents):
                if self.state.is_terminate() and agent.is_win(self.state):
                    print(f"\tAgent {i} wins after {moves} moves!")
                    if self.verbose:
                        print("\tRemaining Agent Troops:", self.state.evaluate(i))
                    return tuple([i,self.state.evaluate(i)])

        print("\tGame over. Draw!. Total Moves:", moves)
