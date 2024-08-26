package com.example.teamconnect_api.model;
import jakarta.persistence.*;
import java.util.Date;

@Entity
@Table(name = "tarea")
public class Tarea {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "tarea_id")
    private int tareaId;

    @Column(name = "codigo", nullable = false)
    private String codigo;

    @Column(name = "estado", nullable = false)
    private String estado;

    @Column(name = "fecha_envio", nullable = false)
    @Temporal(TemporalType.TIMESTAMP)
    private Date fechaEnvio;

    @Column(name = "fecha_respuesta")
    @Temporal(TemporalType.TIMESTAMP)
    private Date fechaRespuesta;

    @Column(name = "fecha_solucion")
    @Temporal(TemporalType.TIMESTAMP)
    private Date fechaSolucion;

    @ManyToOne
    @JoinColumn(name = "depto_emisor_id", nullable = false)
    private Departamento departamentoEmisor;

    @ManyToOne
    @JoinColumn(name = "depto_receptor_id", nullable = false)
    private Departamento departamentoReceptor;

    @ManyToOne
    @JoinColumn(name = "empleado_id", nullable = false)
    private Empleado empleado;

    // Getters y Setters

    public int getTareaId() {
        return tareaId;
    }

    public void setTareaId(int tareaId) {
        this.tareaId = tareaId;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public Date getFechaEnvio() {
        return fechaEnvio;
    }

    public void setFechaEnvio(Date fechaEnvio) {
        this.fechaEnvio = fechaEnvio;
    }

    public Date getFechaRespuesta() {
        return fechaRespuesta;
    }

    public void setFechaRespuesta(Date fechaRespuesta) {
        this.fechaRespuesta = fechaRespuesta;
    }

    public Date getFechaSolucion() {
        return fechaSolucion;
    }

    public void setFechaSolucion(Date fechaSolucion) {
        this.fechaSolucion = fechaSolucion;
    }

    public Departamento getDepartamentoEmisor() {
        return departamentoEmisor;
    }

    public void setDepartamentoEmisor(Departamento departamentoEmisor) {
        this.departamentoEmisor = departamentoEmisor;
    }

    public Departamento getDepartamentoReceptor() {
        return departamentoReceptor;
    }

    public void setDepartamentoReceptor(Departamento departamentoReceptor) {
        this.departamentoReceptor = departamentoReceptor;
    }

    public Empleado getEmpleado() {
        return empleado;
    }

    public void setEmpleado(Empleado empleado) {
        this.empleado = empleado;
    }
}
