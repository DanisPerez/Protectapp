import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import UserMenu from './UserMenu';
import '../css/RegistroEventos.css';

const RegistroEventos = () => {
    const [eventos, setEventos] = useState([]);
    const [selectedEvent, setSelectedEvent] = useState(null);
    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        verificarLogin();
        obtenerEventos();
    }, []);

    const verificarLogin = () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
            alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
            window.location.href = '/login';
        }
    };

    const obtenerEventos = async () => {
        const token = localStorage.getItem('access_token');
        const dispositivoId = localStorage.getItem('dispositivoSeleccionado');

        if (!dispositivoId) {
            alert('No se ha seleccionado un dispositivo.');
            window.location.href = '/mis_dispositivos';
            return;
        }

        try {
            const response = await fetch(`http://localhost:8000/api/dispositivos/${dispositivoId}/eventos/`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });

            if (response.ok) {
                const data = await response.json();
                setEventos(data);
            } else {
                throw new Error('Error al cargar los eventos');
            }
        } catch (error) {
            setErrorMessage('Error al cargar los eventos');
            console.error(error);
        }
    };

    const verDetalles = async (eventoId) => {
        const token = localStorage.getItem('access_token');
        try {
            const response = await fetch(`http://localhost:8000/api/eventos/${eventoId}/`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });

            if (response.ok) {
                const data = await response.json();
                setSelectedEvent(data);
            } else {
                throw new Error('Error al cargar los detalles del evento');
            }
        } catch (error) {
            setErrorMessage('Error al cargar los detalles del evento');
            console.error(error);
        }
    };

    const closeModal = () => {
        setSelectedEvent(null);
    };

    return (
        <div className="main-content registro-eventos">
            <div className="content-header">
                <h2>Registro de Eventos</h2>
                <UserMenu />
            </div>

            <div className="table-section">
                <h4>Historial de Eventos</h4>
                {errorMessage && <p className="error-message">{errorMessage}</p>}
                <table className="table table-striped table-sm">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Tipo de Evento</th>
                            <th>Fecha</th>
                            <th>Hora</th>
                            <th>Detalles</th>
                        </tr>
                    </thead>
                    <tbody>
                        {eventos.map(evento => (
                            <tr key={evento.id}>
                                <td>{evento.id}</td>
                                <td>{evento.tipo_evento}</td>
                                <td>{evento.fecha}</td>
                                <td>{evento.hora}</td>
                                <td>
                                    <button className="btn btn-info" onClick={() => verDetalles(evento.id)}>Ver Detalles</button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {selectedEvent && (
                <div className="modal-overlay" onClick={closeModal}>
                    <div className="modal-content small-modal" onClick={(e) => e.stopPropagation()}>
                        <span className="close" onClick={closeModal}>&times;</span>
                        <h5>Detalles del Evento</h5>
                        <p><strong>Tipo de Evento:</strong> {selectedEvent.tipo_evento}</p>
                        <p><strong>Fecha:</strong> {selectedEvent.fecha}</p>
                        <p><strong>Hora:</strong> {selectedEvent.hora}</p>
                        <p><strong>Detalles:</strong> {selectedEvent.detalles}</p>
                    </div>
                </div>
            )}
        </div>
    );
};

export default RegistroEventos;