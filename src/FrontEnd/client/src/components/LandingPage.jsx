// src/components/LandingPage.jsx
import React from 'react';

const LandingPage = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-4xl font-bold mb-4">TeamConnect</h1>
      <p className="text-lg mb-8 text-center px-4 md:px-0">
        Somos tu software importante para que conectes con toda tu empresa, tus proyectos o lo que te imagines.
      </p>
      <div className="space-x-4">
        <a href="/login" className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Iniciar Sesión
        </a>
        <a href="/register" className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
          Registrarse
        </a>
      </div>
    </div>
  );
};

export default LandingPage;
