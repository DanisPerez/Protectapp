// src/components/Capturas.js
import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import SidebarEventos from './SidebarEventos';
import '../css/Capturas.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faDesktop, faCamera } from '@fortawesome/free-solid-svg-icons';
import accountImage from '../assets/img/cuenta.png';

const Capturas = () => {
    const token = localStorage.getItem('access_token');
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const navigate = useNavigate();

    useEffect(() => {
        if (!token || !dispositivoId) {
            alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
            navigate('/login');
        }
    }, [token, dispositivoId, navigate]);

    const manejarCaptura = async (url, tipoCaptura) => {
        try {
            mostrarSpinner(true);
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });
            mostrarSpinner(false);

            if (response.ok) {
                const data = await response.json();
                tipoCaptura === 'pantalla' ? mostrarCaptura(data.ruta_captura) : mostrarFoto(data.ruta_foto);
                alert(`${tipoCaptura.charAt(0).toUpperCase() + tipoCaptura.slice(1)} realizada con éxito!`);
            } else {
                const errorData = await response.json();
                alert(`Error al realizar la ${tipoCaptura}: ${errorData.error || 'Desconocido'}`);
            }
        } catch (error) {
            mostrarSpinner(false);
            console.error(`Error al realizar la ${tipoCaptura}:`, error);
            alert('Error de conexión.');
        }
    };

    const mostrarSpinner = (mostrar) => {
        document.getElementById('spinner').style.display = mostrar ? 'inline-block' : 'none';
    };

    const mostrarCaptura = (ruta) => {
        const previewSection = document.getElementById('preview-section');
        const imgElement = document.createElement('img');
        imgElement.src = ruta;
        imgElement.classList.add('preview-image');
        previewSection.appendChild(imgElement);
    };

    const mostrarFoto = (ruta) => {
        const previewSection = document.getElementById('preview-section');
        const imgElement = document.createElement('img');
        imgElement.src = ruta;
        imgElement.classList.add('preview-image');
        previewSection.appendChild(imgElement);
    };

    const toggleUserDropdown = () => {
        const dropdown = document.getElementById('user-dropdown');
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    };

    const logout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('dispositivoSeleccionado');
        navigate('/login');
    };

    return (
        <div className="main-layout">
            <SidebarEventos />
            <div className="main-content">
                <div className="content-header">
                    <h2>Capturas</h2>
                    <div className="user-info">
                        <img src={accountImage} alt="User Icon" id="user-icon" onClick={toggleUserDropdown} />
                        <div className="user-dropdown" id="user-dropdown">
                            <a href="/cuenta">Mi Cuenta</a>
                            <button onClick={logout}>Cerrar Sesión</button>
                        </div>
                    </div>
                </div>

                <div className="mb-3">
                    <button
                        className="btn btn-primary"
                        onClick={() => manejarCaptura(`http://localhost:8000/api/dispositivos/${dispositivoId}/capturas-pantalla/`, 'pantalla')}
                    >
                        <FontAwesomeIcon icon={faDesktop} /> Capturar Pantalla
                    </button>
                    <button
                        className="btn btn-secondary"
                        onClick={() => manejarCaptura(`http://localhost:8000/api/dispositivos/${dispositivoId}/fotos/`, 'foto')}
                    >
                        <FontAwesomeIcon icon={faCamera} /> Tomar Foto
                    </button>
                    <div id="spinner" className="spinner-border text-info" role="status">
                        <span className="sr-only">Procesando...</span>
                    </div>
                </div>

                <div className="preview" id="preview-section">
                    <h3>Capturas de Pantalla</h3>
                    <h3>Fotos</h3>
                </div>
            </div>
        </div>
    );
};

export default Capturas;
