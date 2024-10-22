from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance/database.db')

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
            print(current_user.is_authenticated)
            return jsonify({'message':'Usuário credenciado'})

    return jsonify({'message':'Usuário não encontrado'}), 400


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Usuário deslogado com sucesso'})

@app.route('/hello-world', methods=['GET'])
def hello_world():
    return "Hello world"


# Cria as tabelas ao iniciar a aplicação
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
