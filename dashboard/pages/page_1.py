import math

import pandas as pd
from dash import html, dash_table, dcc
from dash.dependencies import Input, Output
from dashboard.default_values import filter_skills
from dashboard.data import df_occurrence, get_word_count_jobs
from dashboard.app import *
from dashboard.make_figures import fig_live_ranking, colors

fig_ranking = fig_live_ranking(df_occurrence.head())

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div(children=[
        html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
            html.H3(children='Filters',
                    style={'height': '20%', 'textAlign': 'center', 'color': colors['header'],
                           'backgroundColor': colors['color2'], 'padding': '10px 0'}),
        ]),

        html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
            html.H3(children='Ranking',
                    style={'height': '20%', 'textAlign': 'center', 'color': colors['header'],
                           'backgroundColor': colors['color2'], 'padding': '10px 0'}),
        ]),
    ]),
    html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
        dcc.Input(
            id="input_text",
            type="text",
            placeholder="Search skill",
        ),
    ]),

    html.Div(children=[
        html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
            dash_table.DataTable(
                id='table_filter',
                data=[{'Skill': feat} for feat in filter_skills if feat not in df_occurrence.head().index.tolist()],
                row_selectable='multi',
                style_cell={'textAlign': 'left',
                            'backgroundColor': colors['background'],
                            'color': colors['text']},
                style_header={
                    'backgroundColor': colors['color2'],
                    'fontWeight': 'bold',
                    'color': colors['text']
                },
            ),
        ]),

        html.Div(style={'width': '50%', 'display': 'inline-block'}, children=[
            html.Div([
                html.Div('a', style={'color': colors['background']}),
                dcc.Graph(
                    id='ranking',
                    figure=fig_ranking
                )
            ])
        ])
    ])
])


# TODO: Use API to also search for synonyms

@app.callback(
    Output(component_id='ranking', component_property='figure'),
    Input(component_id='table_filter', component_property='selected_rows'),
    Input(component_id='input_text', component_property='value'),
)
def update_output_p1(selected_idxs, input_text):
    # Do some dataset operations to return top 5 skills and include selected skill(s)
    df_rank = df_occurrence.head()
    if selected_idxs is not None:
        selected_values = [filter_skills[selected_idx] for selected_idx in selected_idxs]
        df_rank = pd.concat([df_rank, df_occurrence.loc[selected_values, :]])

    if input_text is not None:
        try:
            # print(df_occurrence.loc[input_text, :].values)
            df_new = pd.DataFrame([df_occurrence.loc[input_text, :].values.tolist()], index=[input_text],
                                  columns=['relative_occurrence_job', 'total'])
        except:
            values = get_word_count_jobs(input_text)
            df_new = pd.DataFrame([[values[1], values[0]]], index=[input_text],
                                  columns=['relative_occurrence_job', 'total'])
        df_rank = pd.concat([df_rank, df_new])

    fig_rank = fig_live_ranking(df_rank)
    return fig_rank
