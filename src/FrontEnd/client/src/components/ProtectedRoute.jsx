import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children, allowedRoles }) => {
    const userRole = localStorage.getItem('role'); 
    const token = localStorage.getItem('token'); // Verificar si hay un token
  
    if (!token) {
      // Si no hay token, redirigir al login
      return <Navigate to="/login" />;
    }
  
    // if (!allowedRoles.includes(userRole)) {
    //   // Si el rol del usuario no está permitido, redirigir a acceso denegado
    //   return <Navigate to="/not-authorized" />;
    // }
  
    // Renderizar el componente si está autenticado y tiene el rol permitido
    return children;
};
  
export default ProtectedRoute;
