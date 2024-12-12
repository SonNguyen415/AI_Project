import army

START_ARMY_SZ = 20000
N_ARMIES = 1
    

class State: 
    def __init__(self, agents):
        # Current armies
        self.armies = dict()
        for agent in agents:
            self.armies[agent] = [START_ARMY_SZ] * N_ARMIES

    def get_successor(self, agent, action):
        """
        Given an agent and an action, return the successor state
        """
        pass
    
    def combat(self, agents: list):
        agent0 = agents[0]
        agent1 = agents[1]
        for army0 in self.armies[agents[0]]:
            for army1 in self.armies[agents]:
                if army0.position == army1.position:
                
                    # Placeholder: Warren changes
                    if army0.supply > army1.supply:
                        self.armies[agent1].remove(army1)
                    elif army0.supply < army1.supply:   
                        self.armies[agent0].remove(army0)

    
    def resupply(self):
        for army1 in self.armies1:
            # Update to make a list of caches so we don't have to iterate through the entire map
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