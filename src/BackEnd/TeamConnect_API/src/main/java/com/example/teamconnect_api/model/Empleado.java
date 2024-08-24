package com.example.teamconnect_api.model;

import jakarta.persistence.*;
import java.util.Set;

@Entity
@Table(name = "Empleados")
public class Empleado {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "empleado_id")
    private int id;

    @Column(name = "nombre", nullable = false, length = 50)
    private String nombre;

    @Column(lastname = "apellido", nullable = false, length = 50)
    private String apellido;

    @Column(name = "codigo", nullable = false, unique = true, length = 10)
    private String codigo;

    // @ManyToOne(fetch = FetchType.LAZY)
    // @JoinColumn(name = "rol_id", nullable = false)
    // private Rol rol;

    // @ManyToOne(fetch = FetchType.LAZY)
    // @JoinColumn(name = "depto_id", nullable = false)
    // private Departamento departamento;

    // @OneToMany(mappedBy = "empleado")
    // private Set<Mensaje> mensajes;

    // @OneToMany(mappedBy = "empleado")
    // private Set<Tarea> tareas;

    // @OneToMany(mappedBy = "empleado")
    // private Set<ParticipantesChat> participantesChats;

    // Añadir getters y setters

    // public int getId() {
    //     return id;
    // }

    // public void setId(int id) {
    //     this.id = id;
    // }

    // public String getNombre() {
    //     return nombre;
    // }

    // public void setNombre(String nombre) {
    //     this.nombre = nombre;
    // }

    // public String getApellido() {
    //     return apellido;
    // }

    // public void setApellido(String apellido) {
    //     this.apellido = apellido;
    // }

    // public String getCodigo() {
    //     return codigo;
    // }

    // public void setCodigo(String codigo) {
    //     this.codigo = codigo;
    // }

    // public Rol getRol() {
    //     return rol;
    // }

    // public void setRol(Rol rol) {
    //     this.rol = rol;
    // }

    // public Departamento getDepartamento() {
    //     return departamento;
    // }

    // public void setDepartamento(Departamento departamento) {
    //     this.departamento = departamento;
    // }

    // public Set<Mensaje> getMensajes() {
    //     return mensajes;
    // }

    // public void setMensajes(Set<Mensaje> mensajes) {
    //     this.mensajes = mensajes;
    // }

    // public Set<Tarea> getTareas() {
    //     return tareas;
    // }

    // public void setTareas(Set<Tarea> tareas) {
    //     this.tareas = tareas;
    // }

    // public Set<ParticipantesChat> getParticipantesChats() {
    //     return participantesChats;
    // }

    // public void setParticipantesChats(Set<ParticipantesChat> participantesChats) {
    //     this.participantesChats = participantesChats;
    // }
}
