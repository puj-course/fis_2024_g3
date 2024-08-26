package com.example.teamconnect_api.repository;

import com.example.teamconnect_api.model.Tarea;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface TareaRepository extends JpaRepository<Tarea, Integer> {
    // Métodos personalizados si es necesario
}
