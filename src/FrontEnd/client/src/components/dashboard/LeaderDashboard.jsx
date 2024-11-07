// src/components/dashboard/LeaderDashboard.jsx

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

const LeaderDashboard = () => {
  const [department, setDepartment] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchDepartment = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get(`${API_URL}/departments/assigned`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        setDepartment(response.data);
      } catch (err) {
        setError('No se pudo cargar el departamento asignado.');
      }
    };

    fetchDepartment();
  }, []);

  if (error) {
    return <p className="text-red-500">{error}</p>;
  }

  if (!department) {
    return <p>Cargando el departamento asignado...</p>;
  }

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Dashboard del Líder</h1>
      <h2 className="text-2xl font-semibold mb-2">Departamento: {department.name}</h2>
      <p className="mb-4">{department.description}</p>

      <div className="mt-6">
        <h3 className="text-xl font-semibold">Usuarios en el Departamento:</h3>
        <ul className="list-disc list-inside">
          {department.users.map((user, index) => (
            <li key={index}>{user}</li>
          ))}
        </ul>
      </div>

      <div className="mt-6">
        <h3 className="text-xl font-semibold">Proyectos en el Departamento:</h3>
        <ul className="list-disc list-inside">
          {department.projects.map((project, index) => (
            <li key={index}>{project}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default LeaderDashboard;
