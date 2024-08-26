package com.example.teamconnect_api.repository;
import com.example.teamconnect_api.model.Chat;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ChatRepo extends JpaRepository<Chat, Integer> {
    // Métodos personalizados si es necesario
}
