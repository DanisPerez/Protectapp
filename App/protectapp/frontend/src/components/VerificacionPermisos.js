import React, { useEffect, useState } from 'react';
import SidebarEventos from './SidebarEventos';
import { useNavigate } from 'react-router-dom';
import UserIcon from '../assets/img/cuenta.png';
import '../css/verificacion_permisos.css';

const VerificacionPermisos = () => {
    const [permisos, setPermisos] = useState([]);
    const token = localStorage.getItem('access_token');
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);

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
            const response = await fetch(`/api/dispositivos/${dispositivoId}/verificacion-permisos/`, {
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

    const solicitarPermiso = async (permisoId) => {
        try {
            const response = await fetch(`/api/dispositivos/${dispositivoId}/solicitar-permiso/${permisoId}/`, {
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

    const logout = () => {
        localStorage.clear();
        navigate('/login');
    };

    return (
        <div className="main-layout">
            <SidebarEventos />
            <div className="main-content">
                <div className="content-header">
                    <h2>Verificación de Permisos</h2>
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
                                    <th>Crítico</th>
                                    <th>Fecha de Verificación</th>
                                </tr>
                            </thead>
                            <tbody>
                                {permisos.length > 0 ? (
                                    permisos.map((permiso, index) => (
                                        <tr key={permiso.id}>
                                            <td>{index + 1}</td>
                                            <td>{permiso.permiso}</td>
                                            <td>{permiso.tipo_permiso || 'No disponible'}</td>
                                            <td>{permiso.estado ? 'Concedido' : 'Denegado'}</td>
                                            <td>{permiso.critico ? 'Sí' : 'No'}</td>
                                            <td>{permiso.fecha_verificacion || 'No disponible'}</td>
                                        </tr>
                                    ))
                                ) : (
                                    <tr>
                                        <td colSpan="6" className="text-center">No hay permisos disponibles.</td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                )}
            </div>
        </div>
    );
};

export default VerificacionPermisos;
