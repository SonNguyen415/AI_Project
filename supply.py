"""
This file will contain logic for the supply system
"""

import collections 
import map
import locations as loc

class SupplyPacket:
    def __init__(self, supply, source, destination):
        self.supply = supply
        self.source = source
        self.destination = destination
        self.travel_time = self.calculate_travel_time()

    def update_travel_time(self):
        self.travel_time -= 1

    def is_delivered(self):
        return self.travel_time == 0
    
    def calculate_travel_time(self):
        return 0


class SupplyGraph:
    """
    This class contains the agent's specific supply graph. The graph portraying the hubs and supply lines as it is per tick
    """
    def __init__(self):
        self.graph = dict()



class SupplyTracker:
    """
    This class will contain the graph of all the supply hubs for both sides.
    """
    def __init__(self):
        self.supply_list = collections.deque() 
        self.graph = dict()

    def add_packet(self, supply: int, source: tuple, destination: tuple):
        """
        Create a new packet and add it to the supply list, a list of packets in transit.

        :param supply: The amount of supply in the packet
        :param source: The source of the packet as a tuple (x, y)
        :param destination: The destination of the packet as a tuple (x, y)
        """
        new_packet = SupplyPacket(supply, source, destination)
        self.supply_list.append(new_packet)

    def update_list(self):
        """
        Update the supply list. This will update the travel time of each packet and remove packets that have been delivered.
        """
        current = self.supply_list.head
        while current:
            # Every tick, we update the travel time of each packet
            current.data.update_travel_time()
            if current.data.is_delivered():
                # If it is delivered, we resupply the destination
                self.list.remove(current.data)
                # Need to check destination stuff too but for now this is ok
            current = current.next
        
    def add_hub(self, hub: loc.SupplyHub):
        """
        Add a hub to the supply tracker's graph of all hubs in the game.

        :param hub: a supply hub object
        """
        # The graph is a dictionary with the key being the coordinates of the hub (since the hub objects can't be passed around in python)
        # The value contains the hub itself and a list of destination nodes that the hub is connected to
        self.graph[hub.location.coordinates] = {
            "source": hub,
            "sink": []
        }

    def add_edges(self, src: loc.Location, dest: loc.Location, cost: int):
        """
        Add an edge to the graph. This is a connection between two hubs.

        :param src: The source hub
        :param dest: The destination hub
        :param cost: The total cost of traversing the edge (the road path between the two hubs)
        
        """
        srcCoord = src.coordinates
        sink = loc.SupplyHub(dest)
        self.graph[srcCoord]["sink"].append((sink, cost))
    

    def visualize_graph(self):
        """
        Print out the graph in a readable format
        """
        for source in self.graph:
            print(source, "-->", end= "")
            for dest in self.graph[source]["sink"]:
                print(dest[0].location.coordinates, end = "")
            print()
            
           