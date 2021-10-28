import json
import networkx as nx

g = nx.karate_club_graph()

nodes = [{'id': g.nodes[i]['club']} for i in g.nodes()]
links = [{'source': link[0], 'target': link[1]} for link in g.edges()]

with open('./graph_data.json', 'w') as file:
	json.dump({'nodes': nodes, 'links': links}, file, indent = 4)