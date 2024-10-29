// src/components/UbicacionTiempoReal.js

import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import UserIcon from '../assets/img/cuenta.png';
import '../css/Ubicacion.css';

const UbicacionTiempoReal = () => {
    const navigate = useNavigate();
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const token = localStorage.getItem('access_token');
    const mapRef = useRef(null);  // Ref para almacenar el mapa
    const markerRef = useRef(null);  // Ref para almacenar el marcador

    if (!dispositivoId) {
        alert('No se ha seleccionado un dispositivo.');
        navigate('/mis_dispositivos');
    }

    useEffect(() => {
        if (!token) {
            alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
            navigate('/login');
        }
    }, [navigate, token]);

    // Inicializar Google Map
    useEffect(() => {
        const initMap = () => {
            const loadingMessage = document.getElementById('loading-map');
            mapRef.current = new window.google.maps.Map(document.getElementById('map'), {
                center: { lat: 0, lng: 0 },
                zoom: 15,
            });
            markerRef.current = new window.google.maps.Marker({
                position: { lat: 0, lng: 0 },
                map: mapRef.current,
            });

            window.google.maps.event.addListenerOnce(mapRef.current, 'idle', () => {
                loadingMessage.style.display = 'none';
            });
        };
        
        initMap();
        
        const interval = setInterval(() => {
            obtenerUbicacionActual();
            obtenerHistorialUbicaciones();
        }, 10000);

        return () => clearInterval(interval);
    }, []);

    // Obtener y actualizar la ubicación actual
    const obtenerUbicacionActual = async () => {
        try {
            const response = await fetch(`/api/dispositivos/${dispositivoId}/ubicaciones/`, {
                method: 'GET',
                headers: { 'Authorization': `Bearer ${token}` },
            });

            if (response.ok) {
                const data = await response.json();
                if (data.length > 0) {
                    const ubicacionActual = data[data.length - 1];
                    const latLng = {
                        lat: parseFloat(ubicacionActual.latitud),
                        lng: parseFloat(ubicacionActual.longitud),
                    };
                    mapRef.current.setCenter(latLng);
                    markerRef.current.setPosition(latLng);
                }
            } else {
                console.error("Error al obtener la ubicación actual");
            }
        } catch (error) {
            console.error("Error al actualizar la ubicación:", error);
        }
    };

    // Obtener historial de ubicaciones
    const obtenerHistorialUbicaciones = async () => {
        const loadingMessage = document.getElementById('loading-historial');
        try {
            const response = await fetch(`/api/dispositivos/${dispositivoId}/ubicaciones/`, {
                method: 'GET',
                headers: { 'Authorization': `Bearer ${token}` },
            });

            if (response.ok) {
                const data = await response.json();
                const historial = document.getElementById('historial-ubicaciones');
                historial.innerHTML = '';
                data.forEach((ubicacion, index) => {
                    historial.innerHTML += `
                        <tr>
                            <td>${index + 1}</td>
                            <td>${ubicacion.latitud}</td>
                            <td>${ubicacion.longitud}</td>
                            <td>${ubicacion.fecha}</td>
                            <td>${ubicacion.hora}</td>
                        </tr>
                    `;
                });
                loadingMessage.style.display = 'none';
            } else {
                throw new Error("Error al obtener el historial de ubicaciones");
            }
        } catch (error) {
            console.error("Error al obtener el historial:", error);
            loadingMessage.textContent = 'Error al cargar el historial de ubicaciones.';
        }
    };

    const toggleUserDropdown = () => {
        const dropdown = document.getElementById('user-dropdown');
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    };

    const logout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        alert('Has cerrado sesión.');
        navigate('/login');
    };

    return (
        <div className="main-content">
            <div className="content-header">
                <h2>Ubicación en Tiempo Real</h2>
                <div className="user-info">
                    <img src={UserIcon} alt="User Icon" id="user-icon" onClick={toggleUserDropdown} />
                    <div className="user-dropdown" id="user-dropdown">
                        <a href="/cuenta">Mi Cuenta</a>
                        <a href="/login" onClick={logout}>Cerrar Sesión</a>
                    </div>
                </div>
            </div>

            <div className="map-container">
                <div id="map"></div>
                <p className="loading-message" id="loading-map">Cargando mapa...</p>
            </div>

            <h3>Historial de Ubicaciones</h3>
            <p className="loading-message" id="loading-historial">Cargando historial de ubicaciones...</p>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Latitud</th>
                        <th>Longitud</th>
                        <th>Fecha</th>
                        <th>Hora</th>
                    </tr>
                </thead>
                <tbody id="historial-ubicaciones">
                    {/* Se carga dinámicamente el historial */}
                </tbody>
            </table>
        </div>
    );
};

export default UbicacionTiempoReal;
