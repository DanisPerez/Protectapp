// src/components/ExportarDatos.js
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/ExportarDatos.css';
import SidebarEventos from './SidebarEventos';
import UserIcon from '../assets/img/cuenta.png';

const ExportarDatos = () => {
    const navigate = useNavigate();
    const [tipoDatos, setTipoDatos] = useState('llamadas');
    const [formato, setFormato] = useState('pdf');
    const [progreso, setProgreso] = useState(0);
    const [downloadUrl, setDownloadUrl] = useState(null);

    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const token = localStorage.getItem('access_token');

    useEffect(() => {
        if (!token || !dispositivoId) {
        alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
        navigate('/login');
        }
    }, [token, dispositivoId, navigate]);

    const iniciarExportacion = async () => {
        setProgreso(0);
        try {
        const response = await fetch(`/api/dispositivos/${dispositivoId}/exportar/${formato}/?tipo=${tipoDatos}`, {
            method: 'GET',
            headers: { Authorization: `Bearer ${token}` },
        });
        
        if (!response.ok) throw new Error('Error en la exportación');
        
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        setDownloadUrl(url);
        alert('Exportación completada con éxito');
        } catch (error) {
        console.error('Error al exportar:', error);
        alert('Error al exportar los datos o de conexión.');
        }
    };

    const handleExportClick = () => {
        setProgreso(0);
        iniciarProgreso();
        iniciarExportacion();
    };

    const iniciarProgreso = () => {
        setProgreso(0);
        let valorProgreso = 0;
        const interval = setInterval(() => {
        valorProgreso += 10;
        setProgreso(valorProgreso);
        if (valorProgreso >= 100) clearInterval(interval);
        }, 300);
    };

    const toggleUserDropdown = () => {
        const dropdown = document.getElementById('user-dropdown');
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    };

    const logout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        navigate('/login');
    };

    return (
        <div className="main-layout">
        <SidebarEventos />
        <div className="main-content">
            <div className="content-header">
            <h2>Exportar Datos</h2>
            <div className="user-info">
                <img src={UserIcon} alt="User Icon" onClick={toggleUserDropdown} />
                <div className="user-dropdown" id="user-dropdown">
                <a href="/cuenta">Mi Cuenta</a>
                <button onClick={logout}>Cerrar Sesión</button>
                </div>
            </div>
            </div>

            <div className="form-group">
            <label>Seleccione el tipo de datos a exportar:</label>
            <select className="form-control" value={tipoDatos} onChange={(e) => setTipoDatos(e.target.value)}>
                <option value="llamadas">Llamadas</option>
                <option value="mensajes">Mensajes</option>
                <option value="contactos">Contactos</option>
                <option value="fotos">Fotos</option>
                <option value="videos">Videos</option>
                <option value="ubicaciones">Ubicaciones</option>
            </select>
            </div>

            <div className="form-group">
            <label>Seleccione el formato de exportación:</label>
            <select className="form-control" value={formato} onChange={(e) => setFormato(e.target.value)}>
                <option value="pdf">PDF</option>
                <option value="csv">CSV</option>
                <option value="xlsx">Excel</option>
            </select>
            </div>

            <button className="btn btn-primary" onClick={handleExportClick}>
            Exportar Datos
            </button>

            <div className="progress mt-3">
            <div className="progress-bar" style={{ width: `${progreso}%` }}>
                {progreso}%
            </div>
            </div>

            {downloadUrl && (
            <a href={downloadUrl} className="btn btn-success mt-3" download={`${tipoDatos}_exportado.${formato}`}>
                Descargar Archivo
            </a>
            )}
        </div>
        </div>
    );
};

export default ExportarDatos;
