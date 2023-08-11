import dash
from dash import html, dcc, callback, Output, Input, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__)



power_form = dbc.Form(
    id= "power-form",
    children = dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Label("1 Second", html_for="power_grid_left"),
                    dbc.Input(
                        id="one-second-power",
                        placeholder="Enter Power Max...",
                    ),
                    dbc.Label("10 Second", html_for="example-email-grid"),
                    dbc.Input(
                        id="ten-second-power",
                        placeholder="Enter Power Max...",
                    ),
                    dbc.Label("1 Minute", html_for="example-email-grid"),
                    dbc.Input(
                        id="one-minute-power",
                        placeholder="Enter Power Max...",
                    ),
                ],
                width=2,
            ),
            dbc.Col(
                [
                    dbc.Label("5 Minute", html_for="power_grid_right"),
                    dbc.Input(
                        id="five-minute-power",
                        placeholder="Enter Power Max...",
                    ),
                    dbc.Label("20 Minute", html_for="example-password-grid"),
                    dbc.Input(
                        id="twenty-minute-power",
                        placeholder="Enter Power Max...",
                    ),
                    dbc.Label("1 Hour", html_for="example-password-grid"),
                    dbc.Input(
                        id="one-hour-power",
                        placeholder="Enter Power Max...",
                    ),
                ],
                width=2,
            ),
            dbc.Col(dbc.Button("Submit", color="primary"), width="auto", class_name= "py-5"),
        ],
    )
)

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


layout = html.Div([power_form, graph])

