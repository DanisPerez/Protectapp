// src/components/Capturas.js
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import UserMenu from './UserMenu';
import '../css/Capturas.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faDesktop, faCamera } from '@fortawesome/free-solid-svg-icons';

const BASE_URL = "http://127.0.0.1:8000";

const Capturas = () => {
    const token = localStorage.getItem('access_token');
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const navigate = useNavigate();
    const [capturas, setCapturas] = useState([]);
    const [fotos, setFotos] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        if (!token || !dispositivoId) {
            alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
            navigate('/login');
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
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });
            setLoading(false);

            if (response.ok) {
                tipoCaptura === 'pantalla' ? obtenerCapturas() : obtenerFotos();
                alert(`${tipoCaptura.charAt(0).toUpperCase() + tipoCaptura.slice(1)} realizada con éxito!`);
            } else {
                const errorData = await response.json();
                alert(`Error al realizar la ${tipoCaptura}: ${errorData.error || 'Desconocido'}`);
            }
        } catch (error) {
            setLoading(false);
            console.error(`Error al realizar la ${tipoCaptura}:`, error);
            alert('Error de conexión.');
        }
    };

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
            </div>
        </div>
    );
};

export default Capturas;
