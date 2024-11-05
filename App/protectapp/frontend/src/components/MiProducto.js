// src/components/MiProducto.js
<<<<<<< HEAD
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import UserMenu from './UserMenu';
=======
<<<<<<< HEAD
import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import UserMenu from './UserMenu'; // Importa el componente UserMenu
// import '../css/MiProducto.css';
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBox } from '@fortawesome/free-solid-svg-icons';

const MiProducto = () => {
<<<<<<< HEAD
    const [username, setUsername] = useState('');

    useEffect(() => {
        const fetchUserProfile = async () => {
=======
    useEffect(() => {
=======
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBox } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import UserIcon from '../assets/img/cuenta.png';

const MiProducto = () => {
    const logout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        alert("Has cerrado sesión.");
        window.location.href = "/login";
    };

    React.useEffect(() => {
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
        const checkLogin = () => {
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            const token = localStorage.getItem('access_token');
            if (!token) {
                alert("No has iniciado sesión. Redirigiendo a la página de inicio de sesión.");
                window.location.href = "/login";
<<<<<<< HEAD
                return;
            }

            try {
                const response = await fetch('http://localhost:8000/api/user/profile/', {
                    headers: {
                        'Authorization': `Bearer ${token}`,
                        'Content-Type': 'application/json',
                    },
                });

                if (response.ok) {
                    const data = await response.json();
                    setUsername(data.username);  
                } else {
                    alert("Error al obtener datos del usuario.");
                }
            } catch (error) {
                console.error("Error al conectarse al servidor:", error);
            }
        };

        fetchUserProfile();
=======
            }
        };

        checkLogin();
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    }, []);

    return (
        <div className="main-content">
            <div className="content-header">
<<<<<<< HEAD
                <h2>Bienvenido{username && `, ${username}`}</h2>
                <UserMenu />
=======
                <h2>Bienvenido</h2>
<<<<<<< HEAD
                <UserMenu /> 
=======
                <div className="user-info">
                    <img src={UserIcon} alt="User Icon" id="user-icon" onClick={() => document.getElementById("user-dropdown").classList.toggle("show")}/>
                    <div className="user-dropdown" id="user-dropdown">
                        <Link to="/cuenta">Mi Cuenta</Link>
                        <Link to="/login" onClick={logout}>Cerrar Sesión</Link>
                    </div>
                </div>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            </div>

            {/* Product Section */}
            <div className="product-box">
                <h3>No tienes un producto adquirido</h3>
                <p>Adquiere un plan para comenzar a proteger a tus seres queridos.</p>
<<<<<<< HEAD
                <Link to="/compras" className="btn-plan">
                    <FontAwesomeIcon icon={faBox} /> Ver Planes
                </Link>
=======
<<<<<<< HEAD
                <Link to="/compras" className="btn-plan">
                    <FontAwesomeIcon icon={faBox} /> Ver Planes
                </Link>
=======
                <Link to="/compras" className="btn-plan">Ver Planes</Link>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            </div>
        </div>
    );
};

export default MiProducto;
