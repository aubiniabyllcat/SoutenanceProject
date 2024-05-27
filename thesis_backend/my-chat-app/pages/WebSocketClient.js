class WebSocketClient {
    constructor(channelSlug) {
      this.channelSlug = channelSlug;
      this.websocket = null;
    }
  
    connect() {
      // Ouvrir une connexion WebSocket
      const wsUrl = `wss://example.com/chat/${this.channelSlug}`;
      this.websocket = new WebSocket(wsUrl);
  
      // Définir les gestionnaires d'événements
      this.websocket.onopen = () => {
        console.log('WebSocket connected');
      };
  
      this.websocket.onmessage = (event) => {
        console.log('Message received:', event.data);
        // Appeler le callback défini pour gérer les messages entrants
        if (this.onMessageCallback) {
          this.onMessageCallback(event.data);
        }
      };
  
      this.websocket.onerror = (error) => {
        console.error('WebSocket error:', error);
      };
  
      this.websocket.onclose = () => {
        console.log('WebSocket closed');
      };
    }
  
    sendMessage(message) {
      // Vérifier si la connexion WebSocket est ouverte
      if (this.websocket && this.websocket.readyState === WebSocket.OPEN) {
        // Envoyer le message
        this.websocket.send(message);
      } else {
        console.error('WebSocket is not open. Cannot send message.');
      }
    }
  
    onMessage(callback) {
      // Définir le callback pour gérer les messages entrants
      this.onMessageCallback = callback;
    }
  
    disconnect() {
      // Fermer la connexion WebSocket
      if (this.websocket) {
        this.websocket.close();
      }
    }
  }
  
  export default WebSocketClient;
  