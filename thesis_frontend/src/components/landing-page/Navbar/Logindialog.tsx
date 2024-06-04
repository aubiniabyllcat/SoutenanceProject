"use client";

import { Dialog, Transition } from '@headlessui/react'
import { Fragment, useState } from 'react'
import { X } from 'lucide-react';
import Link from 'next/link';
import Image from 'next/image';
import { useRouter } from 'next/navigation'

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleLogin = async (e: { preventDefault: () => void; }) => {
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
        router.push('/dashboard'); // Redirection vers le dashboard
      } else {
        console.error('Login failed:', response.statusText);
        console.error('Response body:', responseData);
      }
    } catch (error) {
      console.error('An error occurred during login:', error);
    }
  };



  return (
    <>
      <div className="font-[sans-serif] text-[#333]">
        <div className="min-h-screen flex flex-col items-center justify-center">
          <div className="grid md:grid-cols-2 items-center gap-4 max-w-6xl w-full p-4 m-4 shadow-[0_2px_10px_-3px_rgba(6,81,237,0.3)] rounded-md">
            <div className="md:max-w-md w-full sm:px-6 py-4">
              <form onSubmit={handleLogin}>
                <div className="mb-12">
                  <h3 className="text-3xl font-extrabold">Connexion </h3>
                </div>
                <div>
                  <label className="text-xs block mb-2">Login</label>
                  <div className="relative flex items-center">
                    <input
                      name="login"
                      type="text"
                      className="w-full text-sm border-b border-gray-300 focus:border-[#333] px-2 py-3 outline-none"
                      placeholder="Entrez votre login"
                      value={username}
                      onChange={(e) => setUsername(e.target.value)}
                    />
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="#bbb"
                      stroke="#bbb"
                      className="w-[18px] h-[18px] absolute right-2"
                      viewBox="0 0 682.667 682.667"
                    >
                      {/* SVG code */}
                    </svg>
                  </div>
                </div>
                <div className="mt-8">
                  <label className="text-xs block mb-2">Password</label>
                  <div className="relative flex items-center">
                    <input
                      name="password"
                      type="password"
                      className="w-full text-sm border-b border-gray-300 focus:border-[#333] px-2 py-3 outline-none"
                      placeholder="Entrez votre mot de passe"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                    />
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="#bbb"
                      stroke="#bbb"
                      className="w-[18px] h-[18px] absolute right-2 cursor-pointer"
                      viewBox="0 0 128 128"
                    >
                      {/* SVG code */}
                    </svg>
                  </div>
                </div>
                <div className="flex items-center justify-between gap-2 mt-5">
                  <div className="flex items-center">
                    <input
                      id="remember-me"
                      name="remember-me"
                      type="checkbox"
                      className="h-4 w-4 shrink-0 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                    />
                    <label htmlFor="remember-me" className="ml-3 block text-sm">
                      Me rappeler
                    </label>
                  </div>
                  <div>
                    <a
                      href="jajvascript:void(0);"
                      className="text-blue-600 font-semibold text-sm hover:underline"
                    >
                      Mot de passe oublié?
                    </a>
                  </div>
                </div>
                <div className="mt-12">
                  <button
                    type="submit"
                    className="w-full shadow-xl py-2.5 px-4 text-sm font-semibold rounded-full text-white bg-blue-600 hover:bg-blue-700 focus:outline-none"
                  >
                    Valider
                  </button>
                </div>
                <p className="my-8 text-sm text-gray-400 text-center">
                  ou continuer avec
                </p>
                <div className="space-x-8 flex justify-center">
                  <button type="button" className="border-none outline-none">
                    {/* SVG code for Google icon */}
                  </button>
                  <button type="button" className="border-none outline-none">
                    {/* SVG code for Facebook icon */}
                  </button>
                </div>
              </form>
            </div>
            <div className="md:h-full w-full max-md:mt-10 bg-white rounded-xl lg:p-12 p-8">
              <Image src="/images/Login/imgLogin.png" alt="nothing" width={1000} height={1} />
            </div>
          </div>
        </div>
      </div>
    </>
  )
};
export default Login;