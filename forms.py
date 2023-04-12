from flask_wtf import FlaskForm
from wtforms import ValidationError, SubmitField, IntegerField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
        start = IntegerField("Start Time:", validators=[DataRequired()])
        finish = IntegerField("Finish Time:", validators=[DataRequired()])
        num_of_ppl = IntegerField("Num of People:", validators=[DataRequired()])
        submit = SubmitField("Calculate", render_kw={"class": "btn btn-light btn-lg"})

