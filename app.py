from flask import Flask, request, render_template
from twilio.rest import Client

app = Flask(__name__)

# Your Twilio credentials
account_sid = 'AC15c497ec3f576a16b2dafa6810a94348'
auth_token = '4a751c566fc8c2c0fc04bf3dc216f278'
client = Client(account_sid, auth_token)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    message_body = request.form.get('message')
    to_number = '+14153235858'  # Replace with the recipient's phone number

    # Send the SMS
    message = client.messages.create(
        from_='+18885016651',
        body=message_body,
        to=to_number
    )

    return f"SMS sent with SID: {message.sid}"

if __name__ == '__main__':
    app.run(debug=True)
