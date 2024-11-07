import React, { useState } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

function RegisterEmployee() {
  const [name, setName] = useState('');
  const [lastname, setLastname] = useState('');
  const [email, setEmail] = useState('');
  const [number, setNumber] = useState('');
  const [password, setPassword] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post(`${API_URL}/register`, {
        name,
        lastname,
        email,
        password,
        role: "Empleado",   // Fijo como "Empleado" según el ejemplo
        number,
        projects: [],       // Inicialmente vacío
        tasks: []           // Inicialmente vacío
      });
      setSuccessMessage('Empleado registrado exitosamente');
      setErrorMessage('');
      // Limpiar campos
      setName('');
      setLastname('');
      setEmail('');
      setDepartment('');
      setNumber('');
      setPassword('');
    } catch (error) {
      setErrorMessage(error.response?.data?.detail || 'Error al registrar empleado');
      setSuccessMessage('');
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-900 text-white">
      <div className="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
        <h2 className="text-3xl font-bold mb-6 text-center">Registrar Nuevo Empleado</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block mb-1 text-sm font-semibold">Nombre:</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
              className="w-full px-4 py-2 rounded bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div>
            <label className="block mb-1 text-sm font-semibold">Apellido:</label>
            <input
              type="text"
              value={lastname}
              onChange={(e) => setLastname(e.target.value)}
              required
              className="w-full px-4 py-2 rounded bg-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
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
            <label className="block mb-1 text-sm font-semibold">Teléfono:</label>
            <input
              type="tel"
              value={number}
              onChange={(e) => setNumber(e.target.value)}
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
            Registrar Empleado
          </button>
          {successMessage && <p className="mt-4 text-green-500">{successMessage}</p>}
          {errorMessage && <p className="mt-4 text-red-500">{errorMessage}</p>}
        </form>
      </div>
    </div>
  );
}

export default RegisterEmployee;
