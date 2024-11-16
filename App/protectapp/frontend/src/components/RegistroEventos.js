import React, { useEffect, useState } from 'react';
import UserMenu from './UserMenu';
import '../css/RegistroEventos.css';

const BASE_URL = "http://127.0.0.1:8000"; // Definimos la URL base aquí

const RegistroEventos = () => {
    const [eventos, setEventos] = useState([]);
    const [selectedEvent, setSelectedEvent] = useState(null);
    const [errorMessage, setErrorMessage] = useState('');
    const [loading, setLoading] = useState(true);
    const [filtro, setFiltro] = useState('');
    let ws;

    useEffect(() => {
        verificarLogin();
        cargarDatos();

        // Configurar la conexión WebSocket
        ws = new WebSocket('ws://127.0.0.1:8001/ws/eventos/');
        
        ws.onmessage = (event) => {
            const nuevoEvento = JSON.parse(event.data).evento;
            setEventos((prevEventos) => [nuevoEvento, ...prevEventos]);
        };

        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
            setErrorMessage('Error de conexión en tiempo real.');
        };

        return () => {
            if (ws) ws.close(); // Cierra el WebSocket al desmontar el componente
        };
    }, []);

    const verificarLogin = () => {
        const token = localStorage.getItem('access_token');
        if (!token) {
            alert('No has iniciado sesión. Redirigiendo a la página de inicio de sesión.');
            window.location.href = '/login';
        }
    };

    const cargarDatos = async () => {
        setLoading(true);
        await obtenerEventos();
        setLoading(false);
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
            const response = await fetch(`${BASE_URL}/api/dispositivos/${dispositivoId}/eventos/`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });

            if (response.ok) {
                const data = await response.json();
                setEventos(data);
                setErrorMessage('');
            } else if (response.status === 404) {
                setErrorMessage('No se encontraron eventos para este dispositivo.');
            } else {
                setErrorMessage('Error al cargar los eventos.');
            }
        } catch (error) {
            setErrorMessage('Error al conectar con el servidor.');
            console.error(error);
        }
    };

    const eliminarEvento = async (eventoId) => {
        const token = localStorage.getItem('access_token');
        try {
            const response = await fetch(`${BASE_URL}/api/eventos/${eventoId}/delete/`, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });
    
            if (response.ok) {
                alert('Evento eliminado correctamente.');
                setEventos((prevEventos) => prevEventos.filter(evento => evento.id !== eventoId));
            } else {
                setErrorMessage('Error al eliminar el evento.');
            }
        } catch (error) {
            setErrorMessage('Error al conectar con el servidor.');
            console.error(error);
        }
    };

    const handleDelete = (eventoId) => {
        if (window.confirm("¿Estás seguro de que deseas eliminar este evento?")) {
            eliminarEvento(eventoId);
        }
    };

    const eventosFiltrados = eventos.filter(evento =>
        evento.tipo_evento.toLowerCase().includes(filtro.toLowerCase())
    );

    return (
        <div className="main-content registro-eventos">
            <div className="content-header">
                <h2>Registro de Eventos en Tiempo Real</h2>
                <UserMenu />
            </div>

            <div className="table-section">
                <h4>Historial de Eventos ({eventos.length} total)</h4>
                <input
                    type="text"
                    placeholder="Buscar por tipo de evento"
                    value={filtro}
                    onChange={(e) => setFiltro(e.target.value)}
                    className="search-input"
                />

                {errorMessage && <p className="error-message">{errorMessage}</p>}

                {loading ? (
                    <p>Cargando eventos...</p>
                ) : (
                    <EventsTable eventos={eventosFiltrados} verDetalles={setSelectedEvent} handleDelete={handleDelete} />
                )}
            </div>

            {selectedEvent && (
                <EventDetailModal event={selectedEvent} closeModal={() => setSelectedEvent(null)} />
            )}
        </div>
    );
};

// Tabla de eventos con botón "Delete" al lado de "Ver Detalles"
const EventsTable = ({ eventos, verDetalles, handleDelete }) => (
    <table className="table table-striped table-sm">
        <thead>
            <tr>
                <th>ID</th>
                <th>Tipo de Evento</th>
                <th>Fecha</th>
                <th>Hora</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            {eventos.length > 0 ? (
                eventos.map(evento => (
                    <tr key={evento.id}>
                        <td>{evento.id}</td>
                        <td>{evento.tipo_evento}</td>
                        <td>{evento.fecha}</td>
                        <td>{evento.hora}</td>
                        <td>
                            <button className="btn btn-info btn-sm" onClick={() => verDetalles(evento)}>
                                Ver Detalles
                            </button>
                            <button
                                className="btn btn-danger btn-sm ml-2"
                                onClick={() => handleDelete(evento.id)}
                            >
                                Delete
                            </button>
                        </td>
                    </tr>
                ))
            ) : (
                <tr>
                    <td colSpan="5" className="text-center">No hay eventos para mostrar.</td>
                </tr>
            )}
        </tbody>
    </table>
);

// Modal para detalles del evento
const EventDetailModal = ({ event, closeModal }) => (
    <div className="modal-overlay" onClick={closeModal}>
        <div className="modal-content small-modal" onClick={(e) => e.stopPropagation()}>
            <span className="close" onClick={closeModal}>&times;</span>
            <h5>Detalles del Evento</h5>
            <p><strong>Tipo de Evento:</strong> {event.tipo_evento}</p>
            <p><strong>Fecha:</strong> {event.fecha}</p>
            <p><strong>Hora:</strong> {event.hora}</p>
            <p><strong>Detalles:</strong> {event.detalles}</p>
        </div>
    </div>
);

export default RegistroEventos;
