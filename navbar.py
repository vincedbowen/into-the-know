import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("My Progression", href="#"),
                    dbc.DropdownMenuItem("My Archetype", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="Cycle",
            ),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("My Progression", href="#"),
                    dbc.DropdownMenuItem("My Archetype", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="Run",
            ),
        ],
        brand="Into the Know",
        brand_href="#",
        color="primary",
        dark=True,
    )
    return navbar