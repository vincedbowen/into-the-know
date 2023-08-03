import os
import json
import urllib3
#for https certificates
import certifi
from dotenv import load_dotenv
import pandas as pd

def connect_to_urllib():
    #Get request to strava API
    http = urllib3.PoolManager(
        cert_reqs="CERT_REQUIRED",
        ca_certs=certifi.where()
    )
    return http

def get_athlete(http, auth):
    athlete_response = http.request(
        "GET",
        "https://www.strava.com/api/v3/athlete/",
        headers={
            'Authorization': 'Bearer ' + auth
        },
        timeout = 4,
        retries = 4
    )
    athlete_data = json.loads(athlete_response.data)
    return athlete_data

def get_activities(http, auth):
    activity_response = http.request(
        "GET",
        "https://www.strava.com/api/v3/athlete/activities",
        headers={
            'Authorization': 'Bearer ' + auth
        },
        timeout = 4,
        retries = 4
    )
    activity_data = json.loads(activity_response.data)
    return activity_data

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


def initialize():
    load_dotenv()
    strava_authorization = os.environ['stravaAuth']
    http = connect_to_urllib()
    activity_json = get_activities(http=http, auth= strava_authorization)
    activity_dict = json_to_dict(activity_data=activity_json)
    data_frame = dict_to_df(dictionary=activity_dict)
    return data_frame
