// src/components/Sidebar.js
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faBox, faUser, faLaptop } from '@fortawesome/free-solid-svg-icons';
import { Link, useLocation } from 'react-router-dom';
import ProtectLogoInicio from '../assets/img/Protect2.png';

const Sidebar = () => {
<<<<<<< HEAD
    const location = useLocation(); 
=======
<<<<<<< HEAD
    const location = useLocation(); 
=======
    const location = useLocation(); // Obtiene la ruta actual
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6

    return (
        <div className="sidebar">
            <div className="logo">
                <img src={ProtectLogoInicio} alt="Logo Protect" />
            </div>
            <Link to="/inicio" className={location.pathname === '/inicio' ? 'active' : ''}>
                <FontAwesomeIcon icon={faHome} /> Inicio
            </Link>
            <Link to="/mi_producto" className={location.pathname === '/mi_producto' ? 'active' : ''}>
                <FontAwesomeIcon icon={faBox} /> Mi Producto
            </Link>
            <Link to="/cuenta" className={location.pathname === '/cuenta' ? 'active' : ''}>
                <FontAwesomeIcon icon={faUser} /> Mi Cuenta
            </Link>
            <Link to="/mis_dispositivos" className={location.pathname === '/mis_dispositivos' ? 'active' : ''}>
                <FontAwesomeIcon icon={faLaptop} /> Mis Dispositivos
            </Link>
        </div>
    );
};

export default Sidebar;
