// src/components/UserMenu.js
import React, { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';
import UserIcon from '../assets/img/cuenta.png'; 
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
