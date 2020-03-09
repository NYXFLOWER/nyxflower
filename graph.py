import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


# #############################################################################
#                               Generation
# #############################################################################
def random_graph():
    np.random.seed(0)
    n_node = 50
    n_edge = 200

    edges = np.random.randint(n_node, size=(2, n_edge))
    weights = np.random.random(size=n_edge)
    nnn = 0.5


# #############################################################################
#                              Visualization
# #############################################################################
def draw_to_file(edges, weights, threshold=0.5,
                 file_name="new_plot",
                 figure_size=(10, 8)):
    """ edges: ndarray, size=(2, num_edges) """
    G = nx.Graph()

    # build graph
    mask = np.where(weights > threshold)[-1]
    edges = edges[:, mask]
    edges = zip(edges[0], edges[1], weights[mask])
    G.add_weighted_edges_from(edges)

    # draw graph and save to file
    plt.figure(figsize=figure_size)
    nx.draw_spring(G, with_labels=True, font_weight='bold', )
    plt.savefig("./{}.png".format(file_name))