"""
This file contains code for the agents themselves and their decisions
"""
import supply as sp
import army

START_ARMY_SZ = 20000

class Agent:
    def __init__(self, id):
        self.id = id
        self.supply_line = sp.SupplyGraph
        self.armies = [army.Army(START_ARMY_SZ)]