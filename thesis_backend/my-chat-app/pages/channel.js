import { useState } from 'react';
import { useRouter } from 'next/router';

const CreateChannel = () => {
  const [channelName, setChannelName] = useState('');
  const [channelDescription, setChannelDescription] = useState('');
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = {
      channel_name: channelName,
      describe_info: channelDescription
      // Ajoutez d'autres champs si nécessaire
    };

    try {
      console.log(JSON.stringify(formData))
      const response = await fetch('http://127.0.0.1:8000/channels', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
        
      });

      const responseData = await response.json();

      if (response.ok) {
        console.log('Channel successful:', responseData);
        //localStorage.setItem('accessToken', responseData.access_token);
        router.push('/profile');
      } else {
        console.error('Channel failed:', response.statusText);
        console.error('Response body:', responseData);
      }
    } catch (error) {
      console.error('An error occurred during Channel:', error);
    }
  };

  return (
    <div>
      <h1>Create Channel</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="channelName">Name:</label>
          <input
            type="text"
            id="channelName"
            value={channelName}
            onChange={(e) => setChannelName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="channelDescription">Description:</label>
          <textarea
            id="channelDescription"
            value={channelDescription}
            onChange={(e) => setChannelDescription(e.target.value)}
          />
        </div>
        <button type="submit">Create Channel</button>
      </form>
    </div>
  );
};

export default CreateChannel;
