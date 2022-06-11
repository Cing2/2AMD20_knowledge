from math import ceil
import numpy as np
import pandas as pd
import matplotlib
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dashboard.data import *
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
        [round(val, 3) for val in df_ranking.values.flatten()], axis=0).tolist()

    fig = go.Figure(data=[go.Table(
        header=dict(values=['Skill', 'Relative Occurrence'],
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
