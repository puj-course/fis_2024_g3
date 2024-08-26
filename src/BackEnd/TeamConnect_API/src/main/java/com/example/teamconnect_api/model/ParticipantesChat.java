package com.example.teamconnect_api.model;

import jakarta.persistence.*;


@Entity
@Table(name = "participante_chat")
public class ParticipantesChat {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "participante_chat_id")
    private int participanteChatId;

    @ManyToOne
    @JoinColumn(name = "empleado_id", nullable = false)
    private Empleado empleado;

    @ManyToOne
    @JoinColumn(name = "chat_id", nullable = false)
    private Chat chat;

    // Getters y Setters

    public int getParticipanteChatId() {
        return participanteChatId;
    }

    public void setParticipanteChatId(int participanteChatId) {
        this.participanteChatId = participanteChatId;
    }

    public Empleado getEmpleado() {
        return empleado;
    }

    public void setEmpleado(Empleado empleado) {
        this.empleado = empleado;
    }

    public Chat getChat() {
        return chat;
    }

    public void setChat(Chat chat) {
        this.chat = chat;
    }
}
