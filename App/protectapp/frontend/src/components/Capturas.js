// src/components/Capturas.js
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import UserMenu from './UserMenu';
import '../css/Capturas.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faDesktop, faCamera } from '@fortawesome/free-solid-svg-icons';

const BASE_URL = "http://127.0.0.1:8000";
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import SidebarEventos from './SidebarEventos';
import '../css/Capturas.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faDesktop, faCamera } from '@fortawesome/free-solid-svg-icons';
import accountImage from '../assets/img/cuenta.png';
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6

const Capturas = () => {
    const token = localStorage.getItem('access_token');
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const navigate = useNavigate();
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    const [capturas, setCapturas] = useState([]);
    const [fotos, setFotos] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6

    useEffect(() => {
        if (!token || !dispositivoId) {
            alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
            navigate('/login');
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
        } else {
            obtenerCapturas();
            obtenerFotos();
        }
    }, [token, dispositivoId, navigate]);

    const obtenerCapturas = async () => {
        try {
            const response = await fetch(`${BASE_URL}/api/dispositivos/${dispositivoId}/capturas-pantalla/`, {
                headers: { Authorization: `Bearer ${token}` }
            });
            if (response.ok) {
                const data = await response.json();
                setCapturas(data);
            } else {
                throw new Error("Error al obtener capturas.");
            }
        } catch (error) {
            setError(error.message);
        }
    };

    const obtenerFotos = async () => {
        try {
            const response = await fetch(`${BASE_URL}/api/dispositivos/${dispositivoId}/fotos/`, {
                headers: { Authorization: `Bearer ${token}` }
            });
            if (response.ok) {
                const data = await response.json();
                setFotos(data);
            } else {
                throw new Error("Error al obtener fotos.");
            }
        } catch (error) {
            setError(error.message);
        }
    };

    const manejarCaptura = async (tipoCaptura) => {
        const url = tipoCaptura === 'pantalla'
            ? `${BASE_URL}/api/dispositivos/${dispositivoId}/capturas-pantalla/`
            : `${BASE_URL}/api/dispositivos/${dispositivoId}/fotos/`;

        try {
            setLoading(true);
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
        }
    }, [token, dispositivoId, navigate]);

    const manejarCaptura = async (url, tipoCaptura) => {
        try {
            mostrarSpinner(true);
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            setLoading(false);

            if (response.ok) {
                tipoCaptura === 'pantalla' ? obtenerCapturas() : obtenerFotos();
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
            mostrarSpinner(false);

            if (response.ok) {
                const data = await response.json();
                tipoCaptura === 'pantalla' ? mostrarCaptura(data.ruta_captura) : mostrarFoto(data.ruta_foto);
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                alert(`${tipoCaptura.charAt(0).toUpperCase() + tipoCaptura.slice(1)} realizada con éxito!`);
            } else {
                const errorData = await response.json();
                alert(`Error al realizar la ${tipoCaptura}: ${errorData.error || 'Desconocido'}`);
            }
        } catch (error) {
<<<<<<< HEAD
            setLoading(false);
=======
<<<<<<< HEAD
            setLoading(false);
=======
<<<<<<< HEAD
            setLoading(false);
=======
            mostrarSpinner(false);
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            console.error(`Error al realizar la ${tipoCaptura}:`, error);
            alert('Error de conexión.');
        }
    };

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    return (
        <div className="main-content">
            <div className="content-header">
                <h2>Capturas</h2>
                <UserMenu />
            </div>

            {error && <p className="error-message">{error}</p>}

            <div className="mb-3">
                <button
                    className="btn btn-primary"
                    onClick={() => manejarCaptura('pantalla')}
                >
                    <FontAwesomeIcon icon={faDesktop} /> Capturar Pantalla
                </button>
                <button
                    className="btn btn-secondary"
                    onClick={() => manejarCaptura('foto')}
                >
                    <FontAwesomeIcon icon={faCamera} /> Tomar Foto
                </button>
                {loading && <div className="spinner-border text-info" role="status">
                    <span className="sr-only">Procesando...</span>
                </div>}
            </div>

            <div className="preview" id="preview-section">
                <h3>Capturas de Pantalla</h3>
                {capturas.map((captura) => (
                    <img key={captura.id} src={`${BASE_URL}${captura.archivo_captura}`} alt="Captura de Pantalla" className="preview-image" />
                ))}
                <h3>Fotos</h3>
                {fotos.map((foto) => (
                    <img key={foto.id} src={`${BASE_URL}${foto.archivo_foto}`} alt="Foto" className="preview-image" />
                ))}
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
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
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            </div>
        </div>
    );
};

export default Capturas;
