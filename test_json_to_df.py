import my_app
import back_end 
import json
import pandas as pd

def test_empty_json():
    json_file = open('empty_data.json')
    data = json.load(json_file)
    assert back_end.json_to_dict(data) == {}

def test_empty_dict():
    empty_dict = {}
    empty_df = back_end.dict_to_df(empty_dict)
    assert empty_df.empty == True
