class Client {
    constructor(id, name) {
      this.id = id;
      this.name = name;
      this.topics = [];
    }
  
    subscribe(topic) {
      this.topics.push(topic);
      console.log(`Cliente ${this.name} assinou o tópico ${topic}`);
      // Enviar requisição para o Broker para se inscrever no tópico
      fetch('/api/subscribe', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          topic: topic,
          clientId: this.id
        })
      });
    }
  
    receiveMessage(message) {
      console.log(`Cliente ${this.name} recebeu a mensagem ${message}`);
    }
  }
  
  const clients = [
    new Client(1, "Cliente 1"),
    new Client(2, "Cliente 2"),
    new Client(3, "Cliente 3")
  ];
  
  const clientList = document.getElementById("clients");
  clients.forEach(client => {
    const li = document.createElement("li");
    li.textContent = client.name;
    clientList.appendChild(li);
  });