// src/components/MiProducto.js
<<<<<<< HEAD
import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import UserMenu from './UserMenu'; // Importa el componente UserMenu
// import '../css/MiProducto.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBox } from '@fortawesome/free-solid-svg-icons';

const MiProducto = () => {
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
            const token = localStorage.getItem('access_token');
            if (!token) {
                alert("No has iniciado sesión. Redirigiendo a la página de inicio de sesión.");
                window.location.href = "/login";
            }
        };

        checkLogin();
    }, []);

    return (
        <div className="main-content">
            <div className="content-header">
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
                <Link to="/compras" className="btn-plan">Ver Planes</Link>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
            </div>
        </div>
    );
};

export default MiProducto;
