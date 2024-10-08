package com.example.teamconnect_api.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

import java.util.Collection;
import java.util.Set;

import org.hibernate.annotations.DialectOverride.OverridesAnnotation;
import org.hibernate.mapping.List;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import com.example.teamconnect_api.enums.EmpleadoROle;

@Entity(name = "Empleados")
@Table(name = "Empleados")
//@NoArgsConstructor
//@AllArgsConstructor
//@EqualsAndHashCode(of = "empleado_id")

public class Empleado implements UserDetails{

    private String login;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "empleado_id")
    private int id;

    @Column(name = "nombre", nullable = false, length = 50)
    private String nombre;

    @Column(name = "apellido", nullable = false, length = 50)
    private String apellido;

    @Column(name = "codigo", nullable = false, unique = true, length = 10)
    private String codigo;
    
    @Column(name = "email",nullable = false, unique = true, length = 50)
    private String email;

    @Column(name = "password",nullable = false, unique = true, length = 100)
    private String password;

    // @ManyToOne(fetch = FetchType.LAZY)
    // @JoinColumn(name = "rol_id", nullable = false)
    @Enumerated(EnumType.STRING)
    private EmpleadoROle rol;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "depto_id", nullable = false)
    private Departamento departamento;

    @OneToMany(mappedBy = "empleado")
    private Set<Mensaje> mensajes;

    @OneToMany(mappedBy = "empleado")
    private Set<Tarea> tareas;

    @OneToMany(mappedBy = "empleado")
    private Set<ParticipantesChat> participantesChats;

    //Constructor.
    public Empleado(int id, String nombre, String apellido, String codigo, String email, String password, EmpleadoROle rol,
    Departamento departamento, Set<Mensaje> mensajes, Set<Tarea> tareas,
    Set<ParticipantesChat> participantesChats, String login) {
        this.id = id;
        this.nombre = nombre;
        this.apellido = apellido;
        this.codigo = codigo;
        this.email = email;
        this.password = password;
        this.rol = rol;
        this.departamento = departamento;
        this.mensajes = mensajes;
        this.tareas = tareas;
        this.participantesChats = participantesChats;
        this.login = login;
    }

    
    
 
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public EmpleadoROle getRol() {
        return rol;
    }

    public void setRol(EmpleadoROle rol) {
        this.rol = rol;
    }

    public Departamento getDepartamento() {
        return departamento;
    }

    public void setDepartamento(Departamento departamento) {
        this.departamento = departamento;
    }

    public Set<Mensaje> getMensajes() {
        return mensajes;
    }

    public void setMensajes(Set<Mensaje> mensajes) {
        this.mensajes = mensajes;
    }

    public Set<Tarea> getTareas() {
        return tareas;
    }

    public void setTareas(Set<Tarea> tareas) {
        this.tareas = tareas;
    }

    public Set<ParticipantesChat> getParticipantesChats() {
        return participantesChats;
    }

    public void setParticipantesChats(Set<ParticipantesChat> participantesChats) {
        this.participantesChats = participantesChats;
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        if(this.rol == EmpleadoROle.GERENTE){
            return List.of(new SimpleGrantedAuthority("ROLE_GERENTE"), new SimpleGrantedAuthority("ROLE_EMPLEADO"));
        }
        if(this.rol == EmpleadoROle.LIDER){
            return List.of(new SimpleGrantedAuthority("ROLE_LIDER"), new SimpleGrantedAuthority("ROLE_EMPLEADO"));
        }
        return List.of(new SimpleGrantedAuthority("ROLE_EMPLEADO"));
    }

    @Override
    public String getUsername() {return login;}

    @Override 
    public boolean isAccountNonExpired(){return true;}

    @Override
    public boolean isAccountNonLocked(){return true;}

    @Override 
    public boolean isCredentialsNonExpired(){return true;}

    @Override
    public boolean isEnabled(){return true;}

    @Override
    public String getPassword() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getPassword'");
    }
}
