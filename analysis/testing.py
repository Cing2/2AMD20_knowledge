import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

import article_terms

total_word_cooccurrence = np.load('../output/word_occurence_matrix.npy')


def show_graph_with_labels(adjacency_matrix, labels):
    node_size = np.sqrt(np.diag(adjacency_matrix)) * 10
    adjacency_matrix = adjacency_matrix.copy()
    np.fill_diagonal(adjacency_matrix, 0)
    rows, cols = np.where(adjacency_matrix > 50)

    # show only nodes that have a connection
    idxs_nodes = np.unique(np.concatenate([rows, cols]))
    # adjacency_matrix = adjacency_matrix[idxs_nodes][:, idxs_nodes]
    # labels = [labels[i] for i in idxs_nodes]
    labels = {i: a for i, a in enumerate(labels)}
    # node_size = node_size[idxs_nodes]

    print(adjacency_matrix.shape, len(labels), len(node_size))
    # print(node_size, type(node_size[0]))
    # create graph
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    all_rows = range(0, adjacency_matrix.shape[0])
    for n in all_rows:
        gr.add_node(n)
    gr.add_edges_from(edges)

    plt.figure(figsize=(16, 16))
    pos = nx.spring_layout(gr, k=0.55, iterations=40)
    nx.draw(gr, nodelist=idxs_nodes, pos=pos, labels=labels, with_labels=True, node_size=node_size[idxs_nodes])
    plt.show()
    return gr


G = show_graph_with_labels(total_word_cooccurrence, article_terms.all_traits_skills)
