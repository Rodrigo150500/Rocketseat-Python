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
@app.route('/meal/<int:id>', methods=['GET'])
def readMeal(id):

  meal = Meal.query.get(id)

  if meal:
    return jsonify({'message': meal.to_dict()})
  
  return jsonify({'message':f"A refeição com id {id} não foi encontrada"}), 404

#Editar refeição

@app.route('/meal/<int:id>', methods=['PUT'])
def updateMeal(id):

  data = request.json

  if data:
    name = data.get('name')
    description = data.get('description')
    dateTime = data.get('dateTime')
    isDiet = data.get('isDiet')
    
    meal = Meal.query.get(id)

    meal.name = name
    meal.description = description
    meal.dateTime = dateTime
    meal.isDiet = isDiet

    db.session.commit()
    
    return jsonify({'message': 'Refeição atualizada com sucesso'})


  return jsonify({'message':'Dados não encontrados'}), 404
  

#Deletar refeição
@app.route('/meal/<int:id>', methods = ['DELETE'])
def deleteMeal(id):
  meal = Meal.query.get(id)

  if meal:
    db.session.delete(meal)
    db.session.commit()
    return jsonify({"message":"Refeição deletada"})

  return jsonify({"message":f"A refeição com id {id} não foi encontrada"}), 404



with app.app_context():
    db.create_all()

if(__name__) == '__main__':
  app.run(debug=True)
