// src/components/ContentHeader.js
import React from 'react';
import UserMenu from './UserMenu'; 

const ContentHeader = () => {
    return (
        <div className="content-header">
            <h2>Bienvenido de nuevo</h2>
            <UserMenu /> 
        </div>
    );
};

export default ContentHeader;
