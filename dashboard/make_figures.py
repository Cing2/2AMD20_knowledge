from math import ceil
import networkx as nx
import numpy as np
import pandas as pd
import matplotlib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dashboard.data import *
from article_terms import all_traits_skills
from dashboard.default_values import *


def add_colors_figure(fig):
    """Function to update the layout of a figure to the default colors."""
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig


def fig_live_ranking(df_ranking):
    """Function to create and return the summary statistics table for all groups."""
    df_ranking = df_ranking.drop_duplicates().sort_values(by=['relative_occurrence_job'], ascending=False)

    values = np.expand_dims(df_ranking.index, axis=0).tolist() + np.expand_dims(
        [round(val, 3) for val in df_ranking['relative_occurrence_job'].values.flatten()], axis=0).tolist() + np.expand_dims(
        [round(val, 0) for val in df_ranking['total'].values.flatten()], axis=0).tolist()

    fig = go.Figure(data=[go.Table(
        header=dict(values=['Skill', 'Relative Occurrence', 'Total Occurrence'],
                    fill_color='paleturquoise',
                    font_color='black',
                    align='left'),
        cells=dict(values=values,
                   fill_color='lavender',
                   font_color='black',
                   align='left'))
    ])

    fig = add_colors_figure(fig)

    return fig


def knowledge_graph(min_nr_links: int = 500):
    total_word_cooccurrence = np.load('output/word_occurence_matrix.npy')

    def network_graph(adjacency_matrix, labels, min_nr_links=100):
        node_size = np.sqrt(np.diag(adjacency_matrix)) * 10
        adjacency_matrix = adjacency_matrix.copy()
        np.fill_diagonal(adjacency_matrix, 0) # remove self links
        # get nodes which have at least x links
        rows, cols = np.where(adjacency_matrix > min_nr_links)

        # show only nodes that have a connection
        idxs_nodes = np.unique(rows)
        node_size = node_size[idxs_nodes]
        # print(f'Nodes remaining, with {min_nr_links} links:',len(idxs_nodes))

        # create graph
        edges = zip(rows.tolist(), cols.tolist())
        G = nx.Graph()
        G.add_edges_from(edges)
        pos = nx.spring_layout(G, k=0.55, iterations=40, seed=0)

        # edges trace
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(color='black', width=1),
            hoverinfo='none',
            showlegend=False,
            mode='lines')

        # nodes trace
        node_x = []
        node_y = []
        text = []
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            text.append(labels[node])

        node_trace = go.Scatter(
            x=node_x, y=node_y, text=text,
            mode='markers+text',
            showlegend=False,
            hoverinfo='none',
            textfont=dict(color='black', size=15),
            marker=dict(
                color='lightblue',
                size=40,
                line=dict(color='black', width=1)))

        # layout
        layout = dict(plot_bgcolor='white',
                      paper_bgcolor='white',
                      margin=dict(t=10, b=10, l=10, r=10, pad=0),
                      xaxis=dict(linecolor='black',
                                 showgrid=False,
                                 showticklabels=False,
                                 mirror=True),
                      yaxis=dict(linecolor='black',
                                 showgrid=False,
                                 showticklabels=False,
                                 mirror=True),
                      height=800)

        # figure
        fig = go.Figure(data=[edge_trace, node_trace], layout=layout)
        return fig

    fig = network_graph(total_word_cooccurrence, all_traits_skills, min_nr_links=min_nr_links)

    return fig
