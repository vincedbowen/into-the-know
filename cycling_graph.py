from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import back_end
import navbar
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.FLATLY])


app.layout = html.Div([
    navbar.create_navbar(),
    html.Div(children='Welcome: '),
    dcc.RadioItems(options=['Average Watts', 'Maximum Watts'],
    value='Average Watts', id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph',
        config={
            'displayModeBar': False
        })
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(back_end.initialize(), x='Date', y=col_chosen)
    return fig



if __name__ == '__main__':
    app.run(debug=True)