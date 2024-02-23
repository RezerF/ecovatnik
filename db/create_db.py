from flask import Flask
from models import Materials, Works, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecovatnik.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        # создаем прайс материалов
        good1 = Materials(title='Ecovata', price=1080)
        good2 = Materials(title='Эковата', price=1080)
        good3 = Materials(title='Брус', price=1)
        db.session.add_all([good1, good2, good3])
        db.session.commit()

        # создаем стоимость работ
        work1 = Works(work_name='МонтажЭковаты', costs=22)
        work2 = Works(work_name='ОбустройствоОбрешетки', costs=1)
        work3 = Works(work_name='МонтажПароизоляции', costs=1)
        db.session.add_all([work1, work2, work3])
        db.session.commit()

