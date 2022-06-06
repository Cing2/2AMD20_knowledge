from dash import html, dash_table, dcc
from dash.dependencies import Input, Output
from dashboard.default_values import *
from dashboard.data import *
from dashboard.app import *
from dashboard.make_figures import *


filter_skills = [f'S{i}' for i in range(1, 11)]


layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H2(children='Hard Skills',
            style={'height': '50%', 'textAlign': 'center',
                   'backgroundColor': colors['color2'], 'padding': '10px 0',
                   'color': colors['header']}),

    html.H3(children='Filter',
            style={'height': '20%', 'textAlign': 'center', 'color': colors['header'],
                   'backgroundColor': colors['color2'], 'padding': '10px 0'}),

    html.Div(children=[
        html.Div(style={'width': '49%', 'display': 'inline-block'}, children=[
            dcc.Dropdown(filter_skills, filter_skills[0], id='dropdown_scatter_h1',
                         style={'backgroundColor': colors['background'], 'color': 'white'}),
        ]),
    ]),

    html.H3(children='Ranking',
            style={'height': '20%', 'textAlign': 'center', 'color': colors['header'],
                   'backgroundColor': colors['color2'], 'padding': '10px 0'}),

    html.P(id='my-output_h1'),
    html.P(id='my-output_h2'),
    html.P(id='my-output_h3'),
    html.P(id='my-output_h4'),
    html.P(id='my-output_h5'),

])


@app.callback(
    Output(component_id='my-output_h1', component_property='children'),
    Output(component_id='my-output_h2', component_property='children'),
    Output(component_id='my-output_h3', component_property='children'),
    Output(component_id='my-output_h4', component_property='children'),
    Output(component_id='my-output_h5', component_property='children'),
    Input(component_id='dropdown_scatter_h1', component_property='value')
)
def update_output_p2(input_value):
    # Do some dataset operations to return top 5 skills
    returns = [f'Output: {input_value}_{i}' for i in range(1, 6)]
    return returns[0], returns[1], returns[2], returns[3], returns[4]
