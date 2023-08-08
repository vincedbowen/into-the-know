from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

import pandas as pd
from pages import cycling_graph
from cycling_graph import update_graph
from back_end import initialize


def test_update_graph():
    test_data = [['2022-01-23', 101, 860], ['2022-04-21', 156, 860], 
        ['2022-07-11', 346, 907], ['2022-11-13', 250, 400],
        ['2023-01-12', 302, 503],['2023-03-07', 147, 367],
        ['2023-06-30', 185, 754]]
    data_frame = pd.DataFrame(test_data, columns=['Date', 'Average Watts', 'Maximum Watts'])
    output = update_graph('Average Watts')
    
    assert output == px.line(initialize(), x='Date', y='Average Watts')
