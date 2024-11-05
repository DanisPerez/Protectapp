// src/components/MiProducto.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import UserMenu from './UserMenu';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBox } from '@fortawesome/free-solid-svg-icons';

const MiProducto = () => {
    const [username, setUsername] = useState('');

    useEffect(() => {
        const fetchUserProfile = async () => {
            const token = localStorage.getItem('access_token');
            if (!token) {
                alert("No has iniciado sesión. Redirigiendo a la página de inicio de sesión.");
                window.location.href = "/login";
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
    }, []);

    return (
        <div className="main-content">
            <div className="content-header">
                <h2>Bienvenido{username && `, ${username}`}</h2>
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
