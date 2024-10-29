// src/components/GrabacionTiempoReal.js
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import UserIcon from '../assets/img/cuenta.png';
import '../css/GrabacionTiempoReal.css';

const GrabacionTiempoReal = () => {
    const navigate = useNavigate();
    const [grabacionesLlamadas, setGrabacionesLlamadas] = useState([]);
    const [grabacionesPantalla, setGrabacionesPantalla] = useState([]);
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const token = localStorage.getItem('access_token');

    useEffect(() => {
        if (!token || !dispositivoId) {
            alert('Tu sesión ha expirado o no se ha seleccionado un dispositivo.');
            navigate('/login');
        } else {
            obtenerGrabaciones();
        }
    }, [navigate, token, dispositivoId]);

    const obtenerGrabaciones = async () => {
        const llamadasUrl = `/api/dispositivos/${dispositivoId}/grabaciones/llamadas/`;
        const pantallaUrl = `/api/dispositivos/${dispositivoId}/grabaciones/pantalla/`;

        try {
            const [llamadasResponse, pantallaResponse] = await Promise.all([
                fetch(llamadasUrl, { headers: { Authorization: `Bearer ${token}` } }),
                fetch(pantallaUrl, { headers: { Authorization: `Bearer ${token}` } }),
            ]);
            if (llamadasResponse.ok && pantallaResponse.ok) {
                setGrabacionesLlamadas(await llamadasResponse.json());
                setGrabacionesPantalla(await pantallaResponse.json());
            } else {
                console.error("Error al obtener las grabaciones.");
            }
        } catch (error) {
            console.error("Error al obtener las grabaciones:", error);
        }
    };

    const iniciarGrabacion = async (tipo) => {
        const url = tipo === 'llamada'
            ? `/api/dispositivos/${dispositivoId}/grabar-llamada/`
            : `/api/dispositivos/${dispositivoId}/grabar-pantalla/`;

        try {
            const response = await fetch(url, { method: 'POST', headers: { Authorization: `Bearer ${token}` } });
            if (response.ok) {
                alert(`Grabación de ${tipo} iniciada.`);
                obtenerGrabaciones();
            } else {
                alert(`Error al iniciar la grabación de ${tipo}.`);
            }
        } catch (error) {
            console.error(`Error al iniciar la grabación de ${tipo}:`, error);
        }
    };

    const detenerGrabacion = async (tipo) => {
        const url = tipo === 'llamada'
            ? `/api/dispositivos/${dispositivoId}/detener-grabacion/`
            : `/api/dispositivos/${dispositivoId}/detener-grabacion-pantalla/`;

        try {
            const response = await fetch(url, { method: 'POST', headers: { Authorization: `Bearer ${token}` } });
            if (response.ok) {
                alert(`Grabación de ${tipo} detenida.`);
                obtenerGrabaciones();
            } else {
                alert(`Error al detener la grabación de ${tipo}.`);
            }
        } catch (error) {
            console.error(`Error al detener la grabación de ${tipo}:`, error);
        }
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
        <div className="main-content">
            <div className="content-header">
                <h2>Grabación en Tiempo Real</h2>
                <div className="user-info">
                    <img src={UserIcon} alt="User Icon" id="user-icon" onClick={toggleUserDropdown} />
                    <div className="user-dropdown" id="user-dropdown">
                        <a href="/cuenta">Mi Cuenta</a>
                        <a onClick={logout}>Cerrar Sesión</a>
                    </div>
                </div>
            </div>

            <div className="grabacion-section">
                <h4 className="section-title">Grabación de Llamadas</h4>
                <button className="btn btn-danger" onClick={() => iniciarGrabacion('llamada')}>Iniciar Grabación</button>
                <button className="btn btn-secondary" onClick={() => detenerGrabacion('llamada')}>Detener Grabación</button>
                <ul className="list-group recordings-section">
                    {grabacionesLlamadas.map((grabacion, index) => (
                        <li key={index} className="list-group-item">
                            <span>{grabacion.fecha} - {grabacion.hora}</span>
                            <audio controls src={grabacion.archivo_audio}></audio>
                        </li>
                    ))}
                </ul>
            </div>

            <div className="grabacion-section mt-5">
                <h4 className="section-title">Grabación de Pantalla</h4>
                <button className="btn btn-danger" onClick={() => iniciarGrabacion('pantalla')}>Iniciar Grabación</button>
                <button className="btn btn-secondary" onClick={() => detenerGrabacion('pantalla')}>Detener Grabación</button>
                <ul className="list-group recordings-section">
                    {grabacionesPantalla.map((grabacion, index) => (
                        <li key={index} className="list-group-item">
                            <span>{grabacion.fecha} - {grabacion.hora}</span>
                            <video controls width="320" src={grabacion.archivo_video}></video>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default GrabacionTiempoReal;
