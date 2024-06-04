"use client"
import { useState } from 'react';
import { useRouter } from "next/navigation";
const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!username || !password) {
      console.error('Veuillez entrer un nom d\'utilisateur et un mot de passe.');
      return;
    }

    const formData = {
      username: username,
      password: password
    };

    console.log('FormData:', formData);

    try {
      const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      const responseData = await response.json();

      if (response.ok) {
        console.log('Login successful:', responseData);
        localStorage.setItem('accessToken', responseData.access_token);
        router.push('/profile');
      } else {
        console.error('Login failed:', response.statusText);
        console.error('Response body:', responseData);
      }
    } catch (error) {
      console.error('An error occurred during login:', error);
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;