import React, { useState } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    
    try {
      // Enviar solicitud con formato form-encoded
      const formData = new URLSearchParams();
      formData.append('username', email);
      formData.append('password', password);

      const response = await axios.post(`${API_URL}/login`, formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });

      // DEBUG: Ver la respuesta completa
      console.log("Respuesta completa:", response);

      if (response.status === 200 && response.data.access_token) {
        // Guardar el token en el local storage
        localStorage.setItem('token', response.data.access_token);
        localStorage.setItem('role', response.data.role);
         // Redirigir según el rol del usuario
        const userRole = response.data.role;
        if (userRole === 'Admin') {
          navigate('/admin-dashboard');
        } else if (userRole === 'Gerente') {
          navigate('/manager-dashboard');
        } else if (userRole === 'Líder') {
          navigate('/leader-dashboard');
        } else if (userRole === 'Empleado') {
          navigate('/employee-dashboard');
        }
        setErrorMessage('');
        alert('Inicio de sesión exitoso');
        // Aquí podrías redirigir al usuario a otra página o actualizar el estado de autenticación
      } else {
        // Si no hay token o status 200, mostrar error
        setErrorMessage('Email o contraseña incorrectos');
      }
      
    } catch (error) {
      // DEBUG: Ver el error completo
      console.error("Error completo:", error);

      // Verificar si es un error de autenticación o de red
      if (error.response && error.response.status === 401) {
        setErrorMessage('Email o contraseña incorrectos');
      } else {
        setErrorMessage('Hubo un problema al intentar iniciar sesión');
      }
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-900 text-white">
      <div className="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
        <h2 className="text-3xl font-bold mb-6 text-center">Iniciar Sesión</h2>
        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block mb-1 text-sm font-semibold">Email:</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="w-full px-4 py-2 rounded bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div>
            <label className="block mb-1 text-sm font-semibold">Contraseña:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full px-4 py-2 rounded bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <button
            type="submit"
            className="w-full py-2 mt-4 bg-blue-600 hover:bg-blue-700 rounded text-white font-semibold"
          >
            Iniciar Sesión
          </button>
          {errorMessage && <p className="mt-4 text-red-500">{errorMessage}</p>}
        </form>
      </div>
    </div>
  );
}

export default LoginPage;
