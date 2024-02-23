from flask import Flask, render_template, request, url_for

from common.constants import MaterialsPrices, WorksPrices
from logics.calculator import Calculators
from db.models import db, Materials

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecovatnik.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)


@app.route('/')
def calculator():
    calculator_list = Materials.query.all()
    return render_template('calculator.html', calculator=calculator_list)


@app.route("/calculate", methods=["POST"])
def calculate():
    # eco_price_per_package = Materials.query.get(1).price  # TODO Nujna li basa voobshe????
    # cost_work_per_kg = Works.query.get(1).costs  # TODO Nujna li basa voobshe????
    eco_price_per_package = MaterialsPrices.ECOVATA
    cost_work_per_kg = WorksPrices.ECOVATA_MONTAJ
    # TODO query.get устаревшие методы перейти на 2.0  https://docs.sqlalchemy.org/en/14/changelog/migration_20.html
    # if request.method == "POST":
    sqr = int(request.form['sqr'])
    width = int(request.form['width'])
    data = {"sqr": sqr, "width": width}
    calc = Calculators(sqr, width)
    volume = calc.volume_calculate
    ves = calc.ves_calculate
    packages_count = calc.packages_count_calculate
    eco_price = calc.ecovata_price_calculate(eco_price_per_package)
    cost_work = calc.cost_work_calculate(cost_work_per_kg)
    materials_data = calc.get_materials_data()
    works_data = calc.get_works_data()
    data.update(
        {
        'volume': volume,
        'ves': ves,
        'packages_count': packages_count,
        'eco_price': eco_price,
        'cost_work': cost_work,
        }
    )
    data.update(materials_data)
    data.update(works_data)
    return render_template('result_page.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)
