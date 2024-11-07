// src/components/dashboard/ManagerDashboard.jsx

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

const API_URL = 'http://localhost:8000';

const ManagerDashboard = () => {
  const [projects, setProjects] = useState({
    Pending: [],
    InProgress: [],
    Completed: []
  });
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get(`${API_URL}/projects/assigned`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        
        // Agrupar los proyectos por estado
        const projectsByStatus = {
          Pending: [],
          InProgress: [],
          Completed: []
        };

        response.data.forEach(project => {
          projectsByStatus[project.status].push(project);
        });

        setProjects(projectsByStatus);
      } catch (err) {
        setError('No se pudieron cargar los proyectos.');
      }
    };

    fetchProjects();
  }, []);

  const onDragEnd = async (result) => {
    const { source, destination } = result;

    if (!destination) return;

    if (source.droppableId === destination.droppableId && source.index === destination.index) return;

    const sourceColumn = projects[source.droppableId];
    const destinationColumn = projects[destination.droppableId];
    const [movedProject] = sourceColumn.splice(source.index, 1);

    movedProject.status = destination.droppableId;
    destinationColumn.splice(destination.index, 0, movedProject);

    setProjects({
      ...projects,
      [source.droppableId]: sourceColumn,
      [destination.droppableId]: destinationColumn
    });

    try {
      await axios.patch(`${API_URL}/projects/${movedProject.id}/status`, {
        status: movedProject.status
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      });
    } catch (error) {
      console.error("No se pudo actualizar el estado del proyecto:", error);
    }
  };

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h1 className="text-3xl font-bold mb-4">Tablero de Proyectos</h1>
      {error && <p className="text-red-500">{error}</p>}

      <DragDropContext onDragEnd={onDragEnd}>
        <div className="grid grid-cols-3 gap-4">
          {Object.entries(projects).map(([status, projects]) => (
            <Droppable droppableId={status} key={status}>
              {(provided) => (
                <div
                  {...provided.droppableProps}
                  ref={provided.innerRef}
                  className="bg-gray-800 p-4 rounded shadow-md"
                >
                  <h2 className="text-xl font-semibold mb-4">{status}</h2>
                  {projects.map((project, index) => (
                    <Draggable key={project.id} draggableId={project.id} index={index}>
                      {(provided) => (
                        <div
                          ref={provided.innerRef}
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                          className="bg-gray-700 p-3 rounded mb-2 shadow-md"
                        >
                          <h3 className="text-lg font-medium">{project.name}</h3>
                          <p className="text-sm">{project.description}</p>

                          {/* Lista de tareas en el proyecto */}
                          <div className="mt-2">
                            <h4 className="font-semibold">Tareas:</h4>
                            <ul className="list-disc list-inside">
                              {project.tasks.map((task) => (
                                <li key={task.id} className="mt-1">
                                  <strong>{task.name}</strong>
                                  <ul className="pl-4 text-sm">
                                    {task.user_names.map((user, idx) => (
                                      <li key={idx}>{user}</li>
                                    ))}
                                  </ul>
                                </li>
                              ))}
                            </ul>
                          </div>
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

export default ManagerDashboard;
