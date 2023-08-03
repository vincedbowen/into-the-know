import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import back_end
import navbar
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    title='test',
    name='Cycling Graph'
)


layout = html.Div([
    # navbar.create_navbar(),
    html.Div(children='Welcome: '),
    dbc.RadioItems(
        options=['Average Watts', 'Maximum Watts'],
        value='Average Watts', 
        id='controls-and-radio-item',
        inline = True
    ),
    dcc.Graph(figure={}, id='controls-and-graph',
        config={
            'displayModeBar': False
        })
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(back_end.initialize(), x='Date', y=col_chosen)
    return fig

