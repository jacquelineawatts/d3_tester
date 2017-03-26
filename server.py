from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import requests
from states import pickle_state_names
from api_data import column_to_title
import pickle
import timeit

app = Flask(__name__)
app.secret_key = 'asdfasdfasdf'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """Displays index page."""

    return render_template('index.html', column_to_title=column_to_title)


@app.route('/results')
def show_data_viz():
    """Shows data viz based on form input.

    For now, construct select_axes route with get request form selections on the 
    first round or session variables will throw a key error."""

    try:
        session_data = {}
        for key, value in session.iteritems():
            session_data[key] = value

    except KeyError:
        flash("Looks like you're missing something. Please select from the data sources below.")

    return render_template('results.html',
                           column_to_title=column_to_title,
                           session_data=session_data,
                           )


@app.route('/select_axes')
def select_axes():
    """Recieves form input of which data point to get from API. Redirects to home."""

    session['x_axis'] = request.args.get('x-axis')
    session['y_axis'] = request.args.get('y-axis')
    session['bubble'] = request.args.get('bubble')

    return redirect('/results')


@app.route('/get_data.json')
def get_data():

    start_time = timeit.default_timer()
    # API call for list of dictionaries per state
    url = "http://api.datausa.io/api/?show=geo&sumlevel=state&required=" + session['x_axis'] + "," + session['y_axis'] + "," + session['bubble']
    json = requests.get(url).json()
    response_data = [dict(zip(json["headers"], d)) for d in json["data"]]


    file_object = open('state_names')
    state_names = pickle.load(file_object)

    for state in response_data:
        state['state_name'] = state_names[state['geo']]

    # If needed, can pickle state names again by uncommenting below.
    # pickle_state_names(data)

    elapsed = timeit.default_timer() - start_time
    print 'DATA: ', response_data
    print 'TIME REQUIRED: ', elapsed

    columns = {}
    for key in ['x_axis', 'y_axis', 'bubble']:
        columns[key] = session[key]

    data = {'response_data': response_data,
            'columns': columns,
            }

    return jsonify(data)


# ------------------------------ STARTING SERVER -------------------------------
if __name__ == "__main__":

    app.debug = True
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host='127.0.0.1')
