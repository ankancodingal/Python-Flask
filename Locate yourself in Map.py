# Location map with Flask
from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Initialize Nominatim geolocator (OpenStreetMap)
geolocator = Nominatim(user_agent="locate_me_app")

# Route to serve the main page
@app.route("/")
def home():
	return render_template("index.html")

# Geocoding route to fetch latitude and longitude
@app.route("/geocode", methods=["POST"])
def geocode():
	location = request.json.get("location")
	if not location:
		return jsonify({"error": "Location is required"}), 400

	# Geocoding using Geopy (OpenStreetMap)
	location = geolocator.geocode(location)
	if location:
		return jsonify({
			"latitude": location.latitude,
			"longitude": location.longitude,
			"display_name": location.address
		})
	else:
		return jsonify({"error": "Location not found"}), 404

if __name__ == "__main__":
	app.run(debug=True)
#------------------------------------BMI Calculator--------------------------
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculate" , methods=['POST' , 'GET'])

def calculate():
	bmi=''
	if request.method == 'POST' and 'Weight' in request.form and 'Height' in request.form:
		weight = float(request.form.get('Weight'))
		height = float(request.form.get('Height'))
		bmi = round(weight/((height/100)**2),2)
	return render_template("index.html",bmi=bmi)	

@app.route('/')
def index():
	return render_template('index.html')


app.run(host='0.0.0.0', port=8080)
