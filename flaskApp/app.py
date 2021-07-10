from flask import Flask, render_template, request, redirect
import joblib

app = Flask(__name__)

classifier = joblib.load('/home/tanveer/pythonProjects/diabetesPrediction/classifier.pkl')
parameters = []

@app.route("/", methods=["GET", "POST"])
def homePage():
	global parameters
	if request.method == "GET":
		return render_template("homePage.html")
	else:
		pregnancies = request.form.get("pregnancies")
		glucose = request.form.get("glucose")
		bloodPressure = request.form.get("bloodPressure")
		skinThickness = request.form.get("skinThickness")
		insulin = request.form.get("insulin")
		BMI = request.form.get("BMI")
		diabetesPedigreeFunction = request.form.get("diabetesPedigreeFunction")
		age = request.form.get("age")

		parameters = [[pregnancies, glucose, bloodPressure, skinThickness, insulin, BMI, diabetesPedigreeFunction, age]]

		return redirect("/prediction")

@app.route("/prediction")
def predictionPage():
	global parameters
	global classifier
	result = classifier.predict(parameters)
	if result == [0]:
		diabetes = "Yes"
	else:
		diabetes = "No"
	return render_template("predictionPage.html", diabetes=diabetes)