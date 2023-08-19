import dash
from dash import html, dcc, callback, Output, Input, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__)

cycling_archetype_title = html.H1("Your Cycling Archetype", className="pt-3")

cycling_archetype_description = html.P('''Enter your power maximums for different
lengths of time. These power maximums can often be found on your bike computer or its
companion application if you ride with a power meter. If you don't have this data, but you
know your FTP, various calculators can be found online. I am hoping to integrate this with
the Strava API in the future, but their power stream documentation is quite confusing, and to 
perform these calculations would require a hefty algorithm and a HUGE number of API calls. 
This will have to do for now :)''')

power_form = dbc.Form(
    id= "power-form",
    children = [dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Label("1 Second", html_for="power_grid_left"),
                    dbc.Input(
                        id="one-second-power",
                        placeholder="Enter Power Max...",
                        type="number"

                    ),
                    dbc.Label("10 Second", html_for="power-grid-left"),
                    dbc.Input(
                        id="ten-second-power",
                        placeholder="Enter Power Max...",
                        invalid="numeric"
                    ),
                    dbc.Label("1 Minute", html_for="power-grid-left"),
                    dbc.Input(
                        id="one-minute-power",
                        placeholder="Enter Power Max...",
                        invalid="numeric"
                    ),
                ],
                width=5,
            ),
            dbc.Col(
                [
                    dbc.Label("5 Minute", html_for="power_grid_right"),
                    dbc.Input(
                        id="five-minute-power",
                        placeholder="Enter Power Max...",
                    ),
                    dbc.FormFeedback(
                        "Please enter an integer value",
                        type="invalid",
                    ),
                    dbc.Label("20 Minute", html_for="power-grid-right"),
                    dbc.Input(
                        id="twenty-minute-power",
                        placeholder="Enter Power Max...",
                    ),
                    dbc.FormFeedback(
                        "Please enter an integer value",
                        type="invalid",
                    ),
                    dbc.Label("1 Hour", html_for="power-grid-right"),
                    dbc.Input(
                        id="one-hour-power",
                        placeholder="Enter Power Max...",
                    ),
                    dbc.FormFeedback(
                        "Please enter an integer value",
                        type="invalid",
                    ),
                ],
                width=5,
            ),
            
        ],
    ),
    dbc.Row(
        [
            dbc.Col(dbc.Button("Graph", color="primary"), width="auto", class_name= "py-3"),
        ],
    )],
    class_name="py-5"
)
@callback(
    Output("one-second-power", "invalid"),
    Input("one-second-power", "value"),
    prevent_initial_call= True
)
def check_validity(num):
    if num:
        if num.isdigit():
            return False
    return True

graph = html.Div([
    dcc.Graph(figure={}, id='archetype-graph',
        config={
            'displayModeBar': False
        }),
])

@callback(
    Output("archetype-graph", "figure"),
    Input("power-form", "n_submit"),
    State("one-second-power", "value"),
    State("ten-second-power", "value"),
    State("one-minute-power", "value"),
    State("five-minute-power", "value"),
    State("twenty-minute-power", "value"),
    State("one-hour-power", "value")
)
def update_radar_graph(power_form, one_sec_max, ten_sec_max, one_min_max, five_min_max, twenty_min_max, one_hr_max):
    power_max_list = [one_sec_max, ten_sec_max, one_min_max,five_min_max, twenty_min_max, one_hr_max]

    fig = go.Figure(data=go.Scatterpolar(
        r = power_max_list,
        theta = ['1 second','10 second','1 minute','5 minute', '20 minute', '1 hour'],
        fill='toself'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                autorange = "reversed"
            )
        )
    )
    return fig


layout = dbc.Container(
    children= [
        cycling_archetype_title,
        cycling_archetype_description,
        dbc.Row(dbc.Col(html.Hr())),
        dbc.Row(
            [
                dbc.Col(power_form, class_name="ps-5 pe-0"), 
                dbc.Col(graph, class_name="ps-0 pe-5")
            ],
            justify="around", 
        )
    ]
)

