// src/components/ContentHeader.js
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
        </div>
    );
};

export default ContentHeader;
