from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import requests
# import states
import pickle

app = Flask(__name__)
app.secret_key = 'asdfasdfasdf'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_data_viz():

    stats = {'adult_obesity': 'Adult Obesity',
             'unemployment': 'Unemployment',
             'food_environment_index': 'Food index'}

    try:
        session_data = {}
        for key, value in session.iteritems():
            session_data[key] = value

    except KeyError:
        flash("Looks like you're missing something. Please select from the data sources below.")

    return render_template('index.html',
                           stats=stats,
                           session_data=session_data,
                           )


@app.route('/select_axes')
def select_axes():
    """Recieves form input of which data point to get from API. Redirects to home."""

    session['x_axis'] = request.args.get('x-axis')
    session['y_axis'] = request.args.get('y-axis')
    session['bubble'] = request.args.get('bubble')

    return redirect('/')


@app.route('/get_data.json')
def get_data():

    # API call for list of dictionaries per state
    url = "http://api.datausa.io/api/?show=geo&sumlevel=state&required=" + session['x_axis'] + "," + session['y_axis'] + "," + session['bubble']
    json = requests.get(url).json()
    data = [dict(zip(json["headers"], d)) for d in json["data"]]

    state_names = pickle.loads(pickle.load('state_names'))
    print state_names
    # for state_details in data:
    #     geo_url = 'http://api.datausa.io/attrs/geo/' + state_details['geo']
    #     json = requests.get(geo_url).json()
    #     state_name = json["data"][0][1]
    #     state_details["state_name"] = state_name

    print data

    return jsonify(data)


# ------------------------------ STARTING SERVER -------------------------------
if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host='127.0.0.1')
