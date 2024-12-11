from enum import Enum


MAX_SUPPLY = 1000
MIN_SUPPLY = 10 # Minimum before sending
GENERATOR_SPEED = 10

class TerrainType(Enum):
    WATER = 1
    FLATLAND = 2
    HIGHLAND = 3
    FORESTS = 4
    MOUNTAIN = 5

class LocationType(Enum):
    PASSABLE = 1
    IMPASSABLE = 2
    SUPPLY_CACHE = 3

class Location:
    def __init__(self, terrain, location_type, coordinates):
        self.terrain = terrain
        self.location_type = location_type
        self.coordinates = coordinates
        
        self.agent = 0
        self.supply = self.cache_value()
        self.visited = False
        self.path_cost = self.set_path_cost()
        self.supply_path = False
        self.controller = 0

    def cache_value(self):
        if self.location_type == LocationType.SUPPLY_CACHE:
            if self.visited == False:
                return 100
            else:
                return 0
        return 0

    def set_path_cost(self):
        match self.terrain:
            case TerrainType.FLATLAND:
                self.path_cost = 1
            case TerrainType.HIGHLAND:
                self.path_cost = 2
            case TerrainType.FORESTS:
                self.path_cost = 3
            case TerrainType.MOUNTAIN:
                self.path_cost = 4
            case TerrainType.WATER:
                self.path_cost = 5
