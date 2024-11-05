from flask import Flask
from database import db
from models.meal import Meal


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/meal-diet'

db.init_app(app)


with app.app_context():
    db.create_all()

if(__name__) == '__main__':
  app.run(debug=True)
