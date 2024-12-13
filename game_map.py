"""
This file will contain logic for the map generation
"""
import random
import locations as loc

class GameMap:
    def __init__(self, width: int, height: int):
        # We use temporary constants for now to keep the same map
        # We can perform random generation later
        self.width = width
        self.height = height
        self.map = [[loc.Location(loc.TerrainType.FLATLAND, loc.LocationType.PASSABLE, (y, x)) for x in range(width)] for y in range(height)]
        self.set_terrains()

    def set_terrains(self):
        """
        Set the terrains of the locations. This will be used to determine the path cost of moving through the location.
        """

        # Create a list of terrains excluding roads and assign weight
        exclude_road = [terrain for terrain in loc.TerrainType]
        weights = []
        for terrain in exclude_road:
            match terrain:
                case loc.TerrainType.FLATLAND:
                    weights.append(4)
                case loc.TerrainType.HIGHLAND:
                    weights.append(2)
                case loc.TerrainType.FORESTS:
                    weights.append(2)
                case loc.TerrainType.MOUNTAIN:
                    weights.append(1)
                case loc.TerrainType.WATER:
                    weights.append(1)

        # Generate every other terrain types, this will be randomized 
        for row in self.map:
            for location in row:
                if location.location_type != loc.LocationType.SUPPLY_CACHE:
                    random_terrain = random.choices(exclude_road, weights=weights, k=1)[0]
                    location.terrain = random_terrain

                    # Let's make 25% of mountains be impassable
                    if random_terrain == loc.TerrainType.MOUNTAIN:
                        if random.random() <= 0.25:
                            location.location_type = loc.LocationType.IMPASSABLE


    def get_path_cost(self, old_pos: int, new_pos: int):
        """
        Get the path cost of a location
        """
        total_cost = self.map[old_pos[0]][old_pos[1]].path_cost + self.map[new_pos[0]][new_pos[1]].path_cost
        return total_cost
    
    def display_map_coordinates(self):
        """
        This function will print the game map as a grid of coordinates
        Do not use this function for large maps.
        """
        for row in self.map:
            for location in row:
                print(location.coordinates, end = " ")
            print()


    def display_map(self):
        """
        This function will print the game map as a grid of characters.
        Not useful for very large maps.
        """
        for row in self.map:
            for location in row:
       
                if location.location_type == loc.LocationType.SUPPLY_CACHE:
                    print("C", end = " ")
                # elif location.location_type == loc.LocationType.IMPASSABLE:
                #     print("@", end= " ")
                # elif location.terrain == loc.TerrainType.MOUNTAIN:
                #     print("&", end=" ")
                # elif location.terrain == loc.TerrainType.FORESTS:
                #     print("!", end=" ")
                # elif location.terrain == loc.TerrainType.HIGHLAND:
                #     print("^", end=" ")
                # elif location.terrain == loc.TerrainType.WATER:
                #     print("~", end=" ")
                else:
                    print(".", end=" ")
                    
            print()
            
