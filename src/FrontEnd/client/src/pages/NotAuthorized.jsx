import React from 'react';

const NotAuthorized = () => {
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-3xl font-bold">Acceso Denegado</h1>
      <p>No tienes permiso para acceder a esta página.</p>
    </div>
  );
};

export default NotAuthorized;   