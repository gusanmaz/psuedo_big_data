import networkx as nx
import matplotlib.pyplot as plt
import csv


# Read the data from the CSV file and create a graph using NetworkX
def read_train_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the first row
        edges = [(row[0], row[1], {'weight': float(row[2])}) for row in reader]
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def visualize(in_path="data/graph/train_routes.csv", out_path="data/graph/train_routes.png", figsize=(30, 30)):
    G = read_train_data(in_path)
    # Create a layout for the nodes
    pos = nx.spring_layout(G)

    # Draw the nodes and edges
    nx.draw_networkx_nodes(G, pos, node_size=100)
    nx.draw_networkx_edges(G, pos, width=1)

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Draw node labels
    node_labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels)

    # Set the plot limits to fit the graph
    x_min, x_max = min(pos.values(), key=lambda x: x[0])[0], max(pos.values(), key=lambda x: x[0])[0]
    y_min, y_max = min(pos.values(), key=lambda x: x[1])[1], max(pos.values(), key=lambda x: x[1])[1]
    plt.xlim(x_min - 0.1, x_max + 0.1)
    plt.ylim(y_min - 0.1, y_max + 0.1)

    # Set the plot size
    plt.gcf().set_size_inches(*figsize)

    # Save the plot to a file
    plt.savefig(out_path, bbox_inches='tight')


