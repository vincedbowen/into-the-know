from myApp import json_to_dict, dict_to_df
import json
import pandas as pd

def test_empty_json():
    json_file = open('empty_data.json')
    data = json.load(json_file)
    assert json_to_dict(data) == {}

def test_empty_dict():
    empty_dict = {}
    empty_df = dict_to_df(empty_dict)
    assert empty_df.empty == True
