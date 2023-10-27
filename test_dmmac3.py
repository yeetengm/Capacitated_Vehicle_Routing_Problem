# [START import]
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
# [END import]


# [START data_model]
def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data["distance_matrix"] = [
        # fmt: off
      [0, 5.7, 7.2, 8.4, 7.3, 4.8, 4.6, 6.6, 5.4, 5.6, 6.3, 6.8, 5.4, 6.8, 6.8 ,5.7, 8.6, 6.2, 6.9, 7.4, 5.5, 4, 5.4, 9.8],
      [7.2, 1.8, 0, 2.6, 7.1, 4.6, 4.4, 2.2, 3.4, 3.5, 2.8, 2.3, 3.4, 2.5, 2.6, 3.7, 2.2, 2.7, 2.6, 2.9, 2.6, 3.9, 3.3, 3.4],
      [8.4, 3.8, 2.6, 0, 7.6, 5, 4.8, 2.4, 3.4, 3.5, 2.7, 2.3, 3.4, 4.3, 2.6, 3.7, 1.1, 2.6, 2.7, 3.1, 3.3, 5.7, 3.3, 5.2],
      [7.3, 5.4, 7.1, 7.6, 0, 3.1, 2.9, 5.8, 4.6, 4.7, 5.4, 5.7, 4.6, 6, 6, 4.9, 7.9, 5.4, 6.1, 6.5, 4.7, 4.9, 4.5, 9.1],
      [4.8, 2.9, 4.6, 5, 3.1, 0, 0.5, 3.3, 2.1, 2.2, 2.9, 3.2, 2.1, 3.5, 3.5, 2.4, 5.4, 2.9, 3.6, 4, 2.2, 2.4, 2, 6.6],
      [4.6, 2.7, 4.4, 4.8, 2.9, 0.5, 0, 3.1, 1.9, 2, 2.7, 3, 1.9, 3.3, 3.3, 2.2, 5.2, 2.7, 3.4, 3.8, 2, 2.2, 1.8, 6.4],
      [6.6, 3.8, 2.2, 2.4, 5.8, 3.3, 3.1, 0, 1.6, 1.8, 0.9, 0.11, 1.7, 0.3, 0.35, 2, 2.7, 0.85, 0.4, 0.9, 1.5, 4.4, 1.6, 5],
      [5.4, 1.4, 3.4, 3.4, 4.6, 2.1, 1.9, 1.6, 0, 0.16, 2.3, 2.6, 0.042, 2.8, 2.9, 0.35, 4.8, 2.2, 2.9, 3.4, 1.5, 3.3, 1.4, 7.1],
      [5.6, 1.6, 3.5, 3.5, 4.7, 2.2, 2, 1.8, 0.16, 0, 2.2, 2.4, 1.3, 2.7, 2.7, 0.19, 4.7, 2.1, 2.8, 3.3 ,1.4, 3.2, 1.3, 6.9],
      [6.3, 4, 2.8, 2.7, 5.4, 2.9, 2.7, 0.9, 2.3, 2.2, 0, 0.5, 1.6, 0.75, 0.8, 2, 2.7, 0.85, 0.85, 1.3, 1.5, 5.5, 1.6, 5],
      [6.8, 3.7, 2.3, 2.3, 5.7, 3.2, 3, 0.11, 2.6, 2.4, 0.5, 0, 1.5, 0.26, 0.3, 1.9, 2.6, 0.75, 0.35, 0.85, 1.4, 4.3, 1.5, 4.9],
      [5.4, 1.4, 3.4, 3.4, 4.6, 2.1, 1.9, 1.7, 0.042, 1.3, 1.6, 1.5, 0, 2.8, 2.9, 0.3, 4.8, 2.2, 2.9, 3.4, 1.5, 3.3, 1.4, 7],
      [6.8, 4, 2.5, 4.3, 6, 3.5, 3.3, 0.3, 2.8, 2.7, 0.75, 0.26, 2.8, 0, 0.19, 2, 2.9, 1, 0.096, 0.7, 1.6, 4.6, 1.6, 5.2],
      [6.8, 4, 2.6, 2.6, 6, 3.5, 3.3, 0.35, 2.9, 2.7, 0.8, 0.3, 2.9, 0.19, 0, 1.8, 2.9, 1, 0.29, 0.5, 1.4, 4.6, 1.4, 5.2],
      [5.7, 1.8, 3.7, 3.7, 4.9, 2.4, 2.2, 2, 0.35, 0.19, 2, 1.9, 0.3, 2, 1.8, 0, 4.5, 1.9, 2.6, 3.1, 1.2, 3, 1.1, 6.8],
      [8.6, 3.5, 2.2, 1.1, 7.9, 5.4, 5.2, 2.7, 4.8, 4.7, 2.7, 2.6, 4.8, 2.9, 2.9, 4.5, 0, 3, 2.9, 3.4, 3.6, 5.2, 3.7, 4.7],
      [6.2, 3.9, 2.7, 2.6, 5.4, 2.9, 2.7, 0.85, 2.2, 2.1, 0.85, 0.75, 2.2, 1, 1, 1.9, 3, 0, 1.1, 1.6, 1.1, 4, 1.1, 5.2],
      [6.9, 4.1, 2.6, 2.7, 6.1, 3.6, 3.4, 0.4, 2.9, 2.8, 0.85, 0.35, 2.9, 0.096, 0.29, 2.6, 2.9, 1.1, 0, 0.8, 1.7, 4.7, 1.7, 5.3],
      [7.4, 4.5, 2.9, 3.1, 6.5, 4, 3.8, 0.9, 3.4, 3.3, 1.3, 0.85, 3.4, 0.7, 0.5, 3.1, 3.4, 1.6, 0.8, 0, 1, 4, 1.1, 5.3],
      [5.5, 1, 2.6, 3.3, 4.7, 2.2, 2, 1.5, 1.5, 1.4, 1.5, 1.4, 1.5, 1.6, 1.4, 1.2, 3.6, 1.1, 1.7, 1, 0, 3.4, 0.26, 4.9],
      [4, 4, 3.9, 5.7, 4.9, 2.4, 2.2, 4.4, 3.3, 3.2, 5.5, 4.3, 3.3, 4.6, 4.6, 3, 5.2, 4, 4.7, 4, 3.4, 0, 3, 6.4],
      [5.4, 1.3, 3.3, 3.3, 4.5, 2, 1.8, 1.6, 1.4, 1.3, 1.6, 1.5, 1.4, 1.6, 1.4, 1.1, 3.7, 1.1, 1.7, 1.1, 0.26, 3, 0, 5.2],
      [9.8, 4, 3.4, 5.2, 9.1, 6.6, 6.4, 5, 7.1, 6.9, 5, 4.9, 7, 5.2, 5.2, 6.8, 4.7, 5.2, 5.3, 5.3, 4.9, 6.4, 5.2, 0],
        # fmt: on
    ]
    # [START demands_capacities]
    data["demands"] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8, 4 ,4, 5, 8, 3, 5, 3]
    data["vehicle_capacities"] = [30, 38 ,40]
    # [END demands_capacities]
    data["num_vehicles"] = 3
    data["depot"] = 0
    return data
    # [END data_model]

    # [START solution_printer]
def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f"Objective: {solution.ObjectiveValue()}")
    total_distance = 0
    total_load = 0
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
    print(f"Total distance of all routes: {total_distance}m")
    print(f"Total load of all routes: {total_load}")
    # [END solution_printer]


def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    # [START data]
    data = create_data_model()
    # [END data]

    # Create the routing index manager.
    # [START index_manager]
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )
    # [END index_manager]

    # Create Routing Model.
    # [START routing_model]
    routing = pywrapcp.RoutingModel(manager)
    # [END routing_model]

    # Create and register a transit callback.
    # [START transit_callback]
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    # [END transit_callback]

    # Define cost of each arc.
    # [START arc_cost]
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    # [END arc_cost]

    # Add Capacity constraint.
    # [START capacity_constraint]
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
    # [START parameters]
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.FromSeconds(1)
    # [END parameters]

    # Solve the problem.
    # [START solve]
    solution = routing.SolveWithParameters(search_parameters)
    # [END solve]

    # Print solution on console.
    # [START print_solution]
    if solution:
        print_solution(data, manager, routing, solution)
    # [END print_solution]


if __name__ == "__main__":
    main()
# [END program]
