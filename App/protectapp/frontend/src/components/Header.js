// src/components/Header.js
import React from 'react';
import { useLocation } from 'react-router-dom';
<<<<<<< HEAD
import ProtectLogoInicio from '../assets/img/Protect2.png'; 
import ProtectLogo from '../assets/img/Protect1.png';       
=======
<<<<<<< HEAD
import ProtectLogoInicio from '../assets/img/Protect2.png'; 
import ProtectLogo from '../assets/img/Protect1.png';       
=======
import ProtectLogoInicio from '../assets/img/Protect2.png'; // Logo para la página de inicio
import ProtectLogo from '../assets/img/Protect1.png';       // Logo para las demás páginas
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6

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
<<<<<<< HEAD
                    <a className="navbar-brand" href="/login">
=======
<<<<<<< HEAD
                    <a className="navbar-brand" href="/login">
=======
                    <a className="navbar-brand" href="/">
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
>>>>>>> a1388f7f955b60dcd506918f2bdf9313652780b6
                        <img src={ProtectLogo} alt="Logo Protect" className="img-fluid" />
                    </a>
                )}
            </nav>
        </header>
    );
};

export default Header;
