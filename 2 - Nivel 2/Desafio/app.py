from flask import Flask, request, jsonify
from database import db
from models.meal import Meal


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/meal-diet'

db.init_app(app)


#Criar refeição
@app.route('/meal', methods=['POST'])
def createMeal():
  data = request.json

  if data:   
    name = data.get('name')
    description = data.get('description')
    dateTime = data.get('dateTime')
    isDiet = data.get('isDiet')

    meal = Meal(name=name, description=description, dateTime=dateTime, isDiet=isDiet)

    db.session.add(meal)
    db.session.commit()


    return jsonify({'message': 'Refeição cadastrada com sucesso'})

  else:
     return jsonify({'message':'Dados não encontrados'}), 404

#Ler todas as refeições
@app.route('/meal', methods=['GET'])
def readMeals():
  
  meals = Meal.query.all()

  if meals:
     return jsonify({'message': [meal.to_dict() for meal in meals]})
  
  return jsonify({'message': 'Refeições não encontradas'}), 404

#Ler refeição uma refeição




#Editar refeição


#Deletar refeição





with app.app_context():
    db.create_all()

if(__name__) == '__main__':
  app.run(debug=True)
