import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import graph_generator


dash.register_page(
    __name__
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
    data_frame_to_graph = graph_generator.strava_data_for_graph()
    fig = px.line(data_frame_to_graph, x='Date', y=col_chosen)
    return fig
