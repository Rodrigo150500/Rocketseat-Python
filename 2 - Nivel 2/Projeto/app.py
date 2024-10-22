from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, current_user, login_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)


@app.route('/login', methods=['POST'])
def login():

    data = request.json

    username = data.get('username')
    password = data.get('password')

    if username and password:       

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            
            print(current_user.username.is_authenticated)
            return jsonify({'message':'Usuário credenciado'})
       


    return jsonify({'message':'Usuario não encontrado'}), 400


   
@app.route('/hello-world', methods=['GET'])
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)