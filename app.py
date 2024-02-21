from flask import Flask, render_template, request, redirect

from logics.operations import Calculators
from models import db, PricesMaterials, CostWorks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecovatnik.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)


@app.route('/')
def calculator():
    calculator_list = PricesMaterials.query.all()
    return render_template('calculator.html', calculator=calculator_list)


@app.route("/calculate", methods=["POST"])
def calculate():
    # calculator_list = PricesMaterials.query.all()
    # if request.method == "POST":
    n1 = int(request.form['n1'])
    n2 = int(request.form['n2'])
    calc = Calculators(n1, n2)
    volume = calc.volume_calculate
    data = {'volume': volume}
    return render_template('result_page.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
