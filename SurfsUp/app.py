# 1. Import the Kitchen
#import numpy as np
#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask
from flask import jsonify

# 2. Create an app being sure to pass __name__.
app = Flask(__name__)

# 3. Define what to do when a user hits the index route.
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (f"Available Routes:<br/>"
            f"Precipitation at /api/v1.0/precipitation<br/>"
            f"Stations at /api/v1.0/station<br/>"
            f"TOBS at /api/v1.0/tobs<br/>"
            f"Temperature Query at /api/v1.0/querytemps<br/>"
    )

# 4. Define the other routes
@app.route("/api/v1.0/precipitation")
def fprecipitation():
    print("Server received request for 'precipitation' page...")
    return "Hawaii Precipitation"

@app.route("/api/v1.0/stations")
def fstations():
    print("Server received request for 'stations' page...")
    return "Hawaii Weather Stations"

@app.route("/api/v1.0/tobs")
def ftobs():
    print("Server received request for 'tobs' page...")
    return "Hawaii Dates and Recorded Temperatures"

@app.route("/api/v1.0/querytemps")
def fquerytemps():
    print("Server received request for 'querytemps' page...")
    return "Enter a date or date range for temperature statistics"

if __name__ == "__main__":
    app.run(debug=True)
