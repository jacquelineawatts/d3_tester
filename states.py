import pickle
import requests


def pickle_state_names(data):
    """Make call to API to find state names from ID, pickles object."""

    file_object = open('state_names', 'w')

    state_names = {}
    for state_details in data:
        state_id = state_details['geo']
        geo_url = 'http://api.datausa.io/attrs/geo/' + state_id
        json = requests.get(geo_url).json()
        state_name = json["data"][0][1]
        state_names[state_id] = state_name

    pickle.dump(state_names, file_object)
