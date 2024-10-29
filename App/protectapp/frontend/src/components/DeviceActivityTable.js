// src/components/DeviceActivityTable.js
import React, { useEffect, useState } from 'react';

const BASE_URL = "http://127.0.0.1:8000"; // Definimos la constante BASE_URL

const DeviceActivityTable = () => {
    const [devices, setDevices] = useState([]);

    useEffect(() => {
        cargarActividadDispositivos();
    }, []);

    const cargarActividadDispositivos = async () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
            alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
            window.location.href = "/login";
            return;
        }

        try {
            const response = await fetch(`${BASE_URL}/api/dispositivos/`, { // Usamos BASE_URL aquí
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                const dispositivos = await response.json();
                setDevices(dispositivos);
            } else if (response.status === 401) {
                alert('Tu sesión ha expirado o no es válida. Por favor, inicia sesión de nuevo.');
                window.location.href = "/login";
            } else {
                alert('Error al obtener los datos de los dispositivos.');
            }
        } catch (error) {
            console.error('Error en la solicitud de dispositivos:', error);
            alert('Error en la solicitud. Inténtalo de nuevo.');
        }
    };

    return (
        <div className="table-responsive">
            <h4>Actividad Reciente de los Dispositivos</h4>
            <table className="table">
                <thead>
                    <tr>
                        <th>Dispositivo</th>
                        <th>Última Actividad</th>
                        <th>Ubicación</th>
                        <th>Estado</th>
                    </tr>
                </thead>
                <tbody>
                    {devices.length > 0 ? (
                        devices.map((device, index) => (
                            <tr key={index}>
                                <td>{device.nombre}</td>
                                <td>{device.ultima_actividad}</td>
                                <td>{device.ubicacion}</td>
                                <td>
                                    <span className={`badge ${getBadgeClass(device.estado)}`}>
                                        {device.estado}
                                    </span>
                                </td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="4" className="text-center">No hay actividad reciente para mostrar.</td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
};

// Función para obtener la clase CSS correspondiente al estado del dispositivo
const getBadgeClass = (estado) => {
    if (estado === 'Activo') return 'badge-success';
    if (estado === 'En Espera') return 'badge-warning';
    return 'badge-danger';
};

export default DeviceActivityTable;