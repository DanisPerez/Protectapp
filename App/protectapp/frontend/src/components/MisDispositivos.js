<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/MisDispositivos.css';
import UserMenu from './UserMenu';
<<<<<<< HEAD
=======
=======
// src/components/MisDispositivos.js
import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import UserIcon from '../assets/img/cuenta.png';
import '../css/MisDispositivos.css';
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

const MisDispositivos = () => {
    const [dispositivos, setDispositivos] = useState([]);
    const [errorMessage, setErrorMessage] = useState('');
    const [nombreDispositivo, setNombreDispositivo] = useState('');
    const [dispositivoSeleccionado, setDispositivoSeleccionado] = useState(null);
<<<<<<< HEAD
    const [showRenameModal, setShowRenameModal] = useState(false);
    const [showDeleteModal, setShowDeleteModal] = useState(false);
    const [deviceToDelete, setDeviceToDelete] = useState(null);
=======
<<<<<<< HEAD
    const [showRenameModal, setShowRenameModal] = useState(false);
    const [showDeleteModal, setShowDeleteModal] = useState(false);
    const [deviceToDelete, setDeviceToDelete] = useState(null);
=======
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    const navigate = useNavigate();

    useEffect(() => {
        checkLogin();
        cargarDispositivos();
    }, []);

    const checkLogin = () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
<<<<<<< HEAD
            alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
            navigate('/login');
=======
<<<<<<< HEAD
            alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
            navigate('/login');
=======
        alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
        navigate('/login');
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
        }
    };

    const cargarDispositivos = async () => {
        const token = localStorage.getItem('access_token');
        try {
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            const response = await fetch('http://localhost:8000/api/dispositivos/', {
                method: 'GET',
                headers: { 'Authorization': `Bearer ${token}` },
            });
            if (response.ok) {
                const data = await response.json();
                setDispositivos(data);
            } else {
                throw new Error('Error al cargar los dispositivos');
            }
        } catch (error) {
            setErrorMessage('Error al cargar los dispositivos');
        }
    };

    const handleCambiarNombre = (dispositivoId, nombreActual) => {
        setDispositivoSeleccionado(dispositivoId);
        setNombreDispositivo(nombreActual);
        setShowRenameModal(true);
<<<<<<< HEAD
=======
=======
        const response = await fetch('/api/dispositivos/', {
            method: 'GET',
            headers: { 'Authorization': `Bearer ${token}` },
        });
        if (response.ok) {
            const data = await response.json();
            setDispositivos(data);
        } else {
            throw new Error('Error al cargar los dispositivos');
        }
        } catch (error) {
        setErrorMessage('Error al cargar los dispositivos');
        }
    };

    const handleCambiarNombre = (dispositivoId) => {
        setDispositivoSeleccionado(dispositivoId);
        setNombreDispositivo(dispositivos.find(d => d.id === dispositivoId).nombre);
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    };

    const handleActualizarNombre = async () => {
        const token = localStorage.getItem('access_token');
        try {
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            const response = await fetch(`http://localhost:8000/api/dispositivos/${dispositivoSeleccionado}/`, {
                method: 'PUT',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ nombre: nombreDispositivo })
            });
            if (response.ok) {
                cargarDispositivos();
                setShowRenameModal(false);
                setDispositivoSeleccionado(null);
            } else {
                throw new Error('Error al actualizar el nombre del dispositivo');
            }
        } catch (error) {
            setErrorMessage('Error al actualizar el nombre del dispositivo');
        }
    };

    const handleDeleteClick = () => {
        setShowDeleteModal(true);
        setDeviceToDelete(null); // reset selected device in delete modal
    };

    const handleConfirmDelete = async () => {
        const token = localStorage.getItem('access_token');
        if (deviceToDelete) {
            const confirmDelete = window.confirm(`¿Estás seguro de que deseas eliminar el dispositivo "${deviceToDelete.nombre}"?`);
            if (confirmDelete) {
                try {
                    const response = await fetch(`http://localhost:8000/api/dispositivos/delete/${deviceToDelete.id}/`, {
                        method: 'DELETE',
                        headers: { 'Authorization': `Bearer ${token}` },
                    });
                    if (response.ok) {
                        alert('Dispositivo eliminado correctamente');
                        cargarDispositivos();
                        setShowDeleteModal(false);
                        setDeviceToDelete(null);
                    } else {
                        throw new Error('Error al eliminar el dispositivo');
                    }
                } catch (error) {
                    setErrorMessage('Error al eliminar el dispositivo');
                }
            }
        } else {
            alert('Por favor, selecciona un dispositivo para eliminar.');
        }
<<<<<<< HEAD
=======
=======
        const response = await fetch(`/api/dispositivos/${dispositivoSeleccionado}/`, {
            method: 'PUT',
            headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nombre: nombreDispositivo })
        });
        if (response.ok) {
            cargarDispositivos();
            setDispositivoSeleccionado(null);
        } else {
            throw new Error('Error al actualizar el nombre del dispositivo');
        }
        } catch (error) {
        setErrorMessage('Error al actualizar el nombre del dispositivo');
        }
    };

    const handleEliminarDispositivo = async (dispositivoId) => {
        const token = localStorage.getItem('access_token');
        try {
        const response = await fetch(`/api/dispositivos/delete/${dispositivoId}/`, {
            method: 'DELETE',
            headers: { 'Authorization': `Bearer ${token}` },
        });
        if (response.ok) {
            cargarDispositivos();
        } else {
            throw new Error('Error al eliminar el dispositivo');
        }
        } catch (error) {
        setErrorMessage('Error al eliminar el dispositivo');
        }
    };

    const logout = () => {
        localStorage.removeItem('access_token');
        alert("Has cerrado sesión.");
        navigate('/login');
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
    };

    return (
        <div className="main-content">
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            <div className="content-header">
                <div className="header-title">
                    <h2>Mis Dispositivos</h2>
                    <button
                        className="btn btn-danger btn-sm ml-3 eliminar-boton"
                        onClick={handleDeleteClick}
                    >
                        Delete
                    </button>
                </div>
                <UserMenu />
            </div>

            <div className="dispositivos-section">
                <div className="row">
                    {dispositivos.map((dispositivo) => (
                        <div className="col-md-4" key={dispositivo.id}>
                            <div className="card mb-3">
                                <div className="card-body">
                                    <h5 className="card-title">{dispositivo.nombre}</h5>
                                    <p className="card-text">Modelo: {dispositivo.modelo || 'Desconocido'}</p>
                                    <p className="card-text">Estado: {dispositivo.estado ? 'Activo' : 'Inactivo'}</p>
                                    <button
                                        className="btn btn-info mr-2"
                                        onClick={() => handleCambiarNombre(dispositivo.id, dispositivo.nombre)}
                                    >
                                        Cambiar Nombre
                                    </button>
                                    <button
                                        className="btn btn-success"
                                        onClick={() => {
                                            localStorage.setItem('dispositivoSeleccionado', dispositivo.id);
                                            navigate(`/dispositivo/${dispositivo.id}/reg_event`);
                                        }}
                                    >
                                        Historial de Eventos
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Modal para cambiar nombre del dispositivo */}
            {showRenameModal && (
                <div className="modal-overlay" onClick={() => setShowRenameModal(false)}>
                    <div className="modal-content small-modal" onClick={(e) => e.stopPropagation()}>
                        <h5>Cambiar Nombre</h5>
                        <input
                            type="text"
                            value={nombreDispositivo}
                            onChange={(e) => setNombreDispositivo(e.target.value)}
                            placeholder="Nuevo nombre"
                        />
                        <div className="modal-actions">
                            <button className="btn btn-success" onClick={handleActualizarNombre}>Guardar</button>
                            <button className="btn btn-secondary" onClick={() => setShowRenameModal(false)}>Cancelar</button>
                        </div>
                    </div>
                </div>
            )}

            {/* Modal para eliminar dispositivo */}
            {showDeleteModal && (
                <div className="modal-overlay" onClick={() => setShowDeleteModal(false)}>
                    <div className="modal-content small-modal" onClick={(e) => e.stopPropagation()}>
                        <h5>Eliminar Dispositivo</h5>
                        <select
                            className="form-control mb-3"
                            value={deviceToDelete ? deviceToDelete.id : ''}
                            onChange={(e) => setDeviceToDelete(dispositivos.find(d => d.id === parseInt(e.target.value)))}
                        >
                            <option value="">Selecciona un dispositivo</option>
                            {dispositivos.map((device) => (
                                <option key={device.id} value={device.id}>{device.nombre}</option>
                            ))}
                        </select>
                        <div className="modal-actions">
                            <button className="btn btn-danger" onClick={handleConfirmDelete}>Eliminar</button>
                            <button className="btn btn-secondary" onClick={() => setShowDeleteModal(false)}>Cancelar</button>
                        </div>
                    </div>
                </div>
            )}

            {errorMessage && <p className="text-danger">{errorMessage}</p>}
        </div>
    );
};

<<<<<<< HEAD
export default MisDispositivos;
=======
export default MisDispositivos;
=======
        <div className="content-header">
            <div className="header-title">
            <h2>Mis Dispositivos</h2>
            <button className="btn btn-danger btn-sm ml-3" onClick={() => alert('Selecciona un dispositivo para eliminar')}>Delete</button>
            </div>
            <div className="user-info">
            <img src={UserIcon} alt="User Icon" onClick={() => document.getElementById("user-dropdown").classList.toggle("show")} />
            <div className="user-dropdown" id="user-dropdown">
                <Link to="/cuenta">Mi Cuenta</Link>
                <Link to="/login" onClick={logout}>Cerrar Sesión</Link>
            </div>
            </div>
        </div>

        <div className="dispositivos-section">
            <div className="row">
            {dispositivos.map((dispositivo) => (
                <div className="col-md-4" key={dispositivo.id}>
                <div className="card mb-3">
                    <div className="card-body">
                    <h5 className="card-title">{dispositivo.nombre}</h5>
                    <p className="card-text">ID: {dispositivo.id}</p>
                    <button className="btn btn-info" onClick={() => handleCambiarNombre(dispositivo.id)}>
                        Cambiar Nombre
                    </button>
                    <button className="btn btn-danger" onClick={() => handleEliminarDispositivo(dispositivo.id)}>
                        Eliminar
                    </button>
                    </div>
                </div>
                </div>
            ))}
            </div>
        </div>

        {dispositivoSeleccionado && (
            <div className="modal">
            <h5>Cambiar Nombre del Dispositivo</h5>
            <input
                type="text"
                value={nombreDispositivo}
                onChange={(e) => setNombreDispositivo(e.target.value)}
            />
            <button onClick={handleActualizarNombre}>Guardar</button>
            <button onClick={() => setDispositivoSeleccionado(null)}>Cancelar</button>
            </div>
        )}

        {errorMessage && <p className="text-danger">{errorMessage}</p>}
        </div>
    );
    };

export default MisDispositivos;
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
