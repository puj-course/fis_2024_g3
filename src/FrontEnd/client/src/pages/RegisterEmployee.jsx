import React, { useState } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000'; 

function RegisterEmployee() {
  const [name, setName] = useState('');
  const [lastname, setLastname] = useState('');
  const [email, setEmail] = useState('');
  const [department, setDepartment] = useState('');
  const [number, setNumber] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const generatePassword = () => {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let password = '';
    for (let i = 0; i < 8; i++) {
      password += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return password;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const password = generatePassword();

    try {
      await axios.post(`${API_URL}/register`, {
        name,
        lastname,
        email,
        password,
        number,
        role: 'empleado', 
        department
      });
      setSuccessMessage('Empleado registrado exitosamente');
      setErrorMessage('');
      setName('');
      setLastname('');
      setEmail('');
      setDepartment('');
      setNumber('');
    } catch (error) {
      setErrorMessage('Error al registrar empleado');
      setSuccessMessage('');
    }
  };

  return (
    <div className="register-employee-container">
      <h2>Registrar Nuevo Empleado</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label>Nombre:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            className="text-black"
          />
        </div>
        <div>
          <label>Apellido:</label>
          <input
            type="text"
            value={lastname}
            onChange={(e) => setLastname(e.target.value)}
            required
            className="text-black"
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="text-black"
          />
        </div>
        <div>
          <label>Departamento:</label>
          <input
            type="text"
            value={department}
            onChange={(e) => setDepartment(e.target.value)}
            required
            className="text-black"
          />
        </div>
        <div>
          <label>Teléfono:</label>
          <input
            type="tel"
            value={number}
            onChange={(e) => setNumber(e.target.value)}
            required
            className="text-black"
          />
        </div>
        <button type="submit">Registrar Empleado</button>
        {successMessage && <p className="text-green-500">{successMessage}</p>}
        {errorMessage && <p className="text-red-500">{errorMessage}</p>}
      </form>
    </div>
  );
}

export default RegisterEmployee;
