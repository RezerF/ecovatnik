from flask import Flask, render_template, request, redirect
from models import db, PricesMaterials

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
    n1 = int(request.form['n1'])
    n2 = int(request.form['n2'])
    result = n1 * n2
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
