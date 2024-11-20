from enum import Enum


MAX_SUPPLY = 1000
MIN_SUPPLY = 10 # Minimum before sending
GENERATOR_SPEED = 10

class TerrainType(Enum):
    ROAD = 1
    FLATLAND = 2
    HIGHLAND = 3
    FORESTS = 4
    MOUNTAIN = 5
    WATER = 6

class LocationType(Enum):
    PASSABLE = 1
    IMPASSABLE = 2
    SUPPLY_HUB = 3
    SUPPLY_GENERATOR = 4
    

class Location:
    def __init__(self, terrain, location_type, coordinates):
        self.terrain = terrain
        self.location_type = location_type
        self.coordinates = coordinates
        self.army = 0
        self.supply = None
        self.path_cost = 2
        self.supply_path = False
        self.controller = 0

    def calculate_path_cost(self):
        match self.terrain:
            case TerrainType.ROAD:
                return 1
            case TerrainType.FLATLAND:
                return 2
            case TerrainType.HIGHLAND:
                return 3
            case TerrainType.FORESTS:
                return 4
            case TerrainType.MOUNTAIN:
                return 4
            case TerrainType.WATER:
                return 5

class SupplyHub:
    def __init__(self, location):
        self.location = location
        self.supply = 0
        self.generator = False

    def resupply(self):
        self.location.army += self.supply

    def consume(self):
        self.location.army -= self.supply

    def generate_supply(self):
        if self.generator:
            self.supply += GENERATOR_SPEED