"""
This file will contain logic for the map generation
"""
import random
import supply as sp
import locations as loc

class GameMap:
    def __init__(self, width: int, height: int):
        # We use temporary constants for now to keep the same map
        # We can perform random generation later
        self.width = width
        self.height = height
        self.map = [[loc.Location(loc.TerrainType.FLATLAND, loc.LocationType.PASSABLE, (y, x)) for x in range(width)] for y in range(height)]
        self.hubs = []

    def generate_map_info(self, n_hubs: int, n_generators: int, supply_tracker: sp.SupplyTracker):
        n_hubs_root = int(n_hubs ** 0.5)

        # Generate supply hubs
        for i in range(1, n_hubs_root+1):
            for j in range(1, n_hubs_root + 1):
                x = i * (self.width // (n_hubs_root+1))
                y = j * (self.height // (n_hubs_root+1))
                self.map[y][x].location_type = loc.LocationType.SUPPLY_HUB  
                self.hubs.append(self.map[y][x])

                # Add the hub to the supply tracker
                hub = loc.SupplyHub(self.map[y][x])
                supply_tracker.add_hub(hub)

        self.generate_roads(n_hubs_root, supply_tracker, "vertical")
        self.generate_roads(n_hubs_root, supply_tracker, "horizontal")

        
        # Create supply generators and set the terrain of every other locations
        self.create_generators(n_generators)
        self.set_terrains()


    def generate_roads(self, n_hubs_root: int, supply_tracker: sp.SupplyTracker, direction: str):
        for i in range(1, n_hubs_root + 1):
            # Determine fixed axis and range for traversal
            if direction == "vertical":
                fixed_axis = i * (self.width // (n_hubs_root + 1)) 
                range_axis = self.height
            else:
                fixed_axis = i * (self.height // (n_hubs_root + 1))
                range_axis = self.width

            source = None
            destination = None
            edge_cost = 0

            # Traverse along the appropriate axis
            for variable_axis in range(range_axis):
                if direction == "vertical":
                    x, y = (fixed_axis, variable_axis)
                else:
                    x, y = (variable_axis, fixed_axis)
                current_cell = self.map[y][x]

                if current_cell.location_type == loc.LocationType.SUPPLY_HUB:
                    edge_cost += current_cell.path_cost
                    if source is None:
                        source = current_cell
                    else:
                        destination = current_cell
                        # Add the edge to the supply tracker
                        supply_tracker.add_edges(source, destination, edge_cost)
                        supply_tracker.add_edges(destination, source, edge_cost)

                        # Reset values
                        edge_cost = current_cell.path_cost
                        source = destination
                        destination = None
                else:
                    # Set the road, update edge cost, and mark as supply path
                    current_cell.terrain = loc.TerrainType.ROAD
                    edge_cost += current_cell.path_cost
                    current_cell.supply_path = True

    def create_generators(self, n_generators: int): 
        # Generate supply generators, direction is either north-south or west-east
        direction = random.choice([0,1])
        direction = 1
        n_agents = 2

        height_pos = [0, self.height-1]
        width_pos = [0, self.width-1]
        for i in range(0, n_agents):
            # Fix the x or y coordinate based on direction (north-south or west-east)
            if direction == 0:
                y = random.choice(height_pos)
                height_pos.remove(y)
            else:
                x = random.choice(width_pos)
                width_pos.remove(x)
            
            for j in range(n_generators):
                if direction == 0:
                    x = random.randint(0, self.width-1)
                else:
                    y = random.randint(self.height*i//n_agents, self.height*(i+1)//n_agents-1)
                self.map[y][x].location_type = loc.LocationType.SUPPLY_GENERATOR
                self.map[y][x].controller = i+1

    def set_terrains(self):
        # Create a list of terrains excluding roads and assign weight
        exclude_road = [terrain for terrain in loc.TerrainType if terrain != loc.TerrainType.ROAD]
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
                if location.location_type != loc.LocationType.SUPPLY_HUB and location.terrain != loc.TerrainType.ROAD:
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
        for row in self.map:
            for location in row:
       
                if location.location_type == loc.LocationType.SUPPLY_HUB:
                    print("H", end = " ")
                elif location.location_type == loc.LocationType.SUPPLY_GENERATOR:
                    if location.controller == 1:
                        print("G", end = " ")
                    else:
                        print("E", end = " ")
                # elif location.location_type == loc.LocationType.IMPASSABLE:
                #     print("@", end= " ")
                elif location.terrain == loc.TerrainType.ROAD:
                    print("-", end = " ")
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
            
