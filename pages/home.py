import dash
from dash import html

dash.register_page( 
    __name__,
    path = '/')

layout = html.Div([
    # navbar.create_navbar(),
    html.Div(children='Home'),
])
