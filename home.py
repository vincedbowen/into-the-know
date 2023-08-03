from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import back_end
import navbar
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.FLATLY])

app.layout = html.Div([
    navbar.create_navbar(),
    html.Div(children='Home Page'),
])

if __name__ == '__main__':
    app.run(debug=True)