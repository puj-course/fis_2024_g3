package com.example.teamconnect_api.enums;

public enum EmpleadoROle {

    GERENTE("Gerente"),
    LIDER("Lider"),
    EMPLEADO("Empleado");


    private String role;

    EmpleadoROle(String role){
        this.role = role;
    }

    public String getRole(){
        return role;
    }
}
