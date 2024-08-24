package com.example.teamconnect_api.model;

import jakarta.annotation.Generated;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Table;

@Entity
@Table(name = Roles)

public class Rol {
    @Id
    @GeneratedValue(strategy =  GeneratedValue.IDENTITY)
    @Column(name = "rol_id")
    private int id;

    @Column(name = "nombre", nullable = false, length = 60)
    private string nombre_area;
    
}
