import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import graph_generator


dash.register_page(
    __name__
)

cycling_graph_title = html.H1("Your Cycling Graph", className="pt-3")

cycling_graph_description = html.P('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nunc nunc lorem, consectetur sed tincidunt in, tincidunt tempor odio. Integer posuere arcu nec ipsum 
porta, vitae finibus erat varius. Curabitur mattis sapien a nisl maximus posuere. Praesent bibendum 
libero eu posuere condimentum. Nunc quis dolor magna. Vivamus eu metus porta, rutrum ante id, vehicula 
nisl. Vivamus sed nisi sed nisi dictum cursus sed ut libero. Vestibulum facilisis, quam at dictum rutrum, 
justo quam condimentum elit, ac facilisis est dui vitae lectus. Sed imperdiet rhoncus ligula quis 
feugiat. Integer quis est id ex porttitor tincidunt eu eget nibh. Maecenas congue, eros sed hendrerit 
maximus, odio eros ullamcorper nunc, at tincidunt dolor urna et mi. Proin luctus ex quis ex luctus, id 
semper felis suscipit. Integer nisl mi, luctus eu ligula sit amet, faucibus gravida orci.''')


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

