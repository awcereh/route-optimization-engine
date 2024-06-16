import networkx as nx
import geopy.distance
import contextily as ctx
import folium
from folium import plugins
import matplotlib.pyplot as plt
import geopy.distance
import networkx as nx
import osmnx as ox
from operator import itemgetter
from scipy.spatial import distance
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import pandas as pd

def get_depot_and_nearest_nodes(G, center_location, district_tempat):
    depot = ox.distance.nearest_nodes(G, center_location[1], center_location[0])
    rute_stops = [(row['latitude'], row['longitude']) for _, row in district_tempat.iterrows()]
    node_stop = [ox.distance.nearest_nodes(G, stop[1], stop[0]) for stop in rute_stops]
    return depot, node_stop

def add_bus_stops_to_graph(G, district_tempat):
    for _, rute_stop in district_tempat.iterrows():
        nearest_node = ox.distance.nearest_nodes(G, rute_stop['longitude'], rute_stop['latitude'])
        dist = geopy.distance.distance((G.nodes[nearest_node]['y'], G.nodes[nearest_node]['x']), (rute_stop['latitude'], rute_stop['longitude']))
        G.add_node(rute_stop['place_id'], x=rute_stop['longitude'], y=rute_stop['latitude'])
        G.add_edge(nearest_node, rute_stop['place_id'], weight=dist.m)
        G.add_edge(rute_stop['place_id'], nearest_node, weight=dist.m)
    return G

def create_routing_model(nodes, NUM_VEHICLES, depot, demands, vehicle_capacities):
    manager = pywrapcp.RoutingIndexManager(len(nodes), NUM_VEHICLES, nodes.index(depot))
    routing = pywrapcp.RoutingModel(manager)
    return routing, manager

def distance_callback(from_node_index, to_node_index, nodes, G, manager):
    from_node = nodes[manager.IndexToNode(from_node_index)]
    to_node = nodes[manager.IndexToNode(to_node_index)]
    return nx.shortest_path_length(G, from_node, to_node)

def add_distance_constraint(routing, transit_callback_index, NUM_VEHICLES):
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,
        3000,
        True,
        dimension_name
    )
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

def solve_routing_problem(routing, search_parameters):
    return routing.SolveWithParameters(search_parameters)

def print_solution(routing, solution, NUM_VEHICLES, manager, vehicle_capacities):
    total_distance = 0
    total_load = 0
    for vehicle_id in range(NUM_VEHICLES):
        index = routing.Start(vehicle_id)
        route_distance = 0
        route_load = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            route_load += demands[node_index]
        route.append(manager.IndexToNode(index))
        print(f"Route for vehicle {vehicle_id}:")
        print(f"{' -> '.join(str(node) + ' Load(' + str(demands[node]) + ')' for node in route)}")
        print(f"Distance of route: {route_distance}m")
        print(f"Load of route: {route_load}\n")
        total_distance += route_distance
        total_load += route_load
    print(f"Total distance of all routes: {total_distance}m")
    print(f"Total load of all routes: {total_load}")
