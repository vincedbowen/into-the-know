import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import graph_generator


dash.register_page(
    __name__
)

cycling_graph_title = html.H1("Your Cycling Graph", className="pt-3")

cycling_graph_description = html.P('''View historic trends in your power data obtained from
the Strava API. Analyze your average watts and maximum watts for every ride. Hover over points
to see the date and watts for specific rides. If you are a strava premium member (and you have enough API calls
:/ ), you can view your average watts for rides taking place in different heart rate zones. The page may take
more than a few seconds to update depending on how many rides you have. I am improving the page load time
by minimizing API requests.''')


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
    ],
    className = "pb-3"
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
            {"label": "Heart Rate Zone", "value": "Heart Rate Zone", "disabled": False},]
    else:
        return [{"label": "Average Watts", "value": "Average Watts"}, 
            {"label":"Maximum Watts", "value": "Maximum Watts"}, 
            {"label": "Heart Rate Zone", "value": "Heart Rate Zone", "disabled": True},]

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
    if col_chosen != "Heart Rate Zone":
        fig = px.line(data_frame_to_graph, x='Date', y=col_chosen)
    else:
        fig = px.line(data_frame_to_graph, x='Date', y='Average Watts', color = 'Heart Rate Zone')
    return fig

layout = html.Div(
    [
        cycling_graph_title, 
        cycling_graph_description,
        dbc.Row(dbc.Col(html.Hr())), 
        strava_premium, 
        graph_options, 
        display_graph
    ], 
    className="ps-5 pe-5"
)

