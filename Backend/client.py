import paho.mqtt.client as mqtt

class Client:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.topics = []
    self.client = mqtt.Client()
    self.client.connect("localhost", 1883)

  def subscribe(self, topic):
    self.topics.append(topic)
    self.client.subscribe(topic)

  def receiveMessage(self, topic, message):
    print(f"Cliente {self.name} recebeu a mensagem {message} no tópico {topic}")

clients = [
  Client(1, "Cliente 1"),
  Client(2, "Cliente 2"),
  Client(3, "Cliente 3")
]