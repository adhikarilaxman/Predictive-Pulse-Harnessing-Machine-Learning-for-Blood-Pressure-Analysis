import pandas as pd
import joblib
from flask import (
    Flask,
    url_for,
    render_template
)
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

import os
ml_model = None
ml_model_error = None
ml_model_path = "model.joblib"
if os.path.exists(ml_model_path):
    try:
        ml_model = joblib.load(ml_model_path)
    except Exception as err:
        ml_model_error = f"Custom Error: Could not load model due to: {str(err)}"
else:
    ml_model_error = f"Custom Error: Model file '{ml_model_path}' is missing. Please upload or train the model."



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home", welcome_message="Welcome to Predictive Pulse! Your personalized BP analysis tool.")


@app.route("/about")
def about():
    return "<h2>About Predictive Pulse</h2><p>This app was created by Laxman Adhikari for Smartbridge Internship Project AIML. It predicts hypertension stage using machine learning.</p>"



@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    form.Gender.choices = [("Male", "Male"), ("Female", "Female")]
    form.History.choices = [("Yes", "Yes"), ("No", "No")]
    form.Patient.choices = [("Yes", "Yes"), ("No", "No")]
    form.TakeMedication.choices = [("Yes", "Yes"), ("No", "No")]
    form.Severity.choices = [("Mild", "Mild"), ("Moderate", "Moderate"), ("Severe", "Severe")]
    form.BreathShortness.choices = [("Yes", "Yes"), ("No", "No")]
    form.VisualChanges.choices = [("Yes", "Yes"), ("No", "No")]
    form.NoseBleeding.choices = [("Yes", "Yes"), ("No", "No")]
    form.ControlledDiet.choices = [("Yes", "Yes"), ("No", "No")]

    if ml_model_error:
        message = ml_model_error
    elif form.validate_on_submit():
        gender_map = {"Male": 0, "Female": 1}
        history_map = {"No": 0, "Yes": 1}
        take_med_map = {"No": 0, "Yes": 1}
        severity_map = {"Mild": 0, "Moderate": 1, "Severe": 2}
        breath_short_map = {"No": 0, "Yes": 1}
        visual_changes_map = {"No": 0, "Yes": 1}
        nose_bleed_map = {"No": 0, "Yes": 1}
        controlled_diet_map = {"No": 0, "Yes": 1}
        whendiagnosed_map = {"<1 Year": 0, "1-5 Years": 1, ">5 Years": 2}
        systolic_map = {"100+": 0, "111-120": 1, "121-130": 2, "130+": 3}
        diastolic_map = {"70-80": 0, "81-90": 1, "91-100": 2, "100+": 3, "130+": 4}

        input_data = pd.DataFrame(dict(
            Gender=[gender_map.get(form.Gender.data, 0)],
            Age=[['18-34', '35-50', '51-64', '65+'].index(form.Age.data) if form.Age.data in ['18-34', '35-50', '51-64', '65+'] else 0],
            History=[history_map.get(form.History.data, 0)],
            Patient=[form.Patient.data],
            TakeMedication=[take_med_map.get(form.TakeMedication.data, 0)],
            Severity=[severity_map.get(form.Severity.data, 0)],
            BreathShortness=[breath_short_map.get(form.BreathShortness.data, 0)],
            VisualChanges=[visual_changes_map.get(form.VisualChanges.data, 0)],
            NoseBleeding=[nose_bleed_map.get(form.NoseBleeding.data, 0)],
            Whendiagnoused=[whendiagnosed_map.get(form.Whendiagnoused.data, 0)],
            Systolic=[systolic_map.get(form.Systolic.data, 0)],
            Diastolic=[diastolic_map.get(form.Diastolic.data, 0)],
            ControlledDiet=[controlled_diet_map.get(form.ControlledDiet.data, 0)]
        ))
        prediction = ml_model.predict(input_data)[0]
        message = f"[Predictive Pulse] Your predicted hypertension stage: {prediction}"
    else:
        message = "Please provide valid input details!"
    return render_template("predict.html", title="Predict", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True, port=10000)
