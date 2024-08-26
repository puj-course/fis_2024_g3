package com.example.teamconnect_api.repository;

import com.example.teamconnect_api.model.ParticipantesChat;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ParticipantesChatRepository extends JpaRepository<ParticipantesChat, Integer> {
    // Métodos personalizados si es necesario
}
