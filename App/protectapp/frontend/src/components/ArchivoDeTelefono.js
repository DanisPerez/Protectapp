// src/components/ArchivoDeTelefono.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import SidebarEventos from './SidebarEventos';
import UserIcon from '../assets/img/cuenta.png'; 
import '../css/PhoneArchive.css';

const ArchivoDeTelefono = () => {
    const [activeTab, setActiveTab] = useState('llamadas');
    const [data, setData] = useState({ llamadas: [], mensajes: [], contactos: [], fotos: [], videos: [] });
    const [loadingMessage, setLoadingMessage] = useState('');

    // Verificación y configuración del dispositivo seleccionado
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    if (!dispositivoId) {
        alert('No se ha seleccionado un dispositivo.');
        window.location.href = '/mis_dispositivos';
    }

    const fetchData = async (endpoint) => {
        const token = localStorage.getItem('access_token');
        try {
            const response = await fetch(`http://localhost:8000/api/dispositivos/${dispositivoId}/${endpoint}/`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) throw new Error('Network response was not ok');
            return await response.json();
        } catch (error) {
            console.error(`Error fetching ${endpoint}:`, error);
            setLoadingMessage('Error al obtener los datos');
            throw error;
        }
    };

    const loadTabData = async (tab) => {
        setLoadingMessage(`Cargando ${tab}...`);
        try {
            const tabData = await fetchData(tab);
            setData((prevData) => ({ ...prevData, [tab]: tabData }));
            setLoadingMessage('');
        } catch {
            setLoadingMessage('Error al cargar los datos');
        }
    };

    useEffect(() => {
        loadTabData(activeTab);
    }, [activeTab]);

    return (
        <div className="main-layout">
            <SidebarEventos />
            <div className="main-content">
                <div className="content-header">
                    <h2>Archivo de Teléfono</h2>
                    <div className="user-info">
                        <img src={UserIcon} alt="User Icon" id="user-icon" onClick={() => {
                            const dropdown = document.getElementById("user-dropdown");
                            dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
                        }} />
                        <div className="user-dropdown" id="user-dropdown">
                            <Link to="/cuenta">Mi Cuenta</Link>
                            <Link to="/login" onClick={() => {
                                localStorage.removeItem('access_token');
                                window.location.href = "/login";
                            }}>Cerrar Sesión</Link>
                        </div>
                    </div>
                </div>

                {/* Navegación entre pestañas */}
                <ul className="nav nav-tabs">
                    {['llamadas', 'mensajes', 'contactos', 'fotos', 'videos'].map((tab) => (
                        <li className="nav-item" key={tab}>
                            <button
                                className={`nav-link ${activeTab === tab ? 'active' : ''}`}
                                onClick={() => setActiveTab(tab)}
                            >
                                {tab.charAt(0).toUpperCase() + tab.slice(1)}
                            </button>
                        </li>
                    ))}
                </ul>

                {/* Contenido de las pestañas */}
                <div className="tab-content">
                    {loadingMessage && <p className="loading-message">{loadingMessage}</p>}
                    <div className="tab-pane fade show active">
                        {activeTab === 'llamadas' && (
                            <table className="table">
                                <thead>
                                    <tr><th>#</th><th>Número</th><th>Duración</th><th>Fecha</th><th>Hora</th><th>Tipo</th></tr>
                                </thead>
                                <tbody>
                                    {data.llamadas.map((llamada, index) => (
                                        <tr key={index}>
                                            <td>{index + 1}</td>
                                            <td>{llamada.numero}</td>
                                            <td>{llamada.duracion} seg</td>
                                            <td>{llamada.fecha}</td>
                                            <td>{llamada.hora}</td>
                                            <td>{llamada.tipo}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        )}

                        {activeTab === 'mensajes' && (
                            <table className="table">
                                <thead>
                                    <tr><th>#</th><th>Número</th><th>Contenido</th><th>Fecha</th><th>Hora</th><th>Tipo</th></tr>
                                </thead>
                                <tbody>
                                    {data.mensajes.map((mensaje, index) => (
                                        <tr key={index}>
                                            <td>{index + 1}</td>
                                            <td>{mensaje.numero}</td>
                                            <td>{mensaje.contenido}</td>
                                            <td>{mensaje.fecha}</td>
                                            <td>{mensaje.hora}</td>
                                            <td>{mensaje.tipo}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        )}

                        {activeTab === 'contactos' && (
                            <ul className="list-group">
                                {data.contactos.map((contacto, index) => (
                                    <li className="list-group-item" key={index}>
                                        {contacto.nombre} - {contacto.numero}
                                    </li>
                                ))}
                            </ul>
                        )}

                        {activeTab === 'fotos' && (
                            <div className="media-container">
                                {data.fotos.map((foto, index) => (
                                    <img src={foto.ruta_foto} alt={`Foto ${index + 1}`} key={index} />
                                ))}
                            </div>
                        )}

                        {activeTab === 'videos' && (
                            <div className="media-container">
                                {data.videos.map((video, index) => (
                                    <video src={video.ruta_video} controls key={index}></video>
                                ))}
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ArchivoDeTelefono;
