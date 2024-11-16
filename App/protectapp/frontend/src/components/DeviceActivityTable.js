// src/components/DeviceActivityTable.js
import React, { useEffect, useState } from 'react';

<<<<<<< HEAD
const BASE_URL = "http://127.0.0.1:8000";

=======
<<<<<<< HEAD
const BASE_URL = "http://127.0.0.1:8000";

=======
<<<<<<< HEAD
const BASE_URL = "http://127.0.0.1:8000"; // Definimos la constante BASE_URL

=======
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
const DeviceActivityTable = () => {
    const [devices, setDevices] = useState([]);

    useEffect(() => {
        cargarActividadDispositivos();
    }, []);

    const cargarActividadDispositivos = async () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
            window.location.href = "/login";
            return;
        }

        try {
<<<<<<< HEAD
            const response = await fetch(`${BASE_URL}/api/dispositivos/`, {
=======
<<<<<<< HEAD
            const response = await fetch(`${BASE_URL}/api/dispositivos/`, {
=======
            const response = await fetch(`${BASE_URL}/api/dispositivos/`, { // Usamos BASE_URL aquí
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
        alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
        window.location.href = "/login";
        return;
        }

        try {
        const response = await fetch('/api/dispositivos/', {
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
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
        }
    };

    return (
        <div className="table-responsive">
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
            <h4>Actividad Reciente de los Dispositivos</h4>
            <table className="table">
                <thead>
                    <tr>
                        <th>Dispositivo</th>
<<<<<<< HEAD
                        <th>Estado</th>
                        <th>Eventos</th>
                        <th>Última Actividad</th> {/* Nueva columna para la última actividad */}
=======
<<<<<<< HEAD
                        <th>Estado</th>
                        <th>Eventos</th>
                        <th>Última Actividad</th> {/* Nueva columna para la última actividad */}
=======
                        <th>Última Actividad</th>
                        <th>Ubicación</th>
                        <th>Estado</th>
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                    </tr>
                </thead>
                <tbody>
                    {devices.length > 0 ? (
                        devices.map((device, index) => (
                            <tr key={index}>
                                <td>{device.nombre}</td>
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                                <td>
                                    <span className={`badge ${getBadgeClass(device.estado_texto)}`}>
                                        {device.estado_texto}
                                    </span>
                                </td>
                                <td>{device.eventos}</td>
                                <td>{device.ultima_actividad}</td> {/* Muestra la última actividad */}
<<<<<<< HEAD
=======
=======
                                <td>{device.ultima_actividad}</td>
                                <td>{device.ubicacion}</td>
                                <td>
                                    <span className={`badge ${getBadgeClass(device.estado)}`}>
                                        {device.estado}
                                    </span>
                                </td>
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="4" className="text-center">No hay actividad reciente para mostrar.</td>
                        </tr>
                    )}
                </tbody>
            </table>
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
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
            {devices.map((device, index) => (
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
            ))}
            </tbody>
        </table>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
        </div>
    );
};

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
const getBadgeClass = (estado) => {
    if (estado === 'Activo') return 'badge-success';
    if (estado === 'Inactivo') return 'badge-danger';
    return 'badge-warning';
};

export default DeviceActivityTable;
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
// Función para obtener la clase CSS correspondiente al estado del dispositivo
=======
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
const getBadgeClass = (estado) => {
    if (estado === 'Activo') return 'badge-success';
    if (estado === 'En Espera') return 'badge-warning';
    return 'badge-danger';
};

<<<<<<< HEAD
export default DeviceActivityTable;
=======
export default DeviceActivityTable;
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
