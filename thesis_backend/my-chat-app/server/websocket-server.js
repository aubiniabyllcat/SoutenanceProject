const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8000 });

wss.on('connection', function connection(ws) {
  console.log('New WebSocket connection established.');

  ws.on('message', function incoming(message) {
    console.log('Received message:', message);
    // Vous pouvez ajouter votre logique de gestion des messages ici
  });
});
