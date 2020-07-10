from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
	return '''
<html>
	<head>
		<title> Home Page</title> 
	</head>
	<body>
		<h1> Welcome to the Climate App</h1>
		<h3> The following links are available</h3>
		<ul>
				<li><a href=/api/v1.0/precipitation>Percipitation Information</a></li>
				<li><a href=/api/v1.0/stations>Station Information</a></li>
				<li><a href=/api/v1.0/tobs>TOBS(Forget what this means)</a></li>
		</ul>
	</body> 
</html> '''

@app.route('/api/v1.0/precipitation')
def perciptation():
	return '''
<html>
	<head>
		<title>Percipitation Page</title> 
	</head> 
	<body> 
		<h1>Welcome to the Percipition Page</h1> 
	</body> 
</html> '''

@app.route('/api/v1.0/stations')
def stations(): 
	return ''' 

<html> 
	<head>
		<title>Stations Page</title> 
	<head>
	<body> 
		<h1>Welcome to the Stations Page</h1>
	</body> 
</html> '''

@app.route('/api/v1.0/tobs')
def tobs(): 
	return '''
<html>
	<head>
		<title>TOBS Page</title> 
	</head>
	<body> 
		<h1>Welcome to the TOBS Page</h1> 
	</body> 
</html>'''



if __name__ == "__main__": 
	app.run(debug=True)