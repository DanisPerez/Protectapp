// src/components/UserMenu.js
import React, { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';
<<<<<<< HEAD
import UserIcon from '../assets/img/cuenta.png'; 
=======
import UserIcon from '../assets/img/cuenta.png'; // Asegúrate de ajustar esta ruta según tu estructura de archivos
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
import '../css/Account.css';

const UserMenu = () => {
    const [dropdownVisible, setDropdownVisible] = useState(false);
    const dropdownRef = useRef(null);

    const toggleDropdown = () => {
        setDropdownVisible(!dropdownVisible);
    };

    const closeDropdown = (e) => {
        if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
            setDropdownVisible(false);
        }
    };

    useEffect(() => {
        document.addEventListener('mousedown', closeDropdown);
        return () => {
            document.removeEventListener('mousedown', closeDropdown);
        };
    }, []);

    const logout = () => {
        localStorage.removeItem('access_token');
        alert("Se ha cerrado la sesión.");
        window.location.href = "/login";
    };

    return (
        <div className="user-info" onClick={toggleDropdown} ref={dropdownRef}>
            <img src={UserIcon} alt="Icono de usuario" className="user-icon" />
            {dropdownVisible && (
                <div className="user-dropdown show">
                    <Link to="/cuenta">Mi Cuenta</Link>
                    <Link to="/login" onClick={logout}>Cerrar Sesión</Link>
                </div>
            )}
        </div>
    );
};

export default UserMenu;
