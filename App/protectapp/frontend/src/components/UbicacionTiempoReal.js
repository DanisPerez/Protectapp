import React, { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import UserMenu from './UserMenu';
import '../css/Ubicacion.css';

const UbicacionTiempoReal = () => {
    const navigate = useNavigate();
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const token = localStorage.getItem('access_token');
    const mapRef = useRef(null);
    const markerRef = useRef(null);
    const [historial, setHistorial] = useState([]);
    const [loadingMap, setLoadingMap] = useState(true);
    const [loadingHistorial, setLoadingHistorial] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (!dispositivoId) {
            alert('No se ha seleccionado un dispositivo.');
            navigate('/mis_dispositivos');
            return;
        }

        if (!token) {
            alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
            navigate('/login');
            return;
        }

        const initMap = () => {
            mapRef.current = new window.google.maps.Map(document.getElementById('map'), {
                center: { lat: 0, lng: 0 },
                zoom: 15,
            });

            markerRef.current = new window.google.maps.Marker({
                position: { lat: 0, lng: 0 },
                map: mapRef.current,
            });

            window.google.maps.event.addListenerOnce(mapRef.current, 'idle', () => {
                setLoadingMap(false);
            });
        };

        // Verificar si Google Maps está cargado
        const checkGoogleMaps = () => {
            if (window.google && window.google.maps) {
                initMap();
            } else {
                console.error("Google Maps no está disponible. Verifica tu clave API.");
            }
        };

        // Esperar a que el script se cargue y luego intentar inicializar el mapa
        if (!window.google || !window.google.maps) {
            console.log("Esperando carga de Google Maps...");
            const intervalId = setInterval(() => {
                if (window.google && window.google.maps) {
                    clearInterval(intervalId);
                    initMap();
                }
            }, 1000); // Revisar cada segundo
        } else {
            initMap();
        }

        obtenerHistorialUbicaciones();

    }, [dispositivoId, token, navigate]);

    const obtenerHistorialUbicaciones = async () => {
        console.log("Iniciando solicitud para obtener historial de ubicaciones...");
        setLoadingHistorial(true);
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/dispositivos/${dispositivoId}/ubicaciones/`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });
    
            if (response.ok) {
                const data = await response.json();
                console.log("Historial de ubicaciones recibido:", data);
                setHistorial(data);
                setLoadingHistorial(false);
            } else {
                const errMessage = await response.json();
                console.error("Error al obtener el historial de ubicaciones. Estado de respuesta:", response.status);
                setError(errMessage.error || "Error al obtener el historial de ubicaciones");
                setLoadingHistorial(false);
            }
        } catch (error) {
            console.error("Error al obtener el historial de ubicaciones:", error);
            setError("Error al obtener el historial de ubicaciones");
            setLoadingHistorial(false);
        }
    };

    return (
        <div className="main-content">
            <div className="content-header">
                <h2>Ubicación en Tiempo Real</h2>
                <UserMenu />
            </div>

            <div className="map-container">
                <div id="map"></div>
                {loadingMap && <p className="loading-message">Cargando mapa...</p>}
            </div>

            <h3>Historial de Ubicaciones</h3>
            {loadingHistorial ? (
                <p className="loading-message">Cargando historial de ubicaciones...</p>
            ) : error ? (
                <p className="error-message">{error}</p>
            ) : (
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Latitud</th>
                            <th>Longitud</th>
                            <th>Fecha</th>
                            <th>Hora</th>
                        </tr>
                    </thead>
                    <tbody>
                        {historial.map((ubicacion) => (
                            <tr key={ubicacion.id}>
                                <td>{ubicacion.id}</td>
                                <td>{ubicacion.latitud}</td>
                                <td>{ubicacion.longitud}</td>
                                <td>{ubicacion.fecha}</td>
                                <td>{ubicacion.hora}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
};

export default UbicacionTiempoReal;