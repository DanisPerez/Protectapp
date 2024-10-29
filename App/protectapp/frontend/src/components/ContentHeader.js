// src/components/ContentHeader.js
<<<<<<< HEAD
import React from 'react';
import UserMenu from './UserMenu'; // Importa el nuevo componente UserMenu

const ContentHeader = () => {
    return (
        <div className="content-header">
            <h2>Bienvenido de nuevo</h2>
            <UserMenu /> {/* Reemplaza la lógica del dropdown con el componente UserMenu */}
=======
import React, { useState } from 'react';
import UserIcon from '../assets/img/cuenta.png';
import { Link } from 'react-router-dom';

const ContentHeader = () => {
    const [dropdownVisible, setDropdownVisible] = useState(false);

    const toggleDropdown = () => {
        setDropdownVisible(!dropdownVisible);
    };

    const logout = () => {
        localStorage.removeItem('access_token');
        alert("Has cerrado sesión.");
        window.location.href = "/login";
    };

    return (
        <div className="content-header">
        <h2>Bienvenido de nuevo</h2>
        <div className="user-info" onClick={toggleDropdown}>
            <img src={UserIcon} alt="User Icon" />
            {dropdownVisible && (
            <div className="user-dropdown">
                <Link to="/cuenta">Mi Cuenta</Link>
                <Link to="/login" onClick={logout}>Cerrar Sesión</Link>
            </div>
            )}
        </div>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
        </div>
    );
};

export default ContentHeader;
