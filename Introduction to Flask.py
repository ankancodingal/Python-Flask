# Calculate Age with Flask
from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")  # This serves the HTML form.
@app.route("/calculate", methods=["POST"])
def calculate_age():
    try:
        # Fetch the birth year from the form
        birth_year = int(request.form.get("birth_year"))

        # Get the current year
        current_year = datetime.now().year

        # Validate the birth year
        if birth_year > current_year or birth_year < 1900:
            return render_template("index.html", error="Please enter a valid year (1900 - current year).")

        # Calculate age
        age = current_year - birth_year

        # Pass the age to the template
        return render_template("index.html", age=age)

    except ValueError:
        # Handle non-integer input
        return render_template("index.html", error="Please enter a valid number.")
if __name__ == "__main__":
    app.run(debug=True)

#--------------------------------Check leap year-------------------------
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/" , methods=['POST' , 'GET'])

def leapyear():
	msg = ''
	if request.method == 'POST' and 'input_year' in request.form:
		Input_year = int(request.form.get('input_year'))
		if (Input_year % 4) == 0:
			if (Input_year % 100) == 0:
				if (Input_year % 400) == 0:
					msg = '{0} is a Leap year'.format(Input_year)
				else: 
					msg = '{0} is Not a Leap year'.format(Input_year)
			else: 
				msg = '{0} is a Leap year'.format(Input_year)
		else:
			msg = '{0} is Not a Leap year'.format(Input_year)
	
	return render_template("index.html",msg=msg)	

@app.route('/')
def index():
	return render_template('index.html')


app.run(host='0.0.0.0', port=8080)
