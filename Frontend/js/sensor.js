class Sensor {
    constructor(id, name, parameter) {
      this.id = id;
      this.name = name;
      this.parameter = parameter;
      this.value = 0;
      this.minValue = 0;
      this.maxValue = 100;
    }
  
    setValue(value) {
      this.value = value;
      if (this.value < this.minValue || this.value > this.maxValue) {
        this.sendAlert();
      }
    }
  
    sendAlert() {
      const message = `Sensor ${this.name} com valor ${this.value} fora do limite`;
      console.log(message);
      // Enviar mensagem para o Broker
      fetch('/api/alert', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          topic: this.parameter,
          message: message
        })
      });
    }
  }
  
  const sensors = [
    new Sensor(1, "Temperatura", "temperatura"),
    new Sensor(2, "Umidade", "umidade"),
    new Sensor(3, "Velocidade", "velocidade")
  ];
  
  const sensorList = document.getElementById("sensors");
  sensors.forEach(sensor => {
    const li = document.createElement("li");
    li.textContent = `${sensor.name} - ${sensor.parameter}`;
    sensorList.appendChild(li);
  });