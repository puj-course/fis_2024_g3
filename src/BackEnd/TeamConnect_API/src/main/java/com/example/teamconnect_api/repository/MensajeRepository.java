package com.example.teamconnect_api.repository;

import com.example.teamconnect_api.model.Mensaje;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MensajeRepository extends JpaRepository<Mensaje, Integer> {
    // Métodos personalizados si es necesario
}
