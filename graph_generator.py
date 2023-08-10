import pandas as pd
import strava_api

def connect_to_strava():
    """
    Connects to the Strava API through urllib3

    Parameters:
        None

    Returns:
        connection: an instance of urllib3 Pool Manager 
    """
    connection = strava_api.connect_to_urllib()
    return connection

def strava_data_for_graph():
    """
    Retreives a list of authorized users' activities, and
    converts json containing activities into a dataframe.

    Parameters:
        None
    
    Returns:
        activitiy_data_frame: dataframe containing all activities
    """
    connection = connect_to_strava()
    bool_premium_user = is_user_premium(connection = connection)
    activity_list = strava_api.get_activities(http = connection)
    activity_dict = json_to_dict(activity_data=activity_list)
    activity_data_frame = dict_to_df(dictionary=activity_dict)
    if bool_premium_user == True:
        activity_zone(connection=connection, activity_data_frame=activity_data_frame)
    return activity_data_frame

def json_to_dict(activity_data):
    """
    Converts list of acitvities in json form to a 
    Python dictionary.

    Parameters:
        activity_data: a json containing list of activities
    
    Returns:
        data_dict: dictionary containing list of activities
    """
    data_dict = {}
    if not activity_data:
        return {}
    for i in range(len(activity_data)):
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
    """
    Converts a dictionary of authorized user's
    activities to a dataframe

    Parameters:
        dictionary: dictionary containing list of activities
    
    Returns:
        data_frame: dataframe containing all activities
    """
    data_frame= pd.DataFrame.from_dict(dictionary, orient='index')
    data_frame= data_frame.iloc[::-1]
    data_frame['Heart Rate Zone'] = 0
    return data_frame

def is_user_premium(connection):
    """
    Converts a dictionary of authorized user's
    activities to a dataframe

    Parameters:
        connection: an instance of urllib3 Pool Manager 
    
    Returns:
        boolean: returns boolean value for if the user is a strava
            premium member
    """
    athlete_json = strava_api.get_athlete(http = connection)
    if athlete_json['premium'] == True:
        return True
    else:
        return False

def activity_zone(connection, activity_data_frame):
    """
    If a user is a premium member, add the zone of their activities to their 
    activity dataframe

    Parameters:
        connection: an instance of urllib3 Pool Manager
        activity_data_frame: dataframe containing id, date, avg watts, max watts
    
    Returns:
        activity_dataframe: returns an updated dataframe with zone data
    """
    heart_rate_zones = []
    break_down_zones = dict()
    for df_id in activity_data_frame.index:
        curr_activity_zones = strava_api.get_zones(http=connection, activity_id=df_id)
        for entry in curr_activity_zones:
            if entry["type"] == "heartrate":
                heart_rate_zones = entry["distribution_buckets"]
        time_max = 0
        activity_zone = 0
        for i, zone in enumerate(heart_rate_zones):
            if zone["max"] != -1 and zone["time"] > time_max:
                time_max = zone["time"]
                activity_zone = i
        #Add one to zone because python is 0-indexed but heartrate zones are not
        activity_zone += 1
        activity_data_frame.loc[df_id, ['Heart Rate Zone']] = activity_zone
    return activity_data_frame





        