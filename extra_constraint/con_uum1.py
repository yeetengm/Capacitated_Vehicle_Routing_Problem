
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data["distance_matrix"] = [
        # fmt: off
      [0, 5700, 7200, 8400, 7300, 4800, 4600, 6600, 5400, 5600, 6300, 6800, 5400, 6800, 6800, 5700, 8600, 6200, 6900, 7400, 5500, 4000, 5400, 9800],
      [7200, 1800, 0, 2600, 7100, 4600, 4400, 2200, 3400, 3500, 2800, 2300, 3400, 2500, 2600, 3700, 2200, 2700, 2600, 2900, 2600, 3900, 3300, 3400],
      [8400, 3800, 2600, 0, 7600, 5000, 4800, 2400, 3400, 3500, 2700, 2300, 3400, 4300, 2600, 3700, 1100, 2600, 2700, 3100, 3300, 5700, 3300, 5200],
      [7300, 5400, 7100, 7600, 0, 3100, 2900, 5800, 4600, 4700, 5400, 5700, 4600, 6000, 6000, 4900, 7900, 5400, 6100, 6500, 4700, 4900, 4500, 9100],
      [4800, 2900, 4600, 5000, 3100, 0, 500, 3300, 2100, 2200, 2900, 3200, 2100, 3500, 3500, 2400, 5400, 2900, 3600, 4000, 2200, 2400, 2000, 6600],
      [4600, 2700, 4400, 4800, 2900, 500, 0, 3100, 1900, 2000, 2700, 3000, 1900, 3300, 3300, 2200, 5200, 2700, 3400, 3800, 2000, 2200, 1800, 6400],
      [6600, 3800, 2200, 2400, 5800, 3300, 3100, 0, 1600, 1800, 900, 1100, 1700, 300, 350, 2000, 2700, 850, 400, 900, 1500, 4400, 1600, 5000],
      [5400, 1400, 3400, 3400, 4600, 2100, 1900, 1600, 0, 160, 2300, 2600, 42, 2800, 2900, 350, 4800, 2200, 2900, 3400, 1500, 3300, 1400, 7100],
      [5600, 1600, 3500, 3500, 4700, 2200, 2000, 1800, 160, 0, 2200, 2400, 1300, 2700, 2700, 190, 4700, 2100, 2800, 3300, 1400, 3200, 1300, 6900],
      [6300, 4000, 2800, 2700, 5400, 2900, 2700, 900, 2300, 2200, 0, 500, 1600, 750, 800, 2000, 2700, 850, 850, 1300, 1500, 5500, 1600, 5000],
      [6800, 3700, 2300, 2300, 5700, 3200, 3000, 1100, 2600, 2400, 500, 0, 1500, 260, 300, 1900, 2600, 750, 350, 850, 1400, 4300, 1500, 4900],
      [5400, 1400, 3400, 3400, 4600, 2100, 1900, 1700, 42, 1300, 1600, 1500, 0, 2800, 2900, 300, 4800, 2200, 2900, 3400, 1500, 3300, 1400, 7000],
      [6800, 4000, 2500, 4300, 6000, 3500, 3300, 300, 2800, 2700, 750, 260, 2800, 0, 190, 2000, 2900, 100, 96, 700, 1600, 4600, 1600, 5200],
      [6800, 4000, 2600, 2600, 6000, 3500, 3300, 350, 2900, 2700, 800, 300, 2900, 190, 0, 1800, 2900, 100, 290, 500, 1400, 4600, 1400, 5200],
      [5700, 1800, 3700, 3700, 4900, 2400, 2200, 2000, 350, 190, 2000, 1900, 300, 2000, 1800, 0, 4500, 1900, 2600, 3100, 1200, 3000, 1100, 6800],
      [8600, 3500, 2200, 1100, 7900, 5400, 5200, 2700, 4800, 4700, 2700, 2600, 4800, 2900, 2900, 4500, 0, 3000, 2900, 3400, 3600, 5200, 3700, 4700],
      [6200, 3900, 2700, 2600, 5400, 2900, 2700, 850, 2200, 2100, 850, 750, 2200, 100, 290, 2600, 3000, 0, 1100, 1600, 1100, 4000, 1100, 5200],
      [6900, 4100, 2600, 2700, 6100, 3600, 3400, 400, 2900, 2800, 850, 350, 2900, 96, 290, 2600, 2900, 1100, 0, 800, 1700, 4700, 1700, 5300],
      [7400, 4500, 2900, 3100, 6500, 4000, 3800, 900, 3400, 3300, 1300, 850, 3400, 700, 500, 3100, 3400, 1600, 800, 0, 1000, 4000, 1100, 5300],
      [5500, 1000, 2600, 3300, 4700, 2200, 2000, 1500, 1500, 1400, 1500, 1400, 1500, 1600, 1400, 1200, 3600, 1100, 1700, 1000, 260, 3400, 260, 4900],
      [4000, 4000, 3900, 5700, 4900, 2400, 2200, 4400, 3300, 3200, 5500, 4300, 3300, 4600, 4600, 3000, 5200, 4000, 4700, 4000, 3400, 0, 3000, 6400],
      [5400, 1300, 3300, 3300, 4500, 2000, 1800, 1600, 1400, 1300, 1600, 1500, 1400, 1600, 1400, 1100, 3700, 1100, 1700, 1100, 260, 3000, 0, 5200],
      [9800, 4000, 3400, 5200, 9100, 6600, 6400, 5000, 7100, 6900, 5000, 4900, 7000, 5200, 5200, 6800, 4700, 5200, 5300, 5300, 4900, 6400, 5200, 0],
        # fmt: on
    ]
    data["demands"] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8, 4, 4, 5, 8, 3, 5, 3]
    data["vehicle_capacities"] = [20, 20 , 20, 20, 20]
    data["num_vehicles"] = 5
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
        14000,  # vehicle maximum travel distance
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