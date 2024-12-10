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
        self.supply = []

    def generate_map_info(self, n_supply: int):
        """
        Generate the map information. This will include the supply hubs, supply generators, and the terrain types

        :param n_supply: The number of supply caches
        :param supply_tracker: The supply tracker object to keep track of the supply hubs and edges
        """
        # Create supply generators and set the terrain of every other locations
        self.generate_supply(n_supply)
        self.set_terrains()

    #supplies scattered around the map. By default, there will be width+1 supplies scattered randomly
    
    def generate_supply(self, n_supply: int):
        # Generate supply caches (needs to be redone)
        chosen_positions = set()
        while len(chosen_positions) < n_supply:
            # step 1: pick random coordinate
            rand_x = random.randint(0, self.width - 1)
            rand_y = random.randint(0, self.height - 1)

            #step 2: make sure it's passable terrain
            location = self.map[rand_y][rand_x]
            if location.location_type != loc.LocationType.PASSABLE or location in chosen_positions:
                continue

            #step 3: mark location as supply cach
            location.location_type = loc.LocationType.SUPPLY_CACHE
            chosen_positions.add((rand_y, rand_x))
            
            #step 4: store in supply list
            self.supply.append(location)


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
            
