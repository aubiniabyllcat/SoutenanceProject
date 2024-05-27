// MessageBubble.js
import React from 'react';

const MessageBubble = ({ text, sentByCurrentUser }) => {
  return (
    <div className={`message-bubble ${sentByCurrentUser ? 'sent' : 'received'}`}>
      {text}
    </div>
  );
};

export default MessageBubble;
