# AI_Project

This is the AI Algorithms project. The goal is to develop a strategy game AI to defeat an enemy with uncertain combat outcomes. Every army must move during the game, and all movements result in some attrition rate to the army, proportional to the army sizes and dependent on the terrain. The win condition is to reduce the enemy's total number of armies to 0. The game takes place on a randomized map with randomized terrain. 

### To Run ###
To run:
```bash
python main.py
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
