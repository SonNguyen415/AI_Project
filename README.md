# AI_Project

This is the AI Algorithms project. The goal is to develop a strategy game AI to defeat an enemy with uncertain combat outcomes for the purpose of carrying over the code to a future project, namely a strategy game. Every army must move during the game, and all movements result in some attrition rate to the army, proportional to the army sizes and dependent on the terrain. The win condition is to reduce the enemy's total number of armies to 0. The game takes place on a randomized map with randomized terrain. 

### Software and Hardware ###
All code is implemented on python and utilizes public python libraries. The hardware utilized include Mac and Windows computers.

### Detailed Overview ###
We implemented a grid-based map generation system for a game, where the map is composed of Location objects arranged in a 2D grid. Each location is assigned a terrain type (e.g., Flatland, Water, Mountain) and a location type (Passable, Impassable) based on weighted randomization. Special rules are applied, such as making 25% of mountain terrains impassable. Each location also has attributes like coordinates, a controller (initially 0), and a path cost, which is determined by the terrain type (Water has the highest movement cost). The GameMap class includes methods to generate the map, assign terrains, compute movement costs between locations, and display the map in various formats.

We then implemented an army class for the game. Every army is associated with an agent. Within `army.py` we defined the core logic for managing armies in a game, focusing on their legal moves and state updates. Each Army object is characterized by an agent (controlling entity), the number of troops, and its current position on the game map. The `get_army_legal_moves` method calculates all valid moves the army can make from its current position. The `generate_army_successor` method creates a new Army instance representing the state after moving to a new position, factoring in attrition based on the terrain's path cost. Attrition decreases the troop count, and if it falls to zero, the move is invalid, returning None. 

The core logic of the game was implemented in `agent.py`. The `State` class represents the current game state, which captures information about all armies within the map, and also stores the agents playing. This class has absolute information of the entirety of the state space and is where all methods that require such information reside. The only aspect of the state space that changes from state to state are the armies. This information is held in a list of all armies. Which agent an army belongs to can be distinguished by the Agent attribute in the Army class. The `State` class includes methods for generating legal actions, creating successor states, resolving combat, checking for termination, and evaluating utility for an agent. A legal action is a list of armies and their new position, which is in the form of a list of tuples. The list of legal actions would be a list of list of tuples. To get all possible legal actions of a state, the function finds every possible permutation of army movement. The successor function utilizes a legal action to produce the correct state successor. There exists two combat functions, `combat_proposition` and `combat`, which provide are utilized by monte carlo and simulation/gameplay respectively. The first method produces a list of successor states after combat if there are collisions detected. The second method provides the combat diceroll for actual gameplay and simulation. Finally, the remaining functions are for termination which is relevant for monte carlo tree search and evaluation which is important for final testing and results.

The Node class represents a node in the MCTS tree, storing a copy of the game state, action, visit and win counts, and providing utility calculations like win rate and weighted win rate. Weighted win rate is calculated as the win rate multiplied by the probability of the node occurring. We included this because a node can have different probabilities of occurrence based on combat results. 

The Agent class models decision-making entities, leveraging MCTS to explore possible future states and determine optimal actions. It defines the win condition as the reduction of all enemy armeis to 0 while we still have at least 1 army. 


### To Run ###
To run:
```bash
python3 main.py
```

This will run our default scenario. Each agent has 2 armies (2000 and 3000 troops), operating on a 10x10 map (to reduce the number of moves needed for the simulation, but tests were done on larger map)
1 agent has 100 Monte Carlo iterations, the other runs a single iteration. This scenario took approximately 1-2 minutes to run on `wsl` for around 200-300 moves.    

To run our benchmark, which runs multiple scenarios, go into `main.py` and set `TEST` to true
To run third scenario, go into `main.py` and set `THIRD` to true
To see the map on each step, set `VERBOSE` to true in `main.py`
Our benchmark display results as we increase the number of iterations of MCTS for a single agent.

### Expected Results for Tests ###
We conducted our tests over 25 trials on a 10x10 map with 2 armies per agent, each 1000 and 3000 respectively. Running the first 2 scenarios took around 18 minutes.
Agent 1 is a constant, performing Monte Carlo a single time, effectively random.
Agent 0 iterates either 1, 100, or 1000 times based on the scenario. Default scenario is 100.

For scenario 1, we expected a winrate of Agent 0 and 1 of 50-50.
For scenario 2, we expected that Agent 0 will do slightly better.
For scenario 3, we expected further improvement.

Results:
We found minimal, if any improvement across the the scenarios. 
Scenario 1 resulted in Agent 0 winning 14 times with 109 troops left on average, Agent 1 won 11 times with 296 troops left on average.
Scenario 1 resulted in Agent 0 winning 15 times with 121 troops left on average, Agent 1 10 times with 187 troops left on average.
Each trial takes over 100 moves before completion. Some trials result in no combat, while most are only resolved with 1 combat. The reason is that attrition rate can reduce the enemy forces as well, resulting in lower incentive for the agents to risk battle with the enemy when it is possible to wait it out.
