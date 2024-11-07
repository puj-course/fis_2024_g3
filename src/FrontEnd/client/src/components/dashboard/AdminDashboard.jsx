// src/components/dashboard/AdminDashboard.jsx

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

const AdminDashboard = () => {
  const [users, setUsers] = useState([]);
  const [projects, setProjects] = useState([]);
  const [tasks, setTasks] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [areas, setAreas] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem('token');
        const headers = { Authorization: `Bearer ${token}` };

        const [usersData, projectsData, tasksData, departmentsData, areasData] = await Promise.all([
          axios.get(`${API_URL}/admin/users`, { headers }),
          axios.get(`${API_URL}/admin/projects`, { headers }),
          axios.get(`${API_URL}/admin/tasks`, { headers }),
          axios.get(`${API_URL}/admin/departments`, { headers }),
          axios.get(`${API_URL}/admin/areas`, { headers })
        ]);

        setUsers(usersData.data);
        setProjects(projectsData.data);
        setTasks(tasksData.data);
        setDepartments(departmentsData.data);
        setAreas(areasData.data);
      } catch (err) {
        setError('No se pudo cargar la información');
      }
    };

    fetchData();
  }, []);

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Panel de Administración</h1>
      {error && <p className="text-red-500">{error}</p>}

      <div className="mt-4">
        <h2 className="text-2xl font-semibold">Usuarios</h2>
        <ul className="list-disc list-inside">
          {users.map((user) => (
            <li key={user.id}>{user.name} - {user.role}</li>
          ))}
        </ul>
      </div>

      <div className="mt-4">
        <h2 className="text-2xl font-semibold">Proyectos</h2>
        <ul className="list-disc list-inside">
          {projects.map((project) => (
            <li key={project.id}>{project.name}</li>
          ))}
        </ul>
      </div>

      <div className="mt-4">
        <h2 className="text-2xl font-semibold">Tareas</h2>
        <ul className="list-disc list-inside">
          {tasks.map((task) => (
            <li key={task.id}>{task.name} - Estado: {task.status}</li>
          ))}
        </ul>
      </div>

      <div className="mt-4">
        <h2 className="text-2xl font-semibold">Departamentos</h2>
        <ul className="list-disc list-inside">
          {departments.map((department) => (
            <li key={department.id}>{department.name}</li>
          ))}
        </ul>
      </div>

      <div className="mt-4">
        <h2 className="text-2xl font-semibold">Áreas</h2>
        <ul className="list-disc list-inside">
          {areas.map((area) => (
            <li key={area.id}>{area.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AdminDashboard;
