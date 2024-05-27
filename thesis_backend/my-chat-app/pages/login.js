import { useState } from 'react';
import { useRouter } from 'next/router';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleLogin = async (e) => {
    e.preventDefault();

    if (!username || !password) {
      console.error('Veuillez entrer un nom d\'utilisateur et un mot de passe.');
      return;
    }

    const formData = {
      username: username, 
      password: password, 
    };

    console.log('FormData:', formData);

    try {
      const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      const responseData = await response.json();

      if (response.ok) {
        console.log('Connexion réussie:', responseData);
        localStorage.setItem('accessToken', responseData.access_token);
         
        console.log(localStorage.getItem('accessToken'));

        
        
        router.push('/updateprofile');
      } else {
        console.error('Échec de la connexion:', response.statusText);
        console.error('Corps de la réponse:', responseData);
      }
    } catch (error) {
      console.error('Une erreur est survenue lors de la connexion:', error);
    }
  };

  return (
    <div>
      <h1>Connexion</h1>
      <form onSubmit={handleLogin}>
        <div>
          <label htmlFor="username">Nom d'utilisateur:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="password">Mot de passe:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Connexion</button>
      </form>
    </div>
  );
};

export default Login;
