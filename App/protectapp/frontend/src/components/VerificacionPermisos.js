// VerificacionPermisos.js
import React, { useEffect, useState } from 'react';
import SidebarEventos from './SidebarEventos';
import UserMenu from './UserMenu';
import { useNavigate } from 'react-router-dom';
import '../css/verificacion_permisos.css';

const BASE_URL = "http://127.0.0.1:8000";

const VerificacionPermisos = () => {
    const [permisos, setPermisos] = useState([]);
    const [loading, setLoading] = useState(false);
    const [showInstructions, setShowInstructions] = useState(null); 
    const token = localStorage.getItem('access_token');
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const navigate = useNavigate();

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
            const response = await fetch(`${BASE_URL}/api/dispositivos/${dispositivoId}/verificacion-permisos/`, {
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

    const handleViewInstructions = (instrucciones) => {
        setShowInstructions(instrucciones); // Muestra las instrucciones en el modal
    };

    const closeInstructionsModal = () => {
        setShowInstructions(null);
    };

    return (
        <div className="main-layout">
            <SidebarEventos />
            <div className="main-content">
                <div className="content-header">
                    <h2>Verificación de Permisos</h2>
                    <UserMenu /> 
                </div>

                {loading ? (
                    <div className="loading-container">
                        <div className="spinner-border text-info" role="status">
                            <span className="sr-only">Cargando permisos...</span>
                        </div>
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
                                    <th>Acción</th>
                                    <th>Crítico</th>
                                    <th>Última Verificación</th>
                                </tr>
                            </thead>
                            <tbody>
                                {permisos.length > 0 ? (
                                    permisos.map((permiso, index) => (
                                        <tr key={permiso.id}>
                                            <td>{index + 1}</td>
                                            <td>{permiso.permiso}</td>
                                            <td>{permiso.tipo_permiso || 'No disponible'}</td>
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
                                            <td>{permiso.critico ? 'Sí' : 'No'}</td>
                                            <td>{permiso.fecha_verificacion || 'No disponible'}</td>
                                        </tr>
                                    ))
                                ) : (
                                    <tr>
                                        <td colSpan="7" className="text-center">
                                            No hay permisos disponibles para verificar.
                                        </td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                )}

                {showInstructions && (
                    <div className="modal-overlay" onClick={closeInstructionsModal}>
                        <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                            <span className="close" onClick={closeInstructionsModal}>&times;</span>
                            <h5>Instrucciones para Conceder Permiso</h5>
                            <p>{showInstructions}</p>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default VerificacionPermisos;
