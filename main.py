import calculator as calc
from flask import Flask, render_template,request,redirect,url_for
from forms import CalculatorForm
from data import weekday


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


@app.route("/", methods=["GET","POST"])
def calculator():
    form = CalculatorForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Do calculations with form data
        start = form.start.data
        finish = form.finish.data
        num_of_ppl = form.num_of_ppl.data
        result = None
        if weekday < 6 and num_of_ppl > 1:
            result=calc.week_price_bands(num_of_ppl,start,finish)
        elif weekday < 6 and num_of_ppl == 1:
            result=calc.week_price_solo(num_of_ppl,start,finish)
        elif weekday > 5 and num_of_ppl ==1:
            result=calc.weekend_solo(start, finish)
        elif weekday > 5 and num_of_ppl > 1:
            result=calc.weekend_bands(num_of_ppl, start, finish)
        if result:
            hourly = result / (finish-start)
            return render_template('index.html', form=form, result=result, hourly=hourly)
    return render_template('index.html', form=form)



while __name__ == "__main__":
    app.run(debug=True)