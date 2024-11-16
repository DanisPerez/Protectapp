<<<<<<< HEAD
import React, { useEffect, useState } from 'react';
import SidebarEventos from './SidebarEventos';
import UserMenu from './UserMenu';
=======
<<<<<<< HEAD
import React, { useEffect, useState } from 'react';
import SidebarEventos from './SidebarEventos';
import UserMenu from './UserMenu';
=======
// src/components/ArchivoDeTelefono.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import SidebarEventos from './SidebarEventos';
<<<<<<< HEAD
import UserMenu from './UserMenu'; // Importa UserMenu
=======
import UserIcon from '../assets/img/cuenta.png'; 
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
import '../css/PhoneArchive.css';

const ArchivoDeTelefono = () => {
    const [activeTab, setActiveTab] = useState('llamadas');
    const [data, setData] = useState({ llamadas: [], mensajes: [], contactos: [], fotos: [], videos: [] });
    const [loadingMessage, setLoadingMessage] = useState('');
<<<<<<< HEAD
    const [searchTerm, setSearchTerm] = useState('');
    const [isAscending, setIsAscending] = useState(true);

=======
<<<<<<< HEAD
    const [searchTerm, setSearchTerm] = useState('');
    const [isAscending, setIsAscending] = useState(true); // Para controlar el orden de las fechas

=======

<<<<<<< HEAD
=======
    // Verificación y configuración del dispositivo seleccionado
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    if (!dispositivoId) {
        alert('No se ha seleccionado un dispositivo.');
        window.location.href = '/mis_dispositivos';
    }

<<<<<<< HEAD
    const endpoints = {
        llamadas: 'llamadas',
        mensajes: 'mensajes',
        contactos: 'contactos',
        fotos: 'fotos',
        videos: 'videos',
    };

=======
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
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
<<<<<<< HEAD
            if (!response.ok) throw new Error(`Error fetching ${endpoint}`);
            return await response.json();
        } catch (error) {
            console.error(`Error fetching ${endpoint}:`, error);
            setLoadingMessage(`Error al cargar ${endpoint}`);
            return [];
=======
            if (!response.ok) throw new Error('Network response was not ok');
            return await response.json();
        } catch (error) {
            console.error(`Error fetching ${endpoint}:`, error);
            setLoadingMessage('Error al obtener los datos');
            throw error;
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
        }
    };

    const loadTabData = async (tab) => {
        setLoadingMessage(`Cargando ${tab}...`);
        try {
<<<<<<< HEAD
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

=======
            const tabData = await fetchData(tab);
            setData((prevData) => ({ ...prevData, [tab]: tabData }));
            setLoadingMessage('');
        } catch {
            setLoadingMessage('Error al cargar los datos');
        }
    };

>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    useEffect(() => {
        loadTabData(activeTab);
    }, [activeTab]);

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
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

<<<<<<< HEAD
=======
=======
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
    return (
        <div className="main-layout">
            <SidebarEventos />
            <div className="main-content">
                <div className="content-header">
                    <h2>Archivo de Teléfono</h2>
<<<<<<< HEAD
                    <UserMenu />
                </div>

                <ul className="nav nav-tabs">
                    {Object.keys(endpoints).map((tab) => (
=======
<<<<<<< HEAD
                    <UserMenu />
                </div>

=======
<<<<<<< HEAD
                    <UserMenu /> {/* Reemplazamos el menú manual por UserMenu */}
=======
                    <div className="user-info">
                        <img src={UserIcon} alt="User Icon" id="user-icon" onClick={() => {
                            const dropdown = document.getElementById("user-dropdown");
                            dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
                        }} />
                        <div className="user-dropdown" id="user-dropdown">
                            <Link to="/cuenta">Mi Cuenta</Link>
                            <Link to="/login" onClick={() => {
                                localStorage.removeItem('access_token');
                                window.location.href = "/login";
                            }}>Cerrar Sesión</Link>
                        </div>
                    </div>
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
                </div>

                {/* Navegación entre pestañas */}
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                <ul className="nav nav-tabs">
                    {['llamadas', 'mensajes', 'contactos', 'fotos', 'videos'].map((tab) => (
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
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

<<<<<<< HEAD
                <div className="tab-content">
                    <div className="update-button-container">
                        <button onClick={handleUpdate} className="btn btn-primary">Actualizar</button>
                    </div>

                    {loadingMessage && <p className="loading-message">{loadingMessage}</p>}
                    <div className="tab-pane fade show active" style={{ maxHeight: '500px', overflowY: 'auto' }}>
=======
<<<<<<< HEAD
                <div className="tab-content">
                    {loadingMessage && <p className="loading-message">{loadingMessage}</p>}
                    <div className="tab-pane fade show active">
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                        {(activeTab === 'llamadas' || activeTab === 'mensajes') && (
                            <div className="filters-container">
                                <input
                                    type="text"
<<<<<<< HEAD
                                    placeholder={`Buscar número de ${activeTab}`}
=======
                                    placeholder={`Buscar numero de ${activeTab}`}
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                                    value={searchTerm}
                                    onChange={handleSearch}
                                    className="search-input"
                                />
                                <button onClick={toggleSortOrder} className="sort-button">
                                    Ordenar por Fecha ({isAscending ? 'Ascendente' : 'Descendente'})
                                </button>
                                <table className="table">
                                    <thead>
<<<<<<< HEAD
                                        <tr>
                                            <th>#</th>
                                            <th>Número</th>
                                            <th>{activeTab === 'llamadas' ? 'Duración' : 'Contenido'}</th>
                                            <th>Fecha</th>
                                            <th>Hora</th>
                                            <th>Tipo</th>
                                        </tr>
=======
                                        <tr><th>#</th><th>Número</th><th>Contenido</th><th>Fecha</th><th>Hora</th><th>Tipo</th></tr>
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                                    </thead>
                                    <tbody>
                                        {filteredData.map((item, index) => (
                                            <tr key={index}>
                                                <td>{index + 1}</td>
                                                <td>{item.numero}</td>
<<<<<<< HEAD
                                                <td>{activeTab === 'llamadas' ? `${item.duracion} seg` : item.contenido}</td>
=======
                                                <td>{activeTab === 'llamadas' ? item.duracion + ' seg' : item.contenido}</td>
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                                                <td>{item.fecha}</td>
                                                <td>{item.hora}</td>
                                                <td>{item.tipo}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
<<<<<<< HEAD
                        )}

                        {activeTab === 'contactos' && (
                            <ul className="list-group" style={{ maxHeight: '500px', overflowY: 'auto' }}>
=======
=======
                {/* Contenido de las pestañas */}
                <div className="tab-content">
                    {loadingMessage && <p className="loading-message">{loadingMessage}</p>}
                    <div className="tab-pane fade show active">
                        {activeTab === 'llamadas' && (
                            <table className="table">
                                <thead>
                                    <tr><th>#</th><th>Número</th><th>Duración</th><th>Fecha</th><th>Hora</th><th>Tipo</th></tr>
                                </thead>
                                <tbody>
                                    {data.llamadas.map((llamada, index) => (
                                        <tr key={index}>
                                            <td>{index + 1}</td>
                                            <td>{llamada.numero}</td>
                                            <td>{llamada.duracion} seg</td>
                                            <td>{llamada.fecha}</td>
                                            <td>{llamada.hora}</td>
                                            <td>{llamada.tipo}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        )}

                        {activeTab === 'mensajes' && (
                            <table className="table">
                                <thead>
                                    <tr><th>#</th><th>Número</th><th>Contenido</th><th>Fecha</th><th>Hora</th><th>Tipo</th></tr>
                                </thead>
                                <tbody>
                                    {data.mensajes.map((mensaje, index) => (
                                        <tr key={index}>
                                            <td>{index + 1}</td>
                                            <td>{mensaje.numero}</td>
                                            <td>{mensaje.contenido}</td>
                                            <td>{mensaje.fecha}</td>
                                            <td>{mensaje.hora}</td>
                                            <td>{mensaje.tipo}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                        )}

                        {activeTab === 'contactos' && (
                            <ul className="list-group">
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                                {data.contactos.map((contacto, index) => (
                                    <li className="list-group-item" key={index}>
                                        {contacto.nombre} - {contacto.numero}
                                    </li>
                                ))}
                            </ul>
                        )}

                        {activeTab === 'fotos' && (
<<<<<<< HEAD
                            <div className="media-container" style={{ maxHeight: '500px', overflowY: 'auto' }}>
                                {data.fotos.map((foto, index) => (
                                    <img
                                        src={`http://localhost:8000${foto.archivo_foto}`}
                                        alt={`Foto ${index + 1}`}
                                        key={index}
                                        className="media-item"
                                    />
=======
                            <div className="media-container">
                                {data.fotos.map((foto, index) => (
                                    <img src={foto.ruta_foto} alt={`Foto ${index + 1}`} key={index} />
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                                ))}
                            </div>
                        )}

                        {activeTab === 'videos' && (
<<<<<<< HEAD
                            <div className="media-container" style={{ maxHeight: '500px', overflowY: 'auto' }}>
                                {data.videos.map((video, index) => (
                                    <video
                                        src={`http://localhost:8000${video.ruta_video}`}
                                        controls
                                        key={index}
                                        className="media-item"
                                    ></video>
=======
                            <div className="media-container">
                                {data.videos.map((video, index) => (
                                    <video src={video.ruta_video} controls key={index}></video>
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                                ))}
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

<<<<<<< HEAD
export default ArchivoDeTelefono;
=======
<<<<<<< HEAD
export default ArchivoDeTelefono;
=======
<<<<<<< HEAD
export default ArchivoDeTelefono;
=======
export default ArchivoDeTelefono;
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
