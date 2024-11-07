// src/components/dashboard/EmployeeDashboard.jsx

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

const API_URL = 'http://localhost:8000';

const EmployeeDashboard = () => {
  const [tasks, setTasks] = useState({
    Pending: [],
    Prepared: [],
    onGoing: [],
    Finished: []
  });
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get(`${API_URL}/tasks/assigned`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        
        // Agrupa las tareas por estado
        const tasksByStatus = {
          Pending: [],
          Prepared: [],
          onGoing: [],
          Finished: []
        };

        response.data.forEach(task => {
          tasksByStatus[task.status].push(task);
        });

        setTasks(tasksByStatus);
      } catch (err) {
        setError('No se pudieron cargar las tareas.');
      }
    };

    fetchTasks();
  }, []);

  // Función para manejar el cambio de posición de las tareas
  const onDragEnd = async (result) => {
    const { source, destination } = result;

    // Si no se suelta en una columna válida, salir
    if (!destination) return;

    // Si la posición inicial y final son las mismas, salir
    if (source.droppableId === destination.droppableId && source.index === destination.index) return;

    // Copiar las tareas para manipulación local
    const sourceColumn = tasks[source.droppableId];
    const destinationColumn = tasks[destination.droppableId];
    const [movedTask] = sourceColumn.splice(source.index, 1);

    // Cambiar el estado de la tarea según la columna de destino
    movedTask.status = destination.droppableId;
    destinationColumn.splice(destination.index, 0, movedTask);

    setTasks({
      ...tasks,
      [source.droppableId]: sourceColumn,
      [destination.droppableId]: destinationColumn
    });

    // Actualizar el estado de la tarea en el backend
    try {
      await axios.patch(`${API_URL}/tasks/${movedTask.id}/status`, {
        status: movedTask.status
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      });
    } catch (error) {
      console.error("No se pudo actualizar el estado de la tarea:", error);
    }
  };

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Tablero de Tareas</h1>
      {error && <p className="text-red-500">{error}</p>}

      <DragDropContext onDragEnd={onDragEnd}>
        <div className="grid grid-cols-4 gap-4">
          {Object.entries(tasks).map(([status, tasks]) => (
            <Droppable droppableId={status} key={status}>
              {(provided) => (
                <div
                  {...provided.droppableProps}
                  ref={provided.innerRef}
                  className="bg-gray-800 p-4 rounded shadow-md"
                >
                  <h2 className="text-xl font-semibold mb-4">{status}</h2>
                  {tasks.map((task, index) => (
                    <Draggable key={task.id} draggableId={task.id} index={index}>
                      {(provided) => (
                        <div
                          ref={provided.innerRef}
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                          className="bg-gray-700 p-3 rounded mb-2 shadow-md"
                        >
                          <h3 className="text-lg font-medium">{task.name}</h3>
                          <p className="text-sm">{task.description}</p>
                        </div>
                      )}
                    </Draggable>
                  ))}
                  {provided.placeholder}
                </div>
              )}
            </Droppable>
          ))}
        </div>
      </DragDropContext>
    </div>
  );
};

export default EmployeeDashboard;
