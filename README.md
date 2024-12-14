# AI_Project

This is the AI Algorithms project. The goal is to develop a strategy game AI to play in an unknown map with unknown opposition. This AI must take into account a supply system and defend its own while taking out the other side's supply system
### To Run ###
To run:
To run third scenario, go into main.py and set third to true
```bash
python main.py
```

### Expected Results ###
Agent 1 is a constant, iterating 10 times.

Agent 0 iterates either 20, 100, or 1000 times based on the scenario


For scenario 1, we expect a winrate of Agent 0 and 1 of 50-50. 

For scenario 2, we expect that Agent 0 will do slightly better- closer to 70-30. 


### Development Rules ###
1. Develop features in a branch, and make commits as small as possible. Pull requests into the main branch needs to be approved by at least on other team member.

2. Follow standard python naming conventions. Snake cases for variable and function names. Camel case for class names. See the google convention for more details.

3. Before you make any changes. Pull from `main`. Use `git pull origin --rebase` for this. Then make a separate branch for the feature you're working on.

4. All commits should be as MINIMAL as possible. It's fine if the commit is very small. 

5. Create a PR for that branch and delete the branch right after. We will not have branches for big module implementation. But branches for every features. This is done because many parts of the project is interdependent with each other at very small steps.

### Components ###
- `main.py` runs the game across various scenarios for evaluation purposes.
- `game.py` takes in a scenario as an input, and generate a game and run it.
- `game_map.py` takes in some arguments and generates a 2D grid map to represent the game map.
- `army.py` controls the movements of armies and all related mechanics.
- `locations.py` contains the classes that specific the coordinates information. This information needs to be known by many other modules.
- `agent.py` controls each agent, of which there are 2 instances of in this map

### Dependencies ###
For any new dependencies that might be needed. Make sure to use the virutal environment. To create a virtual environment:

```bash
python3 -m venv myenv
```

To activate the virtual environment:
```bash
source myenv/bin/activate
```

To install required dependencies:
```bash
pip install -r requirements.txt
```

If during development process, you need to install new dependencies, use pip to install them. Then at the end of the process:
```bash
pip freeze > requirements.txt
```
This will update the requirements.txt file. You then can commit this file.

