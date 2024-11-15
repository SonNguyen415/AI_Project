# AI_Project

This is the AI Algorithms project. The goal is to develop a strategy game AI to play in an unknown map with unknown opposition. This AI must take into account a supply system and defend its own while taking out the other side's supply system

## Development Rules ##
1. Develop features in a branch, and make commits as small as possible. Pull requests into the main branch needs to be approved by at least on other team member.

2. Follow standard python naming conventions. Snake cases for variable and function names. Camel case for class names.

## Components ##
`main.py` runs the game across various scenarios for evaluation purposes.
`game.py` takes in a scenario as an input, and generate a game and run it.
`map.py` takes in some arguments and generates a 2D grid map to represent the game map.
`army.py` controls the movements of armies and all related mechanics.
`supply.py` controls the movement of supplies from generator to hubs and calculate supply lines.

## Dependencies ##
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

## To Run ##
To run, use either:
```bash
python main.py
```
```bash
python3 main.py
```