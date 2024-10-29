// src/components/SidebarEventos.js
import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLaptop, faList, faFolder, faMapMarkerAlt, faMicrophone, faCamera, faFileExport, faShieldAlt } from '@fortawesome/free-solid-svg-icons';
import ProtectLogo from '../assets/img/Protect2.png';
import UserIcon from '../assets/img/cuenta.png';

const SidebarEventos = () => {
    const location = useLocation();

    // Función para alternar el menú de usuario
    const toggleUserMenu = () => {
        const dropdown = document.getElementById('user-dropdown');
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    };

    return (
        <div className="sidebar">
            <div className="logo">
                <img src={ProtectLogo} alt="Logo Protect" />
            </div>
            <Link to="/mis_dispositivos" className={location.pathname === '/mis_dispositivos' ? 'active' : ''}>
                <FontAwesomeIcon icon={faLaptop} /> Mis Dispositivos
            </Link>
            <Link to="/reg_event" className={location.pathname === '/reg_event' ? 'active' : ''}>
                <FontAwesomeIcon icon={faList} /> Registro
            </Link>
            <Link to="/archivo_telefono" className={location.pathname === '/archivo_telefono' ? 'active' : ''}>
                <FontAwesomeIcon icon={faFolder} /> Archivo de Teléfono
            </Link>
            <Link to="/ubicacion" className={location.pathname === '/ubicacion' ? 'active' : ''}>
                <FontAwesomeIcon icon={faMapMarkerAlt} /> Ubicación
            </Link>
            <Link to="/grabacion" className={location.pathname === '/grabacion' ? 'active' : ''}>
                <FontAwesomeIcon icon={faMicrophone} /> Grabación en Tiempo Real
            </Link>
            <Link to="/capturas" className={location.pathname === '/capturas' ? 'active' : ''}>
                <FontAwesomeIcon icon={faCamera} /> Capturas
            </Link>
            <Link to="/exportar_datos" className={location.pathname === '/exportar_datos' ? 'active' : ''}>
                <FontAwesomeIcon icon={faFileExport} /> Exportar Datos
            </Link>
            <Link to="/verificacion_permisos" className={location.pathname === '/verificacion_permisos' ? 'active' : ''}>
                <FontAwesomeIcon icon={faShieldAlt} /> Verificación de Permisos
            </Link>
        </div>
    );
};

export default SidebarEventos;
