import os
import json
from dotenv import load_dotenv
import urllib3
import certifi


def connect_to_urllib():
    """
    Creates a Pool Manager instance to allow requests to be made.
    "This object handles all of the details of 
    connection pooling and thread safety so that you don't have to"
        -(https://urllib3.readthedocs.io/en/stable/user-guide.html)
    
    Parameters: 
        None

    Returns:
        http: an instance of urllib3 Pool Manager 
    """
    #Get request to strava API
    http = urllib3.PoolManager(
        cert_reqs="CERT_REQUIRED",
        ca_certs=certifi.where(),
        maxsize = 1,
        block = True
    )
    return http

def authenticate():
    """
    Retrieves Authorization token for Strava API.

    Parameters: 
        None

    Returns:
        strava_authorization: access token required to make calls 
            with the Strava API
    """
    load_dotenv()
    strava_authorization = os.getenv('authorization_token')
    return strava_authorization

def get_athlete(http):
    """
    Displays data of the current authorized user.

    Parameters:
        http: an instance of urllib3 Pool Manager 
    
    Returns:
        athlete_data: a dictionary (json) holding data
            regarding the current Strava user
    """
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
    """
    Displays a list of the current authorized user's activities.

    Parameters:
        http: an instance of urllib3 Pool Manager 
    
    Returns:
        activity_data: a json holding all
            public user activities
    """
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

def get_zones(http, activity_id):
    """
    For premium Strava users only. Returns a list of zones for a specific activity

    Parameters:
        http: an instance of urllib3 Pool Manager 
        activity_id: the id of activity to determine training zone
    
    Returns:
        zone_data: a json holding training zones for a specific activity
    """
    
    zone_response = http.request(
        "GET",
        "https://www.strava.com/api/v3/activities/{}/zones".format(activity_id),
        headers={
            'Authorization': 'Bearer ' + authenticate()
        },
        timeout = 4,
        retries = 4
    )
    zone_data = json.loads(zone_response.data)
    return zone_data

def need_new_token(http):
    """
    Determines if a new access token needs to be generated. Through the Strava
    API, access keys expire every 6 hours. 

    Parameters:
        http: an instance of urllib3 Pool Manager 
    
    Returns:
        boolean: returns boolean value for if a new token
             must be generated
    """
    auth_response = http.request(
        "GET",
        "https://www.strava.com/api/v3/athlete/activities",
        headers={
            'Authorization': 'Bearer ' + authenticate()
        },
        timeout = 4,
        retries = 4
    )
    auth_status = auth_response.status
    if auth_status == 401:
        return True
    else:
        return False

def generate_new_token(http):
    """
    Generates a new access token for the Strava API. This will 
    be saved as an enviromental variable.

    Parameters:
        http: an instance of urllib3 Pool Manager 
    
    Returns:
        Nothing
    """
    load_dotenv()
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')
    refresh_token = os.getenv('refresh_token')
    refresh_url = "https://www.strava.com/api/v3/oauth/token?client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=refresh_token&refresh_token=" + refresh_token +"&scope=read, activity:read"
    token_response = http.request(
        "Post",
        refresh_url,
        headers={
            'Authorization': 'Bearer ' + authenticate()
        }
    )
    refresh_data = json.loads(token_response.data)
    os.environ["stravaAuth"] = refresh_data["access_token"]
    return