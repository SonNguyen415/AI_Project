# AI_Project

This is the AI Algorithms project. The goal is to develop a strategy game AI to play in an unknown map with unknown opposition. This AI must take into account a supply system and defend its own while taking out the other side's supply system

### To Run ###
To run:
```bash
python main.py
```
To run third scenario, go into main.py and set THIRD to true
To see the map on each step, set VERBOSE to true in main.py

### Expected Results ###
Agent 1 is a constant, iterating 10 times.

Agent 0 iterates either 20, 100, or 1000 times based on the scenario


For scenario 1, we expect a winrate of Agent 0 and 1 of 50-50. 

For scenario 2, we expect that Agent 0 will do slightly better- closer to 60-40. 

For scenario 3, we expect closer to 70-30

