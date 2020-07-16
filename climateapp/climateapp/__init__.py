										###############################################
										#    This is the init file for the web app    #
										#    Export the enviornment variable to run   #
										#	                                          #
										#	 windows								  #
										#		set FLASK_APP=climateapp			  #
										#		set export FLASK_ENV=development	  #
										#	non windows								  #
										#  	    export FLASK_APP=climateapp 		  #
										#		export export FLASK_ENV=development	  #
										#											  #
										# 	 pip install -e . 						  #
										# 											  #
										#    flask run  							  #
										###############################################

from flask import Flask
app = Flask(__name__)

from climateapp import routes