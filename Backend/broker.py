import paho.mqtt.client as mqtt
from flask import Flask, request, jsonify

app = Flask(__name__)


MQTT_BROKER_HOST = 'localhost'
MQTT_BROKER_PORT = 1883


client = mqtt.Client()
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

#receber mensagens de alerta dos sensores
@app.route('/api/alert', methods=['POST'])
def receive_alert():
    data = request.get_json()
    topic = data['topic']
    message = data['message']
    client.publish(topic, message)
    return jsonify({'message': 'Mensagem de alerta recebida com sucesso'})

#inscrever em um tópico
@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    topic = data['topic']
    client_id = data['clientId']
    client.subscribe(topic)
    return jsonify({'message': 'Inscrição no tópico realizada com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)