import army, map, random


class Manager:
    def __init__(self, map: map.GameMap, armies1: list, armies2: list):
        self.map = map
        self.armies1 = armies1
        self.armies2 = armies2

    def combat(self):
        for army1 in self.armies1:
            for army2 in self.armies2:
                if army1.position == army2.position:
                    if army1.supply > army2.supply:
                        self.armies2.remove(army2)
                    elif army1.supply < army2.supply:   
                        self.armies1.remove(army1)

    
    def resupply(self):
        for army1 in self.armies1:
            for supply_loc in self.map.supply:
                if army1.position == supply_loc.coordinates:
                    army1.consume_cache(supply_loc.supply)
                    supply_loc.delete_cache()
                    
        for army2 in self.armies2:
            for supply_loc in self.map.supply:
                if army2.position == supply_loc.coordinates:
                    army2.consume_cache(supply_loc.supply)
                    supply_loc.delete_cache()
        

    def is_goal(self):
        return len(self.armies1) == 0 or len(self.armies2) == 0
        