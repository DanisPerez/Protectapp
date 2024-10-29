// src/components/SummarySection.js
import React from 'react';

const SummarySection = () => {
    return (
        <div className="summary-section">
        <div className="summary-card">
            <h4>Dispositivos Activos</h4>
            <p><i className="fas fa-mobile-alt"></i> 3 Dispositivos</p>
        </div>
        <div className="summary-card">
            <h4>Alertas Recientes</h4>
            <p><i className="fas fa-exclamation-circle"></i> 2 Alertas</p>
        </div>
        <div className="summary-card">
            <h4>Última Actividad</h4>
            <p><i className="fas fa-clock"></i> Hace 2 horas</p>
        </div>
        </div>
    );
};

export default SummarySection;
