<<<<<<< HEAD
// VerificacionPermisos.js
import React, { useEffect, useState } from 'react';
import SidebarEventos from './SidebarEventos';
import UserMenu from './UserMenu';
=======
import React, { useEffect, useState } from 'react';
import SidebarEventos from './SidebarEventos';
<<<<<<< HEAD
import UserMenu from './UserMenu'; // Importamos el componente UserMenu
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
import { useNavigate } from 'react-router-dom';
import '../css/verificacion_permisos.css';

const BASE_URL = "http://127.0.0.1:8000";

const VerificacionPermisos = () => {
    const [permisos, setPermisos] = useState([]);
    const [loading, setLoading] = useState(false);
<<<<<<< HEAD
    const [showInstructions, setShowInstructions] = useState(null); 
    const token = localStorage.getItem('access_token');
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const navigate = useNavigate();
=======
    const token = localStorage.getItem('access_token');
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const navigate = useNavigate();
=======
import { useNavigate } from 'react-router-dom';
import UserIcon from '../assets/img/cuenta.png';
import '../css/verificacion_permisos.css';

const VerificacionPermisos = () => {
    const [permisos, setPermisos] = useState([]);
    const token = localStorage.getItem('access_token');
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

    useEffect(() => {
        if (!token || !dispositivoId) {
            alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
            navigate('/login');
        } else {
            obtenerPermisos();
        }
    }, [token, dispositivoId, navigate]);

    const obtenerPermisos = async () => {
        setLoading(true);
        try {
<<<<<<< HEAD
            const response = await fetch(`${BASE_URL}/api/dispositivos/${dispositivoId}/verificacion-permisos/`, {
=======
<<<<<<< HEAD
            const response = await fetch(`${BASE_URL}/api/dispositivos/${dispositivoId}/verificacion-permisos/`, {
=======
            const response = await fetch(`/api/dispositivos/${dispositivoId}/verificacion-permisos/`, {
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                method: 'GET',
                headers: { Authorization: `Bearer ${token}` },
            });

            if (!response.ok) throw new Error('Error al obtener los permisos');
            const permisosData = await response.json();
            setPermisos(permisosData);
        } catch (error) {
            console.error('Error al obtener los permisos:', error);
            alert('Error al cargar los permisos.');
        } finally {
            setLoading(false);
        }
    };

<<<<<<< HEAD
    const handleViewInstructions = (instrucciones) => {
        setShowInstructions(instrucciones); // Muestra las instrucciones en el modal
    };

    const closeInstructionsModal = () => {
        setShowInstructions(null);
    };

=======
    const solicitarPermiso = async (permisoId) => {
        try {
<<<<<<< HEAD
            const response = await fetch(`${BASE_URL}/api/dispositivos/${dispositivoId}/solicitar-permiso/${permisoId}/`, {
=======
            const response = await fetch(`/api/dispositivos/${dispositivoId}/solicitar-permiso/${permisoId}/`, {
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
                method: 'POST',
                headers: {
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                alert('Permiso solicitado exitosamente');
                obtenerPermisos();
            } else {
                alert('Error al solicitar el permiso.');
            }
        } catch (error) {
            console.error('Error al solicitar el permiso:', error);
            alert('Error al solicitar el permiso.');
        }
    };

<<<<<<< HEAD
=======
    const logout = () => {
        localStorage.clear();
        navigate('/login');
    };

>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    return (
        <div className="main-layout">
            <SidebarEventos />
            <div className="main-content">
                <div className="content-header">
                    <h2>Verificación de Permisos</h2>
<<<<<<< HEAD
                    <UserMenu /> 
=======
<<<<<<< HEAD
                    <UserMenu /> {/* Reemplazamos el dropdown de usuario con UserMenu */}
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                </div>

                {loading ? (
                    <div className="loading-container">
                        <div className="spinner-border text-info" role="status">
                            <span className="sr-only">Cargando permisos...</span>
                        </div>
<<<<<<< HEAD
=======
=======
                    <div className="user-info">
                        <img src={UserIcon} alt="User Icon" id="user-icon" />
                        <div className="user-dropdown" id="user-dropdown">
                            <a href="/cuenta">Mi Cuenta</a>
                            <button onClick={logout}>Cerrar Sesión</button>
                        </div>
                    </div>
                </div>

                {loading ? (
                    <div className="spinner-border text-info" role="status">
                        <span className="sr-only">Cargando permisos...</span>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                    </div>
                ) : (
                    <div className="table-permisos">
                        <h4>Estado de Permisos</h4>
                        <table className="table table-striped">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Permiso</th>
                                    <th>Tipo de Permiso</th>
                                    <th>Estado</th>
<<<<<<< HEAD
                                    <th>Acción</th>
                                    <th>Crítico</th>
                                    <th>Última Verificación</th>
=======
<<<<<<< HEAD
                                    <th>Acción</th>
                                    <th>Crítico</th>
                                    <th>Última Verificación</th>
=======
                                    <th>Crítico</th>
                                    <th>Fecha de Verificación</th>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                                </tr>
                            </thead>
                            <tbody>
                                {permisos.length > 0 ? (
                                    permisos.map((permiso, index) => (
                                        <tr key={permiso.id}>
                                            <td>{index + 1}</td>
                                            <td>{permiso.permiso}</td>
                                            <td>{permiso.tipo_permiso || 'No disponible'}</td>
<<<<<<< HEAD
                                            <td>{permiso.estado_permiso ? 'Concedido' : 'Denegado'}</td> 
                                            <td>
                                                {!permiso.estado_permiso && ( 
                                                    <button
                                                        className="btn btn-info btn-sm"
                                                        onClick={() => handleViewInstructions(permiso.instrucciones)}
                                                    >
                                                        Ver
                                                    </button>
                                                )}
                                            </td>
=======
<<<<<<< HEAD
                                            <td>{permiso.estado_permiso ? 'Concedido' : 'Denegado'}</td> {/* Campo corregido */}
                                            <td>
                                                {!permiso.estado_permiso && ( /* Campo corregido */
                                                    <button
                                                        className="btn btn-warning btn-sm"
                                                        onClick={() => solicitarPermiso(permiso.id)}
                                                    >
                                                        Solicitar
                                                    </button>
                                                )}
                                            </td>
=======
                                            <td>{permiso.estado ? 'Concedido' : 'Denegado'}</td>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                                            <td>{permiso.critico ? 'Sí' : 'No'}</td>
                                            <td>{permiso.fecha_verificacion || 'No disponible'}</td>
                                        </tr>
                                    ))
                                ) : (
                                    <tr>
<<<<<<< HEAD
                                        <td colSpan="7" className="text-center">
                                            No hay permisos disponibles para verificar.
                                        </td>
=======
<<<<<<< HEAD
                                        <td colSpan="7" className="text-center">
                                            No hay permisos disponibles para verificar.
                                        </td>
=======
                                        <td colSpan="6" className="text-center">No hay permisos disponibles.</td>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                )}
<<<<<<< HEAD

                {showInstructions && (
                    <div className="modal-overlay" onClick={closeInstructionsModal}>
                        <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                            <span className="close" onClick={closeInstructionsModal}>&times;</span>
                            <h5>Instrucciones para Conceder Permiso</h5>
                            <p>{showInstructions}</p>
                        </div>
                    </div>
                )}
=======
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            </div>
        </div>
    );
};

export default VerificacionPermisos;
