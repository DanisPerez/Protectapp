// src/components/MisDispositivos.js
import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import UserIcon from '../assets/img/cuenta.png';
import '../css/MisDispositivos.css';

const MisDispositivos = () => {
    const [dispositivos, setDispositivos] = useState([]);
    const [errorMessage, setErrorMessage] = useState('');
    const [nombreDispositivo, setNombreDispositivo] = useState('');
    const [dispositivoSeleccionado, setDispositivoSeleccionado] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        checkLogin();
        cargarDispositivos();
    }, []);

    const checkLogin = () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
        alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
        navigate('/login');
        }
    };

    const cargarDispositivos = async () => {
        const token = localStorage.getItem('access_token');
        try {
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
    };

    const handleActualizarNombre = async () => {
        const token = localStorage.getItem('access_token');
        try {
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
    };

    return (
        <div className="main-content">
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
