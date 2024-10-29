// src/components/MiProducto.js
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
                <div className="user-info">
                    <img src={UserIcon} alt="User Icon" id="user-icon" onClick={() => document.getElementById("user-dropdown").classList.toggle("show")}/>
                    <div className="user-dropdown" id="user-dropdown">
                        <Link to="/cuenta">Mi Cuenta</Link>
                        <Link to="/login" onClick={logout}>Cerrar Sesión</Link>
                    </div>
                </div>
            </div>

            {/* Product Section */}
            <div className="product-box">
                <h3>No tienes un producto adquirido</h3>
                <p>Adquiere un plan para comenzar a proteger a tus seres queridos.</p>
                <Link to="/compras" className="btn-plan">Ver Planes</Link>
            </div>
        </div>
    );
};

export default MiProducto;
