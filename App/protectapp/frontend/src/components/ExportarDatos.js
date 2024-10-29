// src/components/ExportarDatos.js
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/ExportarDatos.css';
import SidebarEventos from './SidebarEventos';
import UserMenu from './UserMenu'; // Importamos el nuevo componente UserMenu

const BASE_URL = "http://127.0.0.1:8000";

const ExportarDatos = () => {
    const navigate = useNavigate();
    const [tipoDatos, setTipoDatos] = useState('llamadas');
    const [formato, setFormato] = useState('pdf');
    const [progreso, setProgreso] = useState(0);
    const [downloadUrl, setDownloadUrl] = useState(null);
    const [isExporting, setIsExporting] = useState(false); 

    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const token = localStorage.getItem('access_token');

    useEffect(() => {
        if (!token || !dispositivoId) {
            alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
            navigate('/login');
        }
    }, [token, dispositivoId, navigate]);

    const iniciarExportacion = async () => {
        setIsExporting(true);
        setDownloadUrl(null);
        setProgreso(0);

        try {
            iniciarProgreso();

            const response = await fetch(`${BASE_URL}/api/dispositivos/${dispositivoId}/exportar/${formato}/?tipo=${tipoDatos}`, {
                method: 'GET',
                headers: { Authorization: `Bearer ${token}` },
            });

            if (!response.ok) throw new Error('Error en la exportación');

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            setDownloadUrl(url);
            alert('Exportación completada con éxito');

            setProgreso(100);
        } catch (error) {
            console.error('Error al exportar:', error);
            alert('Error al exportar los datos o de conexión.');
        } finally {
            setIsExporting(false);
        }
    };

    const iniciarProgreso = () => {
        let valorProgreso = 0;
        const interval = setInterval(() => {
            valorProgreso += 10;
            setProgreso(valorProgreso);
            if (valorProgreso >= 100) clearInterval(interval);
        }, 300);
    };

    const handleExportClick = () => {
        setProgreso(0);
        iniciarExportacion();
    };

    return (
        <div className="main-layout">
            <SidebarEventos />
            <div className="main-content">
                <div className="content-header">
                    <h2>Exportar Datos</h2>
                    {/* Integración de UserMenu */}
                    <UserMenu />
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

                <button className="btn btn-primary" onClick={handleExportClick} disabled={isExporting}>
                    {isExporting ? 'Exportando...' : 'Exportar Datos'}
                </button>

                <div className="progress mt-3">
                    <div className="progress-bar" style={{ width: `${progreso}%` }}>
                        {progreso}%
                    </div>
                </div>

                {downloadUrl && (
                    <a
                        href={downloadUrl}
                        className="btn btn-success mt-3"
                        download={`${tipoDatos}_exportado.${formato}`}
                        onClick={() => {
                            setTimeout(() => window.URL.revokeObjectURL(downloadUrl), 100);
                        }}
                    >
                        Descargar Archivo
                    </a>
                )}
            </div>
        </div>
    );
};

export default ExportarDatos;
