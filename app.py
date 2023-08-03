import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import back_end
import navbar
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])


navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                for page in dash.page_registry.values()
                if page["name"] == "Cycling graph"
            ],
            nav=True,
            in_navbar=True,
            label="Cycle",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                for page in dash.page_registry.values()
            ],
            nav=True,
            in_navbar=True,
            label="Run",
        ),
    ],
    brand="Into the Know",
    brand_href="home",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    navbar,
	dash.page_container

])

if __name__ == '__main__':
    app.run(debug=True)