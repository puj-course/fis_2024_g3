package com.example.teamconnect_api.services;

import java.util.ArrayList;
import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import com.example.teamconnect_api.dtos.SignUpDto;
import com.example.teamconnect_api.model.Empleado;
import com.example.teamconnect_api.repository.EmpleadoRepository;

@Service
public class AuthService implements UserDetailsService {
    @Autowired
    EmpleadoRepository repository;

    @Override
    public UserDetails loadUserByUsername(String login) throws UsernameNotFoundException {

        UserDetails user = repository.findByLogin(login);
        if (user == null) {
            throw new UsernameNotFoundException("User not found");
        }

        // Aquí conviertes el empleado en UserDetails
        return new org.springframework.security.core.userdetails.User(
            ((Empleado) user).getLogin(), 
            user.getPassword(), 
            new ArrayList<>() // Si tienes roles implementados, puedes mapearlos aquí
        );
    }

    public UserDetails signUp(SignUpDto data) throws InvalidJwtException {
        if (repository.findByLogin(data.login()) != null) {
            throw new InvalidJwtException("Username already exists");
        }
        String encryptedPassword = new BCryptPasswordEncoder().encode(data.password());
        Empleado newUser = new Empleado(0, data.login(), encryptedPassword, data.rol(), encryptedPassword, encryptedPassword, null, null, null, null, null, encryptedPassword);
        return repository.save(newUser);
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getAuthorities'");
    }

    @Override
    public String getPassword() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getPassword'");
    }

    @Override
    public String getUsername() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'getUsername'");
    }

    


    
}
