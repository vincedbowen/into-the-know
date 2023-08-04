import json
import pandas as pd
import strava_api

def connect_to_strava():
    connection = strava_api.connect_to_urllib()
    return connection

def strava_data_for_graph():
    connection = connect_to_strava()
    activity_list = strava_api.get_activities(http = connection)
    activity_dict = json_to_dict(activity_data=activity_list)
    activity_data_frame = dict_to_df(dictionary=activity_dict)
    return activity_data_frame

def json_to_dict(activity_data):
    data_dict = {}
    if not activity_data:
        return {}
    for i, element in enumerate(activity_data):
        if activity_data[i]['device_watts'] is True:
            if activity_data[i]['id'] not in data_dict.keys():
                data_dict[activity_data[i]['id']] = {
                    'Date' : activity_data[i]['start_date'],
                    'Average Watts' : activity_data[i]['average_watts'], 
                    'Maximum Watts' : activity_data[i]['max_watts']
                }
            else:
                print("err")
    return data_dict

def dict_to_df(dictionary):
    data_frame= pd.DataFrame.from_dict(dictionary, orient='index')
    data_frame= data_frame.iloc[::-1]
    return data_frame

