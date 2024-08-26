package com.example.teamconnect_api.repository;

import com.example.teamconnect_api.model.Rol;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RolRepository extends JpaRepository<Rol, Integer> {
    // Métodos personalizados si es necesario
}
