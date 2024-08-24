package com.example.teamconnect_api.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "areas")
public class Area {
    @Id
    @GeneratedValue(strategy = GeneratedValue.IDENTITY)
    @Column(name="area_id")
    private int id;

    @Column(name = "nombre", nullable = false, length = 60)
    private string nombre_area;

    

}
