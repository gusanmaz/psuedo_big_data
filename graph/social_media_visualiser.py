import networkx as nx
import matplotlib.pyplot as plt
import csv


def visualize(input="data/graph/social_media.csv", output="data/graph/social_media.png"):
    # Read the CSV file
    with open(input, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        edges = [(row[0], row[1]) for row in reader]

    # Create the directed graph
    G = nx.DiGraph()
    G.add_edges_from(edges)

    # Add node attributes for account handles and number of posts
    with open(input, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # skip the first row
        for row in reader:
            if len(row) >= 2:
                G.nodes[row[0]]['account_handle'] = row[0]
            if len(row) >= 7:
                G.nodes[row[0]]['num_posts'] = row[6]

    # Draw the graph
    pos = nx.spring_layout(G, k=5)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', alpha=0.7, node_size=500)
    nx.draw_networkx_labels(G, pos, labels={node: G.nodes[node].get('account_handle', '') for node in G.nodes()}, font_size=8)
    nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5, arrows=True)
    plt.axis('off')
    plt.savefig(output)
