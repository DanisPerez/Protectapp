// src/components/ContentHeader.js
import React from 'react';
import UserMenu from './UserMenu'; // Importa el nuevo componente UserMenu

const ContentHeader = () => {
    return (
        <div className="content-header">
            <h2>Bienvenido de nuevo</h2>
            <UserMenu /> {/* Reemplaza la lógica del dropdown con el componente UserMenu */}
        </div>
    );
};

export default ContentHeader;
