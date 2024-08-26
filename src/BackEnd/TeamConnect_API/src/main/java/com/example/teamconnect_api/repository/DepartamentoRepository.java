package com.example.teamconnect_api.repository;
import com.example.teamconnect_api.model.Departamento;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DepartamentoRepository extends JpaRepository<Departamento, Integer> {
    // Métodos personalizados si es necesario
}
