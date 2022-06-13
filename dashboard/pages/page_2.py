from dash import html, dash_table, dcc
from dash.dependencies import Input, Output
from dashboard.default_values import *
from dashboard.data import *
from dashboard.app import *
from dashboard.make_figures import *


fig_k_graph = knowledge_graph()


layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div(style={'height': '80vh'}, children=[
        dcc.Graph(
            id='k_graph',
            figure=fig_k_graph
        ),
    ]),

    html.Div(children=[html.Div('Minimum number of links', style={'color': colors['text'], 'textAlign': 'center'}),
                       dcc.Slider(min=0, max=1000, step=25, id='slider_bins', value=500)])
])


@app.callback(
    Output(component_id='k_graph', component_property='figure'),
    Input(component_id='slider_bins', component_property='value'),
)
def update_output_p2(input_bin):
    fig_rank = knowledge_graph(input_bin)
    return fig_rank
