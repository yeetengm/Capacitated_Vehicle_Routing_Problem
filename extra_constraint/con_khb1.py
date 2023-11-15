
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data["distance_matrix"] = [
            [0.0, 1700, 150, 230, 700, 800, 700, 600, 500, 600, 650, 550, 600, 1000, 1400, 1500, 1200, 1500, 1600, 2000, 2100, 2700, 3000, 33, 900, 900, 2700],
            [1700, 0.0, 1500, 1400, 1100, 1100, 1200, 1100, 1200, 1100, 1000, 1100, 1100, 1100, 1500, 1600, 1300, 1600, 1700, 2200, 2300, 2900, 3200, 1700, 1000, 1000, 2800],
            [150, 1500, 0.0, 76, 550, 650, 550, 450, 350, 450, 500, 400, 450, 850, 1200, 1300, 1000, 1300, 1500, 1900, 2000, 2600, 2900, 180, 750, 750, 2500],
            [230, 1400, 76, 0.0, 500, 600, 500, 400, 250, 350, 450, 350, 350, 750, 1100, 1300, 950, 1200, 1400, 1800, 1900, 2500, 2800, 26, 650, 650, 2500],
            [700, 1100, 550, 500, 0.0, 140, 170, 110, 240, 150, 190, 150, 190, 600, 1000, 1100, 800, 1100, 1300, 1700, 1800, 2300, 2600, 750, 500, 500, 2300],
            [800, 1100, 650, 600, 140, 0.0, 300, 260, 350, 250, 220, 250, 290, 700, 1100, 1200, 850, 1200, 1400, 1800, 1800, 2400, 2700, 850, 600, 600, 2400],
            [700, 1200, 550, 500, 170, 300, 0.0, 110, 230, 150, 210, 150, 190, 600, 1000, 1100, 750, 1100, 1300, 1600, 1700, 2300, 2600, 750, 500, 500, 2300],
            [600, 1100, 450, 400, 110, 260, 110, 0.0, 130, 37, 100, 36, 78, 450, 850, 1000, 650, 1000, 1100, 1500, 1600, 2200, 2500, 650, 400, 400, 2200],
            [500, 1200, 350, 250, 240, 350, 230, 130, 0.0, 120, 180, 89, 100, 500, 900, 1000, 700, 1000, 1200, 1600, 1700, 2300, 2500, 500, 400, 400, 2200],
            [600, 1100, 450, 350, 150, 250, 150, 37, 120, 0.0, 91, 27, 69, 450, 850, 1000, 650, 950, 1100, 1500, 1600, 2200, 2500, 600, 350, 350, 2200],
            [650, 1000, 500, 450, 190, 220, 210, 100, 180, 91, 0.0, 90, 130, 550, 950, 1000, 700, 1000, 1200, 1600, 1700, 2300, 2600, 700, 450, 450, 2200],
            [550, 1100, 400, 350, 150, 250, 150, 36, 89, 27, 90, 0.0, 42, 450, 850, 1000, 650, 900, 1100, 1500, 1600, 2200, 2500, 600, 350, 350, 2200],
            [600, 1100, 450, 350, 190, 290, 190, 78, 100, 69, 130, 42, 0.0, 400, 800, 900, 600, 900, 1100, 1500, 1600, 2200, 2400, 600, 300, 300, 2100],
            [1000, 1100, 850, 750, 600, 700, 600, 450, 500, 450, 550, 450, 400, 0.0, 400, 500, 190, 500, 650, 1100, 1200, 1800, 2000, 1000, 130, 130, 1700],
            [1400, 1500, 1200, 1100, 1000, 1100, 1000, 850, 900, 850, 950, 850, 800, 400, 0.0, 500, 210, 450, 650, 1100, 1200, 1700, 2000, 1400, 550, 550, 1700],
            [1500, 1600, 1300, 1300, 1100, 1200, 1100, 1000, 1000, 1000, 1000, 1000, 900, 500, 500, 0.0, 290, 300, 500, 900, 1000, 1600, 1800, 1500, 1000, 1000, 1600],
            [1200, 1300, 1000, 950, 800, 850, 750, 650, 700, 650, 700, 650, 600, 190, 210, 290, 0.0, 300, 500, 950, 1100, 1700, 1900, 1200, 650, 650, 1900],
            [1500, 1600, 1300, 1200, 1100, 1200, 1100, 1000, 1000, 950, 1000, 900, 900, 500, 450, 300, 300, 0.0, 200, 700, 800, 1300, 1500, 1500, 1100, 1100, 1500],
            [1600, 1700, 1500, 1400, 1300, 1400, 1300, 1100, 1200, 1100, 1200, 1100, 1100, 650, 650, 500, 500, 200, 0.0, 500, 600, 1100, 1300, 1600, 1200, 1200, 1600],
            [2000, 2200, 1900, 1800, 1700, 1800, 1600, 1500, 1600, 1500, 1600, 1500, 1500, 1100, 1100, 900, 950, 700, 500, 0.0, 100, 600, 800, 2000, 1400, 1400, 2000],
            [2100, 2300, 2000, 1900, 1800, 1800, 1700, 1600, 1700, 1600, 1700, 1600, 1600, 1200, 1200, 1000, 1100, 800, 600, 100, 0.0, 500, 700, 2100, 1500, 1500, 2100],
            [2700, 2900, 2600, 2500, 2300, 2400, 2300, 2200, 2300, 2200, 2300, 2200, 2200, 1800, 1700, 1600, 1700, 1300, 1100, 600, 500, 0.0, 300, 2700, 2200, 2200, 2700],
            [3000, 3200, 2900, 2800, 2600, 2700, 2600, 2500, 2500, 2500, 2600, 2500, 2400, 2000, 2000, 1800, 1900, 1500, 1300, 800, 700, 300, 0.0, 3000, 2400, 2400, 3000],
            [33, 1700, 180, 26, 750, 850, 750, 650, 500, 600, 700, 600, 600, 1000, 1400, 1500, 1200, 1500, 1600, 2000, 2100, 2700, 3000, 0.0, 900, 900, 2700],
            [900, 1000, 750, 650, 500, 600, 500, 400, 400, 350, 450, 350, 300, 130, 550, 1000, 650, 1100, 1200, 1000, 1100, 1400, 1600, 900, 0.0, 0.0, 1700],
            [900, 1000, 750, 650, 500, 600, 500, 400, 400, 350, 450, 350, 300, 130, 550, 1000, 650, 1100, 1200, 1000, 1100, 1400, 1600, 900, 0.0, 0.0, 1700],
            [2700, 2800, 2500, 2500, 2300, 2400, 2300, 2200, 2200, 2200, 2300, 2200, 2100, 1700, 1700, 1500, 650, 1500, 1600, 2000, 2100, 2700, 3000, 2700, 1700, 1700, 0.0]
    ]

    data["demands"] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8, 4, 4, 5, 8, 3, 5, 3, 6, 7, 8]
    data["vehicle_capacities"] = [20, 20 , 20, 20, 20, 20]
    data["num_vehicles"] = 6
    data["depot"] = 0
    return data



def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f"Objective: {solution.ObjectiveValue()}")
    total_distance = 0
    total_load = 0
    max_route_distance = 0
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        plan_output = f"Route for vehicle {vehicle_id}:\n"
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data["demands"][node_index]
            plan_output += f" {node_index} Load({route_load}) -> "
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id
            )
        plan_output += f" {manager.IndexToNode(index)} Load({route_load})\n"
        plan_output += f"Distance of the route: {route_distance}m\n"
        plan_output += f"Load of the route: {route_load}\n"
        print(plan_output)
        total_distance += route_distance
        total_load += route_load
        max_route_distance = max(route_distance, max_route_distance)
    print(f"Total distance of all routes: {total_distance}m")
    print(f"Total load of all routes: {total_load}")
    print(f"Maximum of the route distances: {max_route_distance}m")



def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


 # Add Distance constraint.
    dimension_name = "Distance"
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        6000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name,
    )
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)


     # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data["demands"][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data["vehicle_capacities"],  # vehicle maximum capacities
        True,  # start cumul to zero
        "Capacity",
    )
    # [END capacity_constraint]

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.FromSeconds(1)


    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)
    else:
        print("No solution found !")


if __name__ == "__main__":
    main()