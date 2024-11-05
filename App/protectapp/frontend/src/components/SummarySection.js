// src/components/SummarySection.js
<<<<<<< HEAD
import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

const SummarySection = () => {
    const [dispositivosActivos, setDispositivosActivos] = useState(0);
    const [eventosTotales, setEventosTotales] = useState(0);
    const [ultimaActividad, setUltimaActividad] = useState('Sin actividad registrada');
    const [loading, setLoading] = useState(true);
    const location = useLocation();

    useEffect(() => {
        if (location.pathname) {
            console.log("Cambio de ruta:", location.pathname);
            cargarDatos();
        }
    }, [location.pathname]);

    const cargarDatos = async () => {
        setLoading(true);
        try {
            await Promise.all([
                cargarDispositivosActivos(),
                cargarEventosTotales(),
                cargarUltimaActividadUsuario() // Cambiado a la función de última actividad del usuario
            ]);
        } catch (error) {
            console.error("Error al cargar datos:", error);
        } finally {
            setLoading(false);
        }
    };

    const cargarDispositivosActivos = async () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
            console.error("Token de acceso no encontrado.");
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/dispositivos/activos/', {
                method: 'GET',
                headers: { 'Authorization': `Bearer ${token}` },
            });
            if (response.ok) {
                const data = await response.json();
                console.log("Dispositivos activos recibidos:", data.cantidad);
                setDispositivosActivos(data.cantidad);
            } else {
                console.error('Error al obtener la cantidad de dispositivos activos');
            }
        } catch (error) {
            console.error('Error al conectar con el servidor:', error);
        }
    };

    const cargarEventosTotales = async () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
            console.error("Token de acceso no encontrado.");
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/eventos/totales/', {
                method: 'GET',
                headers: { 'Authorization': `Bearer ${token}` },
            });
            if (response.ok) {
                const data = await response.json();
                console.log("Eventos totales recibidos:", data.total);
                setEventosTotales(data.total);
            } else {
                console.error('Error al obtener el total de eventos');
            }
        } catch (error) {
            console.error('Error al conectar con el servidor:', error);
        }
    };

    const cargarUltimaActividadUsuario = async () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
            console.error("Token de acceso no encontrado.");
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/actividad/ultima/', {
                method: 'GET',
                headers: { 'Authorization': `Bearer ${token}` },
            });
            if (response.ok) {
                const data = await response.json();
                console.log("Última actividad recibida:", data.ultima_actividad);
                setUltimaActividad(data.ultima_actividad || "Sin actividad registrada");
            } else {
                console.error('Error al obtener la última actividad');
            }
        } catch (error) {
            console.error('Error al conectar con el servidor:', error);
        }
    };

    return (
        <div className="summary-section">
            {loading ? (
                <p>Cargando datos...</p>
            ) : (
                <>
                    <div className="summary-card">
                        <h4>Dispositivos Activos</h4>
                        <p><i className="fas fa-mobile-alt"></i> {dispositivosActivos} Dispositivos</p>
                    </div>
                    <div className="summary-card">
                        <h4>Eventos Totales</h4>
                        <p><i className="fas fa-bell"></i> {eventosTotales} Eventos</p>
                    </div>
                    <div className="summary-card">
                        <h4>Última Actividad</h4>
                        <p><i className="fas fa-clock"></i> {ultimaActividad}</p>
                    </div>
                </>
            )}
=======
import React from 'react';

const SummarySection = () => {
    return (
        <div className="summary-section">
        <div className="summary-card">
            <h4>Dispositivos Activos</h4>
            <p><i className="fas fa-mobile-alt"></i> 3 Dispositivos</p>
        </div>
        <div className="summary-card">
            <h4>Alertas Recientes</h4>
            <p><i className="fas fa-exclamation-circle"></i> 2 Alertas</p>
        </div>
        <div className="summary-card">
            <h4>Última Actividad</h4>
            <p><i className="fas fa-clock"></i> Hace 2 horas</p>
        </div>
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
        </div>
    );
};

export default SummarySection;
