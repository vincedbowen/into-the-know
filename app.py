import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY])

INK_LOGO = "logo.jpeg"

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
    fluid=True,
    class_name="ps-2 pe-md-5 pe-lg-5 pe-xl-5 pe-xxl-5"
)

app.layout = html.Div([
    navbar,
	dash.page_container,
])

if __name__ == '__main__':
    app.run(debug=True)
