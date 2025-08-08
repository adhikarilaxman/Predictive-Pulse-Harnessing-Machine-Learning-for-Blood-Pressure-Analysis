from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    Gender = SelectField(
        label="Gender",
        choices=[('Male', 'Male'), ('Female', 'Female')],
        validators=[DataRequired()]
    )
    Age = SelectField(
        label="Age Group",
        choices=[('18-34', '18-34'), ('35-50', '35-50'), ('51-64', '51-64'), ('65+', '65+')],
        validators=[DataRequired()]
    )
    History = SelectField(
        label="History",
        choices=[('Yes', 'Yes'), ('No', 'No')],
        validators=[DataRequired()]
    )
    Patient = StringField(
        label="Patient ID",
        validators=[DataRequired()]
    )
    TakeMedication = SelectField(
        label="Take Medication",
        choices=[('Yes', 'Yes'), ('No', 'No')],
        validators=[DataRequired()]
    )
    Severity = SelectField(
        label="Severity",
        choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')],
        validators=[DataRequired()]
    )
    BreathShortness = SelectField(
        label="Breath Shortness",
        choices=[('Yes', 'Yes'), ('No', 'No')],
        validators=[DataRequired()]
    )
    VisualChanges = SelectField(
        label="Visual Changes",
        choices=[('Yes', 'Yes'), ('No', 'No')],
        validators=[DataRequired()]
    )
    NoseBleeding = SelectField(
        label="Nose Bleeding",
        choices=[('Yes', 'Yes'), ('No', 'No')],
        validators=[DataRequired()]
    )
    Whendiagnoused = SelectField(
        label="When Diagnosed",
        choices=[('<1 Year', '<1 Year'), ('1-5 Years', '1-5 Years'), ('>5 Years', '>5 Years')],
        validators=[DataRequired()]
    )
    Systolic = SelectField(
        label="Systolic (mmHg)",
        choices=[('100+', '100+'), ('111-120', '111-120'), ('121-130', '121-130'), ('130+', '130+')],
        validators=[DataRequired()]
    )
    Diastolic = SelectField(
        label="Diastolic (mmHg)",
        choices=[('70-80', '70-80'), ('81-90', '81-90'), ('91-100', '91-100'), ('100+', '100+'), ('130+', '130+')],
        validators=[DataRequired()]
    )
    ControlledDiet = SelectField(
        label="Controlled Diet",
        choices=[('Yes', 'Yes'), ('No', 'No')],
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")
