import paho.mqtt.client as mqtt

class Sensor:
  def __init__(self, id, name, parameter):
    self.id = id
    self.name = name
    self.parameter = parameter
    self.value = 0
    self.minValue = 0
    self.maxValue = 100
    self.client = mqtt.Client()
    self.client.connect("localhost", 1883)

  def sendAlert(self):
    message = f"Sensor {self.name} com valor {self.value} fora do limite"
    self.client.publish(f"{self.parameter}/alert", message)

sensors = [
  Sensor(1, "Temperatura", "temperatura"),
  Sensor(2, "Umidade", "umidade"),
  Sensor(3, "Velocidade", "velocidade")
]