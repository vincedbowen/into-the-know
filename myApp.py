from dash import Dash, html, dcc, callback, Output, Input
import urllib3
#for https certificates
import certifi
from dotenv import load_dotenv
import os
import json
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__)

load_dotenv()
stravaAuthorization = os.environ['stravaAuth']
#Get request to strava API
http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)
response = http.request(
    "GET",
    "https://www.strava.com/api/v3/athlete/activities",
    headers={
        'Authorization': 'Bearer ' + stravaAuthorization
    },
    timeout = 4,
    retries = 4
)
myData = json.loads(response.data)

data_dict = dict()
for i in range(len(myData)):
    if myData[i]['device_watts'] == True:
        if myData[i]['id'] not in data_dict.keys():
            data_dict[myData[i]['id']] = {'Date' : myData[i]['start_date'], 'Average Watts' : myData[i]['average_watts'], 'Maximum Watts' : myData[i]['max_watts']}
        else:
            print("err")
df = pd.DataFrame.from_dict(data_dict, orient='index')
df = df.iloc[::-1]


app.layout = html.Div([
    html.Div(children='Title of Dash App'),
    dcc.RadioItems(options=['Average Watts', 'Maximum Watts'], value='Average Watts', id='controls-and-radio-item'),
    dcc.Graph(figure={}, id='controls-and-graph')
])


@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(df, x='Date', y=col_chosen)
    return fig
    
if __name__ == '__main__':
    app.run(debug=True)