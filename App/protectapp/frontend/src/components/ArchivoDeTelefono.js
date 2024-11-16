import React, { useEffect, useState } from 'react';
import SidebarEventos from './SidebarEventos';
import UserMenu from './UserMenu';
import '../css/PhoneArchive.css';

const ArchivoDeTelefono = () => {
    const [activeTab, setActiveTab] = useState('llamadas');
    const [data, setData] = useState({ llamadas: [], mensajes: [], contactos: [], fotos: [], videos: [] });
    const [loadingMessage, setLoadingMessage] = useState('');
    const [searchTerm, setSearchTerm] = useState('');
    const [isAscending, setIsAscending] = useState(true);

    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    if (!dispositivoId) {
        alert('No se ha seleccionado un dispositivo.');
        window.location.href = '/mis_dispositivos';
    }

    const endpoints = {
        llamadas: 'llamadas',
        mensajes: 'mensajes',
        contactos: 'contactos',
        fotos: 'fotos',
        videos: 'videos',
    };

    const fetchData = async (endpoint) => {
        const token = localStorage.getItem('access_token');
        try {
            const response = await fetch(`http://localhost:8000/api/dispositivos/${dispositivoId}/${endpoint}/`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) throw new Error(`Error fetching ${endpoint}`);
            return await response.json();
        } catch (error) {
            console.error(`Error fetching ${endpoint}:`, error);
            setLoadingMessage(`Error al cargar ${endpoint}`);
            return [];
        }
    };

    const loadTabData = async (tab) => {
        setLoadingMessage(`Cargando ${tab}...`);
        try {
            const tabData = await fetchData(endpoints[tab]);
            setData((prevData) => ({ ...prevData, [tab]: tabData }));
            setLoadingMessage('');
        } catch {
            setLoadingMessage(`Error al cargar ${tab}`);
        }
    };

    const handleUpdate = () => {
        loadTabData(activeTab); // Actualiza la pestaña activa cuando el usuario hace clic en "Actualizar"
    };

    useEffect(() => {
        loadTabData(activeTab);
    }, [activeTab]);

    const handleSearch = (event) => {
        setSearchTerm(event.target.value);
    };

    const toggleSortOrder = () => {
        setIsAscending(!isAscending);
    };

    const filteredData = data[activeTab]
        .filter((item) => {
            if (activeTab === 'llamadas' || activeTab === 'mensajes') {
                return item.numero.includes(searchTerm);
            }
            return true;
        })
        .sort((a, b) => {
            const dateA = new Date(a.fecha + ' ' + a.hora);
            const dateB = new Date(b.fecha + ' ' + b.hora);
            return isAscending ? dateA - dateB : dateB - dateA;
        });

    return (
        <div className="main-layout">
            <SidebarEventos />
            <div className="main-content">
                <div className="content-header">
                    <h2>Archivo de Teléfono</h2>
                    <UserMenu />
                </div>

                <ul className="nav nav-tabs">
                    {Object.keys(endpoints).map((tab) => (
                        <li className="nav-item" key={tab}>
                            <button
                                className={`nav-link ${activeTab === tab ? 'active' : ''}`}
                                onClick={() => setActiveTab(tab)}
                            >
                                {tab.charAt(0).toUpperCase() + tab.slice(1)}
                            </button>
                        </li>
                    ))}
                </ul>

                <div className="tab-content">
                    <div className="update-button-container">
                        <button onClick={handleUpdate} className="btn btn-primary">Actualizar</button>
                    </div>

                    {loadingMessage && <p className="loading-message">{loadingMessage}</p>}
                    <div className="tab-pane fade show active" style={{ maxHeight: '500px', overflowY: 'auto' }}>
                        {(activeTab === 'llamadas' || activeTab === 'mensajes') && (
                            <div className="filters-container">
                                <input
                                    type="text"
                                    placeholder={`Buscar número de ${activeTab}`}
                                    value={searchTerm}
                                    onChange={handleSearch}
                                    className="search-input"
                                />
                                <button onClick={toggleSortOrder} className="sort-button">
                                    Ordenar por Fecha ({isAscending ? 'Ascendente' : 'Descendente'})
                                </button>
                                <table className="table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Número</th>
                                            <th>{activeTab === 'llamadas' ? 'Duración' : 'Contenido'}</th>
                                            <th>Fecha</th>
                                            <th>Hora</th>
                                            <th>Tipo</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {filteredData.map((item, index) => (
                                            <tr key={index}>
                                                <td>{index + 1}</td>
                                                <td>{item.numero}</td>
                                                <td>{activeTab === 'llamadas' ? `${item.duracion} seg` : item.contenido}</td>
                                                <td>{item.fecha}</td>
                                                <td>{item.hora}</td>
                                                <td>{item.tipo}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
                        )}

                        {activeTab === 'contactos' && (
                            <ul className="list-group" style={{ maxHeight: '500px', overflowY: 'auto' }}>
                                {data.contactos.map((contacto, index) => (
                                    <li className="list-group-item" key={index}>
                                        {contacto.nombre} - {contacto.numero}
                                    </li>
                                ))}
                            </ul>
                        )}

                        {activeTab === 'fotos' && (
                            <div className="media-container" style={{ maxHeight: '500px', overflowY: 'auto' }}>
                                {data.fotos.map((foto, index) => (
                                    <img
                                        src={`http://localhost:8000${foto.archivo_foto}`}
                                        alt={`Foto ${index + 1}`}
                                        key={index}
                                        className="media-item"
                                    />
                                ))}
                            </div>
                        )}

                        {activeTab === 'videos' && (
                            <div className="media-container" style={{ maxHeight: '500px', overflowY: 'auto' }}>
                                {data.videos.map((video, index) => (
                                    <video
                                        src={`http://localhost:8000${video.ruta_video}`}
                                        controls
                                        key={index}
                                        className="media-item"
                                    ></video>
                                ))}
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ArchivoDeTelefono;
