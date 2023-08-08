import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import graph_generator


dash.register_page(
    __name__
)

strava_premium = html.Div(
    [
        dbc.Label("Do you have Strava Premium?"),
        dbc.Checklist(
                options=[
                    {"label": "Yes" , "value": 1},
                ],
                value=[],
                id="switches-input",
                switch=True,
        ),
    ]
)

graph_options = html.Div(
    [
        dbc.RadioItems(
        options={},
        value= {},
        id='controls-and-radio-item',
        inline = True
    ),
    ]
)
@callback(
    Output(component_id="controls-and-radio-item", component_property="options"),
    Input(component_id="switches-input", component_property="value")
)
def update_radio_items(strava_premium_checklist):
    if(strava_premium_checklist == [1]):
        return [{"label": "Average Watts", "value": "Average Watts"}, 
            {"label":"Maximum Watts", "value": "Maximum Watts"}, 
            {"label": "Heart Rate Zones and Power", "value": 2, "disabled": False},]
    else:
        return [{"label": "Average Watts", "value": "Average Watts"}, 
            {"label":"Maximum Watts", "value": "Maximum Watts"}, 
            {"label": "Heart Rate Zones and Power", "value": 2, "disabled": True},]

@callback(
    Output(component_id="controls-and-radio-item", component_property="value"),
    Input(component_id="switches-input", component_property="value")
)
def reset_to_avg_watts(strava_premium_checklist):
    return "Average Watts"


display_graph = html.Div(
    [
       dcc.Graph(figure={}, id='controls-and-graph',
        config={
            'displayModeBar': False
        }),
    ]
)
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    data_frame_to_graph = graph_generator.strava_data_for_graph()
    fig = px.line(data_frame_to_graph, x='Date', y=col_chosen)
    return fig

layout = html.Div([strava_premium, graph_options, display_graph])

