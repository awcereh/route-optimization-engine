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

def load_data(file_path):
    return pd.read_csv(file_path)

def group_and_calculate_median(data):
    district_tempat = data.groupby('place_id')[['latitude', 'longitude']].median().reset_index()
    district_tempat.columns = ['place_id', 'latitude', 'longitude']
    return district_tempat

def get_highway_graph(center_location, dist):
    G = ox.graph_from_point(center_location, dist=dist, network_type='drive')
    return ox.utils_graph.get_largest_component(G, strongly=True)

def create_map_and_plot_routes(G, depot, rute_stops_df, nodes, solution, routing, manager, NUM_VEHICLES, center_location):
    m = folium.Map(location=center_location, zoom_start=16)
    depot_coords = (G.nodes[depot]['y'], G.nodes[depot]['x'])
    folium.Marker(location=depot_coords, icon=folium.Icon(color='red', icon='home', prefix='fa'), tooltip=f"Depot {depot_coords}").add_to(m)
    for index, rute_stop in rute_stops_df.iterrows():
        stop_coords = (rute_stop['latitude'], rute_stop['longitude'])
        folium.Marker(location=stop_coords, icon=folium.Icon(color='green', icon='circle', prefix='fa'), tooltip=f"Pemberhentian {stop_coords}").add_to(m)
    colors = ['blue', 'orange', 'yellow', 'green']
    for vehicle_id in range(NUM_VEHICLES):
        index = routing.Start(vehicle_id)
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(nodes[node_index])
            index = solution.Value(routing.NextVar(index))
        route.append(nodes[manager.IndexToNode(index)])
        color = colors[vehicle_id % NUM_VEHICLES]
        segments = []
        for i in range(len(route)-1):
            path = nx.shortest_path(G, route[i], route[i + 1], weight='length')
            segments.append([(G.nodes[node]['y'], G.nodes[node]['x']) for node in path])
        for segment in segments:
            vehicle_tooltip = vehicle_id
            folium.PolyLine(locations=segment, color=color, weight=5, tooltip=f"Vehicle{vehicle_tooltip}").add_to(m)
            ant_path = plugins.AntPath(
                locations=segment,
                color=color,
                dash_array=[10, 50],
                delay=500,
                weight=5,
            )
            m.add_child(ant_path)
    return m

