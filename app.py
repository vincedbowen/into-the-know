import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem('Cycling Graph', href='/cycling-graph'),
                dbc.DropdownMenuItem('Cycling Archetype', href='/cycling-archetype'),
            ],
            nav=True,
            in_navbar=True,
            label="Cycle",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem('Running Graph', href='/running-graph'),
                dbc.DropdownMenuItem('Running Archetype', href='/running-archetype'),
            ],
            nav=True,
            in_navbar=True,
            label="Run",
        ),
        dbc.NavItem(dbc.NavLink('About', href= '/about'))
    ],
    brand='Into the Know',
    brand_href='/',
    color='primary',
    dark=True,
)

app.layout = html.Div([
    navbar,
	dash.page_container,
])

if __name__ == '__main__':
    app.run(debug=True)
