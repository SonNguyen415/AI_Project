"""
This file will contain logic for the supply system
"""

class SupplyHub:
    def __init__(self, location):
        self.location = location
        self.supply = 0
        self.generator = False

    def resupply(self):
        self.location.army += self.supply

    def consume(self):
        self.location.army -= self.supply
