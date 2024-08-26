package com.example.teamconnect_api.repository;
import com.example.teamconnect_api.model.Area;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AreaRepository extends JpaRepository<Area, Integer> {
    // Métodos personalizados si es necesario
}