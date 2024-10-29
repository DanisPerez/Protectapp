// src/components/Footer.js
import React from 'react';

const Footer = () => {
    return (
        <footer>
        <p>&copy; 2024 Protect. Todos los derechos reservados.</p>
        <a href="/politica">
            <i className="fas fa-lock"></i> Política de privacidad
        </a>
        {' | '}
        <a href="/terminos">
            <i className="fas fa-file-contract"></i> Términos y condiciones
        </a>
        </footer>
    );
};

export default Footer;
