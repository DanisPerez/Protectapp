// src/components/Header.js
import React from 'react';
import { useLocation } from 'react-router-dom';
import ProtectLogoInicio from '../assets/img/Protect2.png'; 
import ProtectLogo from '../assets/img/Protect1.png';       

const Header = () => {
    const location = useLocation();

    return (
        <header>
            <nav className="navbar navbar-light">
                {location.pathname === '/inicio' ? (
                    // Mostrar Protect2.png solo en la página de inicio
                    <a className="navbar-brand" href="/inicio">
                        <img src={ProtectLogoInicio} alt="Logo Protect Inicio" className="img-fluid" />
                    </a>
                ) : (
                    // Mostrar Protect1.png en todas las demás páginas
                    <a className="navbar-brand" href="/login">
                        <img src={ProtectLogo} alt="Logo Protect" className="img-fluid" />
                    </a>
                )}
            </nav>
        </header>
    );
};

export default Header;
