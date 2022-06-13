from dash import dcc, html
from dash.dependencies import Input, Output

from dashboard.app import app
from dashboard.default_values import colors
from dashboard.pages import page_1
from dashboard.pages import page_2


tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'backgroundColor': colors['background'],
    'color': colors['text']
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': colors['color2'],
    'color': 'white',
    'padding': '6px'
}

tabbed_layout = html.Div(style={'backgroundColor': colors['background'],
                                "position": "absolute",
                                "padding": "0",
                                "margin": "0",
                                "top": "0",
                                "left": "0",
                                "width": "100%",
                                "height": "100%",
                                }, children=[
    html.H1(children='Most Wanted Data Scientist Skills',
            style={
                'textAlign': 'center',
                'color': colors['header_tool'],
                'padding-top': '1%',
                'padding-bottom': '10px',
                'font-weight': 'bold',
                'margin-bottom': '0',
                'backgroundColor': colors['color3']
            }),
    dcc.Tabs(id="page_tabs", value='page1', children=[
        dcc.Tab(label='Skills Ranking', value='page1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Knowledge Graph', value='page2', style=tab_style, selected_style=tab_selected_style),
    ],
             style={'height': '44px'}),
    html.Div(id='page_content')
])

### Set app layout to page container ###
app.layout = tabbed_layout
app.validation_layout = html.Div(
    children=[
        tabbed_layout,
        page_1.layout,
        page_2.layout
    ]
)


@app.callback(Output('page_content', 'children'),
              Input('page_tabs', 'value'))
def render_content(tab):
    if tab == 'page1':
        return page_1.layout
    elif tab == 'page2':
        return page_2.layout
