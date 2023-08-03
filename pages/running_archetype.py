import dash
from dash import Dash, html, dcc, callback, Output, Input
dash.register_page( 
    __name__,
    name = 'Running Archetype'
)

layout = html.Div([
    # navbar.create_navbar(),
    html.Div(children='Running Archetype'),
])