"""
This file will contain logic for the supply system
"""

from data_structures import LinkedList

MAX_SUPPLY = 100
MIN_SUPPLY = 10 # Minimum before sending


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

class SupplyTracker:
    def __init__(self):
        self.list = LinkedList() 

    def add_packet(self, supply, source, destination):
        # Make a supply packet and add to the list
        new_packet = SupplyPacket(supply, source, destination)
        self.list.append(new_packet)

    def update_list(self):
        # Every tick, we update the travel time of each packet
        current = self.list.head
        while current:
            current.data.update_travel_time()
            if current.data.is_delivered():
                # If it is delivered, we resupply the destination
                self.list.remove(current.data)
                # Need to check destination stuff too but for now this is ok
            current = current.next
        

class SupplyHub:
    def __init__(self, location):
        self.location = location
        self.supply = 0
        self.generator = False

    def resupply(self):
        self.location.army += self.supply

    def consume(self):
        self.location.army -= self.supply
