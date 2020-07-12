from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

engine = create_engine('sqlite:///Resources/hawaii.sqlite')

Base = automap_base()
Base.prepare(engine,reflect=True)

Measurements = Base.classes.measurement
Stations = Base.classes.station

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/api/v1.0/precipitation')
def perciptation():
	session = Session(engine)

	lastDate = session.query(Measurements.date).order_by(Measurements.date.desc()).first()

	for row in lastDate: 
		date = dt.datetime.strptime(row,"%Y-%m-%d")

	sel = [Measurements.date,
		   func.sum(Measurements.prcp)]

	data = session.query(*sel).filter(func.strftime("%Y-%m-%d)", Measurements.date) >= str((date - dt.timedelta(days=365)))).\
					group_by(Measurements.date).all()

	session.close()

	returnList = []

	for row in data: 
		dateDict = {}
		dateDict["date"] = row.date 
		dateDict["prcp"] = row[1]
		returnList.append(dateDict)

	return jsonify(returnList)

@app.route('/api/v1.0/stations')
def stations(): 
	session = Session(engine)

	data = session.query(Stations.station, Stations.name).all()
	session.close()

	returnList = [] 

	for row in data: 
		stationDict = {}
		stationDict["station"] = row.station 
		stationDict["name"] = row.name
		returnList.append(stationDict)

	return jsonify(returnList)

@app.route('/api/v1.0/tobs')
def tobs(): 
	session = Session(engine)
	sel = [Stations.station,
		   func.count(Measurements.station)]

	rankedStations = session.query(*sel).filter(Measurements.station == Stations.station).\
						group_by(Measurements.station).order_by(func.count(Measurements.station).desc()).first()
	
	for row in rankedStations:
		bestId = rankedStations.station
	
	sel = [Stations.station,
		   func.min(Measurements.tobs),
		   func.max(Measurements.tobs),
		   func.avg(Measurements.tobs)
	]

	data = session.query(*sel).\
					filter(Measurements.station == Stations.station).\
					filter(Stations.station == bestId).all()
	returnList = []
	for row in data: 
		tobsDict = {}
		tobsDict["station"] = row.station
		tobsDict["min"] = row[1]
		tobsDict["max"] = row[2]
		tobsDict["avg"] = row[3]
		returnList.append(tobsDict)
	return jsonify(returnList)

if __name__ == "__main__": 
	app.run(debug=True)