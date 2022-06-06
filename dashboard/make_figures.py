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
