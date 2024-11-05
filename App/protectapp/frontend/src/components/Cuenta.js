// src/components/Cuenta.js
import React, { useEffect, useState } from 'react';
import '../css/Account.css';
import UserMenu from './UserMenu'; // Importa el componente UserMenu

const Cuenta = () => {
    const [usuario, setUsuario] = useState({
        nombre: '',
        email: '',
        fechaCreacion: '',
        esActivo: ''
    });
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const [isEditing, setIsEditing] = useState(false); // Nuevo estado para controlar el modo de edición

    useEffect(() => {
        obtenerUsuario();
    }, []);

    const obtenerUsuario = async () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
            alert("No has iniciado sesión. Redirigiendo a la página de inicio de sesión.");
            window.location.href = "/login";
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/user/', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            if (response.ok) {
                const data = await response.json();
                setUsuario({
                    nombre: data.nombre,
                    email: data.email,
                    fechaCreacion: new Date(data.date_joined).toLocaleDateString(),
                    esActivo: data.es_activo ? "Activo" : "Inactivo"
                });
            } else {
                setErrorMessage('Error al cargar los datos del usuario');
            }
        } catch (error) {
            setErrorMessage('Error al conectarse al servidor');
        }
    };

    const actualizarUsuario = async () => {
        const token = localStorage.getItem('access_token');
        if (password && password.length < 8) {
            setErrorMessage('La contraseña debe tener al menos 8 caracteres.');
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/user/', {
                method: 'PUT',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    nombre: usuario.nombre,
                    password: password || undefined
                })
            });
            if (response.ok) {
                alert('Usuario actualizado');
                obtenerUsuario();
                setIsEditing(false); // Vuelve el botón a modo "Editar" después de guardar
            } else {
                setErrorMessage('Error al actualizar el usuario.');
            }
        } catch (error) {
            setErrorMessage('Error al conectarse al servidor.');
        }
    };

    const handleEditClick = () => {
        if (isEditing) {
            actualizarUsuario();
        }
        setIsEditing(!isEditing); // Alterna entre Editar y Guardar
    };

    return (
        <div className="cuenta-page main-content">
            <div className="content-header">
                <h2>Centro de Miembros Protect</h2>
                <UserMenu /> {/* Aquí está el menú de usuario */}
            </div>

            <div className="form-section">
                <h4>Administre su información personal</h4>
                <form onSubmit={(e) => { e.preventDefault(); actualizarUsuario(); }}>
                    <div className="form-group">
                        <label>Nombre Completo:</label>
                        <input
                            type="text"
                            id="nombre"
                            value={usuario.nombre}
                            onChange={(e) => setUsuario({ ...usuario, nombre: e.target.value })}
                            disabled={!isEditing} // Deshabilitado cuando no está en modo edición
                            autoComplete="name"
                        />
                        <button
                            type="button"
                            onClick={handleEditClick}
                        >
                            {isEditing ? "Guardar" : "Editar"}
                        </button>
                    </div>
                    <div className="form-group">
                        <label>Correo Electrónico:</label>
                        <input type="email" value={usuario.email} disabled autoComplete="email" />
                    </div>
                    <div className="form-group">
                        <label>Fecha de Registro:</label>
                        <input type="text" value={usuario.fechaCreacion} disabled />
                    </div>
                    <div className="form-group">
                        <label>Estado Activo:</label>
                        <input type="text" value={usuario.esActivo} disabled autoComplete="username" />
                    </div>
                    <div className="form-group">
                        <label>Contraseña:</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            autoComplete="current-password"
                        />
                        <button type="submit" className="btn btn-primary">Actualizar Contraseña</button>
                    </div>
                    {errorMessage && <div className="text-danger">{errorMessage}</div>}
                </form>
            </div>
        </div>
    );
};

export default Cuenta;
