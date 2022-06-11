from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

import article_terms

df_scientist_us_jobs = pd.read_csv('../data/data_scientist_united_states_job_postings_jobspikr.csv')
df_datascientist = pd.read_csv('../data/DataScientist.csv', index_col=0)


def count_occurrences_words(text: str, list_words: List[str]):
    word_count = [text.count(word) for word in list_words]

    word_occurrence = np.zeros((len(list_words), len(list_words)))
    for i, count in enumerate(word_count):
        for j, count2 in enumerate(word_count):
            if count > 0 and count2 > 0:
                word_occurrence[i, j] += 1
                word_occurrence[j, i] += 1
    return word_occurrence


def word_cooccurence(df, list_words, col_to_search):
    df['word_occur'] = df[col_to_search].apply(lambda x: count_occurrences_words(x, list_words))
    total_word_cooccurrence = np.zeros((len(list_words), len(list_words)))
    for i, value in df['word_occur'].iteritems():
        total_word_cooccurrence += value

    return total_word_cooccurrence


word_cooccurence_job1 = word_cooccurence(df_datascientist, article_terms.all_traits_skills, 'Job Description')

word_cooccurence_job2 = word_cooccurence(df_scientist_us_jobs, article_terms.all_traits_skills, 'job_description')

total_word_cooccurrence = word_cooccurence_job1 + word_cooccurence_job2


def show_graph_with_labels(adjacency_matrix, labels):
    node_size = np.sqrt(np.diag(adjacency_matrix)) * 10
    adjacency_matrix = adjacency_matrix.copy()
    np.fill_diagonal(adjacency_matrix, 0)
    rows, cols = np.where(adjacency_matrix > 50)

    # show only nodes that have a connection
    idxs_nodes = np.unique(np.concatenate([rows, cols]))
    adjacency_matrix = adjacency_matrix[idxs_nodes][:, idxs_nodes]
    labels = [labels[i] for i in idxs_nodes]
    labels = {i: a for i, a in enumerate(labels)}
    node_size = node_size[idxs_nodes]

    print(adjacency_matrix.shape, len(labels), len(node_size))
    print(node_size, type(node_size[0]))
    # create graph
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    # all_rows = range(0, adjacency_matrix.shape[0])
    for n in idxs_nodes:
        gr.add_node(n)
    gr.add_edges_from(edges)

    plt.figure(figsize=(16, 16))
    pos = nx.spring_layout(gr, k=0.55, iterations=40)
    nx.draw(gr, pos=pos, labels=labels, with_labels=True, node_size=node_size)
    plt.show()
    return gr


G = show_graph_with_labels(total_word_cooccurrence, article_terms.all_traits_skills)
