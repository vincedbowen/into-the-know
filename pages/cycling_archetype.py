import dash
from dash import html, dcc, callback, Output, Input, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__)

cycling_archetype_title = html.H1("Your Cycling Archetype", className="pt-3")

cycling_archetype_description = html.P('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nunc nunc lorem, consectetur sed tincidunt in, tincidunt tempor odio. Integer posuere arcu nec ipsum 
porta, vitae finibus erat varius. Curabitur mattis sapien a nisl maximus posuere. Praesent bibendum 
libero eu posuere condimentum. Nunc quis dolor magna. Vivamus eu metus porta, rutrum ante id, vehicula 
nisl. Vivamus sed nisi sed nisi dictum cursus sed ut libero. Vestibulum facilisis, quam at dictum rutrum, 
justo quam condimentum elit, ac facilisis est dui vitae lectus. Sed imperdiet rhoncus ligula quis 
feugiat. Integer quis est id ex porttitor tincidunt eu eget nibh. Maecenas congue, eros sed hendrerit 
maximus, odio eros ullamcorper nunc, at tincidunt dolor urna et mi. Proin luctus ex quis ex luctus, id 
semper felis suscipit. Integer nisl mi, luctus eu ligula sit amet, faucibus gravida orci.''')

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
                width=5,
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

