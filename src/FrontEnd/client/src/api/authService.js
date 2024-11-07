import axios from 'axios';

const API_URL = 'http://localhost:8000'; 

export const login = async (email, password) => {
  try {
    const response = await axios.post($`{API_URL}/login`, {
      username: email,
      password: password,
    });
    
    if (response.data.access_token) {
      localStorage.setItem('token', response.data.access_token); // Guarda el token en el almacenamiento local
    }
    return response.data;
  } catch (error) {
    console.error('Error en el inicio de sesión', error);
    throw error;
  }
};

export const logout = () => {
  localStorage.removeItem('token');
};

export const getToken = () => {
  return localStorage.getItem('token');
};

export const isAuthenticated = () => {
  return !!getToken();
};