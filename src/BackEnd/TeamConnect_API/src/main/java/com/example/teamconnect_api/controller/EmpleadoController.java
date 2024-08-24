package com.example.teamconnect_api.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;


@RestController
@RequestMapping("/api/users")
public class EmpleadoController{
    @GetMapping
    public String getAllUsers() {
        return "Hello, World!";
    }

    @GetMapping("/login")
    public String getMethodName() {
        return "NUeva ventana de prueba";
    }
    
    @GetMapping("/info")
    public String info() {
        return "Nuevo mensaje";
    }

}