// src/components/GrabacionTiempoReal.js
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
import UserMenu from './UserMenu';
import '../css/GrabacionTiempoReal.css';

const BASE_URL = "http://127.0.0.1:8000";

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
import UserIcon from '../assets/img/cuenta.png';
import '../css/GrabacionTiempoReal.css';

>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
const GrabacionTiempoReal = () => {
    const navigate = useNavigate();
    const [grabacionesLlamadas, setGrabacionesLlamadas] = useState([]);
    const [grabacionesPantalla, setGrabacionesPantalla] = useState([]);
<<<<<<< HEAD
    const [loadingLlamadas, setLoadingLlamadas] = useState(true);
    const [loadingPantalla, setLoadingPantalla] = useState(true);
    const [error, setError] = useState(null);
=======
<<<<<<< HEAD
    const [loadingLlamadas, setLoadingLlamadas] = useState(true);
    const [loadingPantalla, setLoadingPantalla] = useState(true);
    const [error, setError] = useState(null);
=======
<<<<<<< HEAD
    const [loadingLlamadas, setLoadingLlamadas] = useState(true);
    const [loadingPantalla, setLoadingPantalla] = useState(true);
    const [error, setError] = useState(null);
=======
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
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

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    // Función para obtener las grabaciones de llamadas y pantalla
    const obtenerGrabaciones = async () => {
        const llamadasUrl = `${BASE_URL}/api/dispositivos/${dispositivoId}/grabaciones/llamadas/`;
        const pantallaUrl = `${BASE_URL}/api/dispositivos/${dispositivoId}/grabaciones/pantalla/`;

        try {
            setLoadingLlamadas(true);
            setLoadingPantalla(true);

            const [llamadasResponse, pantallaResponse] = await Promise.all([
                fetch(llamadasUrl, { 
                    headers: { 
                        Authorization: `Bearer ${token}`,
                        'Content-Type': 'application/json' 
                    } 
                }),
                fetch(pantallaUrl, { 
                    headers: { 
                        Authorization: `Bearer ${token}`,
                        'Content-Type': 'application/json' 
                    } 
                }),
            ]);

            // Verificar respuesta de llamadas
            if (llamadasResponse.ok) {
                const llamadasData = await llamadasResponse.json();
                setGrabacionesLlamadas(llamadasData);
            } else {
                throw new Error("Error al obtener las grabaciones de llamadas.");
            }

            // Verificar respuesta de pantalla
            if (pantallaResponse.ok) {
                const pantallaData = await pantallaResponse.json();
                setGrabacionesPantalla(pantallaData);
            } else {
                throw new Error("Error al obtener las grabaciones de pantalla.");
            }
        } catch (error) {
            console.error("Error al obtener las grabaciones:", error);
            setError("Error al obtener las grabaciones. Verifica que las rutas del backend sean correctas y que el backend esté activo.");
        } finally {
            setLoadingLlamadas(false);
            setLoadingPantalla(false);
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
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
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
        }
    };

    const iniciarGrabacion = async (tipo) => {
        const url = tipo === 'llamada'
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            ? `${BASE_URL}/api/dispositivos/${dispositivoId}/grabar-llamada/`
            : `${BASE_URL}/api/dispositivos/${dispositivoId}/grabar-pantalla/`;

        try {
            const response = await fetch(url, { 
                method: 'POST', 
                headers: { 
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'application/json' 
                } 
            });
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
            ? `/api/dispositivos/${dispositivoId}/grabar-llamada/`
            : `/api/dispositivos/${dispositivoId}/grabar-pantalla/`;

        try {
            const response = await fetch(url, { method: 'POST', headers: { Authorization: `Bearer ${token}` } });
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            if (response.ok) {
                alert(`Grabación de ${tipo} iniciada.`);
                obtenerGrabaciones();
            } else {
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                const errorData = await response.json();
                alert(`Error al iniciar la grabación de ${tipo}: ${errorData.message || "No se pudo iniciar la grabación."}`);
            }
        } catch (error) {
            console.error(`Error al iniciar la grabación de ${tipo}:`, error);
            alert(`Error al iniciar la grabación de ${tipo}. Verifica que el backend esté activo y las rutas sean correctas.`);
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
                alert(`Error al iniciar la grabación de ${tipo}.`);
            }
        } catch (error) {
            console.error(`Error al iniciar la grabación de ${tipo}:`, error);
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
        }
    };

    const detenerGrabacion = async (tipo) => {
        const url = tipo === 'llamada'
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            ? `${BASE_URL}/api/dispositivos/${dispositivoId}/detener-grabacion/`
            : `${BASE_URL}/api/dispositivos/${dispositivoId}/detener-grabacion-pantalla/`;

        try {
            const response = await fetch(url, { 
                method: 'POST', 
                headers: { 
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'application/json' 
                } 
            });
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
            ? `/api/dispositivos/${dispositivoId}/detener-grabacion/`
            : `/api/dispositivos/${dispositivoId}/detener-grabacion-pantalla/`;

        try {
            const response = await fetch(url, { method: 'POST', headers: { Authorization: `Bearer ${token}` } });
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            if (response.ok) {
                alert(`Grabación de ${tipo} detenida.`);
                obtenerGrabaciones();
            } else {
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                const errorData = await response.json();
                alert(`Error al detener la grabación de ${tipo}: ${errorData.message || "No se pudo detener la grabación."}`);
            }
        } catch (error) {
            console.error(`Error al detener la grabación de ${tipo}:`, error);
            alert(`Error al detener la grabación de ${tipo}. Verifica que el backend esté activo y las rutas sean correctas.`);
        }
    };

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
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

>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    return (
        <div className="main-content">
            <div className="content-header">
                <h2>Grabación en Tiempo Real</h2>
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                <UserMenu /> {/* Aquí se incluye el componente UserMenu */}
            </div>

            {error && <p className="error-message">{error}</p>}

            {/* Sección de grabación de llamadas */}
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
                <div className="user-info">
                    <img src={UserIcon} alt="User Icon" id="user-icon" onClick={toggleUserDropdown} />
                    <div className="user-dropdown" id="user-dropdown">
                        <a href="/cuenta">Mi Cuenta</a>
                        <a onClick={logout}>Cerrar Sesión</a>
                    </div>
                </div>
            </div>

>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            <div className="grabacion-section">
                <h4 className="section-title">Grabación de Llamadas</h4>
                <button className="btn btn-danger" onClick={() => iniciarGrabacion('llamada')}>Iniciar Grabación</button>
                <button className="btn btn-secondary" onClick={() => detenerGrabacion('llamada')}>Detener Grabación</button>
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                {loadingLlamadas ? (
                    <p className="loading-message">Cargando grabaciones de llamadas...</p>
                ) : grabacionesLlamadas.length === 0 ? (
                    <p className="no-data-message">No hay grabaciones de llamadas disponibles.</p>
                ) : (
                    <ul className="list-group recordings-section">
                        {grabacionesLlamadas.map((grabacion) => (
                            <li key={grabacion.id} className="list-group-item">
                                <span>{grabacion.fecha} - {grabacion.hora}</span>
                                <audio controls src={`${BASE_URL}${grabacion.archivo_audio}`}></audio>
                            </li>
                        ))}
                    </ul>
                )}
            </div>

            {/* Sección de grabación de pantalla */}
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
                <ul className="list-group recordings-section">
                    {grabacionesLlamadas.map((grabacion, index) => (
                        <li key={index} className="list-group-item">
                            <span>{grabacion.fecha} - {grabacion.hora}</span>
                            <audio controls src={grabacion.archivo_audio}></audio>
                        </li>
                    ))}
                </ul>
            </div>

>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            <div className="grabacion-section mt-5">
                <h4 className="section-title">Grabación de Pantalla</h4>
                <button className="btn btn-danger" onClick={() => iniciarGrabacion('pantalla')}>Iniciar Grabación</button>
                <button className="btn btn-secondary" onClick={() => detenerGrabacion('pantalla')}>Detener Grabación</button>
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                {loadingPantalla ? (
                    <p className="loading-message">Cargando grabaciones de pantalla...</p>
                ) : grabacionesPantalla.length === 0 ? (
                    <p className="no-data-message">No hay grabaciones de pantalla disponibles.</p>
                ) : (
                    <ul className="list-group recordings-section">
                        {grabacionesPantalla.map((grabacion) => (
                            <li key={grabacion.id} className="list-group-item">
                                <span>{grabacion.fecha} - {grabacion.hora}</span>
                                <video controls width="320" src={`${BASE_URL}${grabacion.archivo_video}`}></video>
                            </li>
                        ))}
                    </ul>
                )}
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
                <ul className="list-group recordings-section">
                    {grabacionesPantalla.map((grabacion, index) => (
                        <li key={index} className="list-group-item">
                            <span>{grabacion.fecha} - {grabacion.hora}</span>
                            <video controls width="320" src={grabacion.archivo_video}></video>
                        </li>
                    ))}
                </ul>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            </div>
        </div>
    );
};

export default GrabacionTiempoReal;
