"""
This file will contain logic for the map generation
"""
import random
from enum import Enum


class TerrainType(Enum):
    ROAD = 1
    FLATLAND = 2
    HIGHLAND = 3
    FORESTS = 4
    MOUNTAIN = 5
    WATER = 6

class LocationType(Enum):
    PASSABLE = 1
    SUPPLY_HUB = 2
    IMPASSABLE = 3

class Location:
    def __init__(self, terrain, location_type, coordinate):
        self.terrain = terrain
        self.coordinate = coordinate
        self.location_type = location_type
        self.army = 0
        self.path_cost = 2

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

class GameMap:
    def __init__(self, width: int, height: int, n_hubs: int, n_generators: int):
        # We use temporary constants for now to keep the same map
        # We can perform random generation later
        self.width = width
        self.height = height
        self.map = [[Location(TerrainType.FLATLAND, LocationType.PASSABLE, (x,y)) for x in range(width)] for y in range(height)]
        self.hubs = []

        # Set the terrain as well upon initialization
        self.set_terrains(n_hubs, n_generators)

    def set_terrains(self, n_hubs: int, n_generators: int):
        n_hubs_root = int(n_hubs ** 0.5)

        # Generate supply hubs
        for i in range(1, n_hubs_root+1):
            for j in range(1, n_hubs_root + 1):
                x = i * (self.width // (n_hubs_root+1))
                y = j * (self.height // (n_hubs_root+1))
                self.map[x][y].location_type = LocationType.SUPPLY_HUB  
                self.hubs += [self.map[x][y]]

        
        # Generate roads between hubs
        for i in range(1, n_hubs_root+1):
            x = i * (self.width // (n_hubs_root+1))
            for y in range(0, self.height):
                self.map[x][y].terrain = TerrainType.ROAD
        
        for i in range(1, n_hubs_root+1):
            y = i * (self.height // (n_hubs_root+1))
            for x in range(0, self.width):
                self.map[x][y].terrain = TerrainType.ROAD
        

        # Create a list of terrains excluding roads and assign weight
        exclude_road = [terrain for terrain in TerrainType if terrain != TerrainType.ROAD]
        weights = []
        for terrain in exclude_road:
            match terrain:
                case TerrainType.FLATLAND:
                    weights.append(4)
                case TerrainType.HIGHLAND:
                    weights.append(2)
                case TerrainType.FORESTS:
                    weights.append(2)
                case TerrainType.MOUNTAIN:
                    weights.append(1)
                case TerrainType.WATER:
                    weights.append(1)

        # Generate every other terrain types, this will be randomized 
        for row in self.map:
            for location in row:
                if location.location_type != LocationType.SUPPLY_HUB and location.terrain != TerrainType.ROAD:
                    random_terrain = random.choices(exclude_road, weights=weights, k=1)[0]
                    location.terrain = random_terrain

                    # Some percentage of mountains are impassable
                    if random_terrain == TerrainType.MOUNTAIN:
                        if random.random() <= 0.25:
                            location.location_type = LocationType.IMPASSABLE


    def display_map(self):
        for row in self.map:
            for location in row:
                if location.location_type == LocationType.SUPPLY_HUB:
                    print("H", end = " ")
                elif location.location_type == LocationType.IMPASSABLE:
                    print("@", end= " ")
                elif location.terrain == TerrainType.ROAD:
                    print("_", end = " ")
                # elif location.terrain == TerrainType.MOUNTAIN:
                #     print("&", end=" ")
                # elif location.terrain == TerrainType.FORESTS:
                #     print("!", end=" ")
                # elif location.terrain == TerrainType.HIGHLAND:
                #     print("^", end=" ")
                elif location.terrain == TerrainType.WATER:
                    print("~", end=" ")
                
                else:
                    print(".", end=" ")
                    
            print()
            
