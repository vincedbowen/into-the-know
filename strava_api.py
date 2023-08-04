import os
import json
from dotenv import load_dotenv
import urllib3
import certifi


def connect_to_urllib():
    #Get request to strava API
    http = urllib3.PoolManager(
        cert_reqs="CERT_REQUIRED",
        ca_certs=certifi.where(),
        maxsize = 1,
        block = True
    )
    return http

def authenticate():
    load_dotenv()
    strava_authorization = os.getenv('stravaAuth')
    return strava_authorization

def get_athlete(http):
    athlete_response = http.request(
        "GET",
        "https://www.strava.com/api/v3/athlete/",
        headers={
            'Authorization': 'Bearer ' + authenticate()
        },
        timeout = 4,
        retries = 4
    )
    athlete_data = json.loads(athlete_response.data)
    return athlete_data

def get_activities(http):
    activity_response = http.request(
        "GET",
        "https://www.strava.com/api/v3/athlete/activities",
        headers={
            'Authorization': 'Bearer ' + authenticate()
        },
        timeout = 4,
        retries = 4
    )
    activity_data = json.loads(activity_response.data)
    return activity_data