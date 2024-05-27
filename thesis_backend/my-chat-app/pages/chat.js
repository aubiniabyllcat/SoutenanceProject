import React, { useState, useEffect } from 'react';
import MessageBubble from './MessageBubble';

const Chat = ({ channelSlug }) => {
  const [socket, setSocket] = useState(null);
  const [messages, setMessages] = useState([]);
  const [messageInput, setMessageInput] = useState('');

  useEffect(() => {
    const newSocket = new WebSocket(`ws://localhost:8000/messages/ws/{channel_slug}`);
    setSocket(newSocket);

    newSocket.onopen = () => {
      console.log('WebSocket connection established.');
    };

    newSocket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setMessages((prevMessages) => [...prevMessages, message]);
    };

    return () => {
      newSocket.close();
    };
  }, [channelSlug]);

  const sendMessage = () => {
    if (socket && messageInput.trim() !== '') {
      socket.send(JSON.stringify({ text: messageInput, sentBy: 'currentUser' }));
      setMessageInput('');
    }
  };

  return (
    <div>
      {messages.map((msg, index) => (
        <MessageBubble
          key={index}
          message={msg.text}
          isSentByCurrentUser={msg.sentBy === 'currentUser'}
        />
      ))}
      <input
        type="text"
        value={messageInput}
        onChange={(e) => setMessageInput(e.target.value)}
        placeholder="Type your message here..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Chat;
