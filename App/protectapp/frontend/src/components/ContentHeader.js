// src/components/ContentHeader.js
<<<<<<< HEAD
import React from 'react';
import UserMenu from './UserMenu'; 
=======
<<<<<<< HEAD
import React from 'react';
import UserMenu from './UserMenu'; 
=======
<<<<<<< HEAD
import React from 'react';
import UserMenu from './UserMenu'; // Importa el nuevo componente UserMenu
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6

const ContentHeader = () => {
    return (
        <div className="content-header">
            <h2>Bienvenido de nuevo</h2>
<<<<<<< HEAD
            <UserMenu /> 
=======
<<<<<<< HEAD
            <UserMenu /> 
=======
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
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
        </div>
    );
};

export default ContentHeader;
