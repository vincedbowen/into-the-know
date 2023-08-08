import graph_generator 
import json
import pandas as pd

def test_empty_json():
    json_file = open('empty_data.json')
    data = json.load(json_file)
    assert graph_generator.json_to_dict(data) == {}

def test_empty_dict():
    empty_dict = {}
    empty_df = graph_generator.dict_to_df(empty_dict)
    assert empty_df.empty == True
