import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import TaskForm from "./pages/TaskForm";
import Navbar from "./components/Navbar";
import LoginPage from "./pages/LoginPage";
import RegisterEmployee from "./pages/RegisterEmployee"; // Asegúrate de importar el componente

function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto px-10">
        <Navbar />
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/" element={<HomePage />} />
          <Route path="/tasks/:id" element={<TaskForm />} />
          <Route path="/tasks/new" element={<TaskForm />} />
          <Route path="/register-employee" element={<RegisterEmployee />} /> {/* Ruta para Registrar Empleado */}
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;