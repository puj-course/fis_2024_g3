package com.example.teamconnect_api.repository;

import com.example.teamconnect_api.model.Empleado;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Repository;
import java.util.List;


@Repository
public interface EmpleadoRepository extends JpaRepository<Empleado, Integer> {
    // Métodos personalizados si es necesario
    Empleado findByCodigo(String codigo);
    UserDetails findByLogin(String login);
    
}
