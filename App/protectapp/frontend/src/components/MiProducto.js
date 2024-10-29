// src/components/MiProducto.js
import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import UserMenu from './UserMenu'; // Importa el componente UserMenu
// import '../css/MiProducto.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBox } from '@fortawesome/free-solid-svg-icons';

const MiProducto = () => {
    useEffect(() => {
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
                <UserMenu /> 
            </div>

            {/* Product Section */}
            <div className="product-box">
                <h3>No tienes un producto adquirido</h3>
                <p>Adquiere un plan para comenzar a proteger a tus seres queridos.</p>
                <Link to="/compras" className="btn-plan">
                    <FontAwesomeIcon icon={faBox} /> Ver Planes
                </Link>
            </div>
        </div>
    );
};

export default MiProducto;
