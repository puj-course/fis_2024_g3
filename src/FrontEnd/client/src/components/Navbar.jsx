import { Link, useLocation } from "react-router-dom";

function Navbar() {
  const location = useLocation();

  return (
    <header className="flex justify-between items-center my-7">
      <Link to="/">
        <h1 className="text-3xl font-bold">Team Connect</h1>
      </Link>
      <div className="flex space-x-4">
        {/* Mostrar el botón de "Iniciar Sesión" solo en la página de registro de empleados */}
        {location.pathname !== "/login" && (
          <Link
            to="/login"
            className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Iniciar Sesión
          </Link>
        )}
        {/* Mostrar el botón de "Registrar Empleado" solo si el usuario está en la página de login o en la página principal */}
        {(location.pathname === "/" || location.pathname === "/login") && (
          <Link
            to="/register-employee"
            className="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
          >
            Registrar Empleado
          </Link>
        )}
        {/* Botón de regreso o de creación de tarea */}
        {location.pathname === "/" ? (
          <Link
            to="/tasks/new"
            className="bg-zinc-950 hover:bg-gray-950 text-white font-bold py-2 px-4 rounded"
          >
            Crear Tarea
          </Link>
        ) : (
          <Link
            to="/"
            className="bg-zinc-950 hover:bg-gray-950 text-white font-bold py-2 px-4 rounded"
          >
            Volver
          </Link>
        )}
      </div>
    </header>
  );
}

export default Navbar;