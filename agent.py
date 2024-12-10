"""
This file contains code for the agents themselves and their decisions
"""
import supply as sp
import army
from game import Directions
START_ARMY_SZ = 20000

class Agent:
    def __init__(self, id):
        self.id = id #index of player
        self.supply_line = sp.SupplyGraph
        self.armies = [army.Army(START_ARMY_SZ)]
    def getAction (self,state)
    dist = self.getDistribution(state)
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution( dist )

