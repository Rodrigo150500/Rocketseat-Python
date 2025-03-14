from flask import Flask, jsonify, request, send_file, render_template
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta
from payment.pix import Pix
from flask_socketio import SocketIO
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEKY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)

socketio = SocketIO(app)


@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():

    data = request.get_json()

    if 'value' not in data:
        return jsonify({'message': 'Dados inválicos'}), 404

    expiration_date = datetime.now() + timedelta(minutes=30)


    createPayment = Payment(value = data['value'], 
                    expiration_date = expiration_date)

    pix_obj = Pix()
    data_pix = pix_obj.create_pix()
    
    createPayment.bank_payment_id = data_pix['bank_payment_id']
    createPayment.qr_code = data_pix['qr_code']
    
 
    db.session.add(createPayment)
    db.session.commit()

    return jsonify({"message":"The  payment has been creates",
                    "payment": createPayment.to_dict()})


@app.route('/payments/pix/qr_code/<fileName>', methods=['GET'])
def get_qr_code(fileName):
    return send_file(f'static/img/{fileName}.png', mimetype = 'image/png')

@app.route('/payments/pix/confirmation', methods = ['POST'])
def pix_confimation():

    data = request.get_json()

    if 'value' not in data and 'bank_payment_id' not in data:
        return jsonify({'message': 'Invalid payment'}), 400
    
    payment = Payment.query.filter_by(bank_payment_id = data.get('bank_payment_id')).first()

    if payment.paid or payment.value != data.get('value'):
        return jsonify({'message': 'Payment not found'}), 404

    payment.paid = True
    db.session.commit()

    socketio.emit(f'payment-confirmed-{payment.id}')
    return jsonify({"message": "The payment was confirmed"})


@app.route('/payments/pix/<payment_id>', methods = ['GET'])
def payment_pix_page(payment_id):

    paymentData = Payment.query.get(payment_id)

    if not paymentData:
        return render_template('404.html')

    if paymentData.paid:
        return render_template('confirmed_payment.html',
        payment_id= paymentData.id,
        value= paymentData.value
        )


    return render_template('payment.html', 
                            payment_id = paymentData.id, 
                            value = paymentData.value,
                            host = "http://127.0.0.1:5000",
                            qr_code = paymentData.qr_code)


#Websocket

@socketio.on('connect')
def handle_connect():
    print("Client connect")

@socketio.on('disconnect')
def handle_disconnect():
    print('Client has disconnected to the server')



if __name__ == '__main__':
    app.run(debug=True)