import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/Compras.css';

const Compras = () => {
    const [basicDuration, setBasicDuration] = useState(1);
    const [premiumDuration, setPremiumDuration] = useState(1);
    const navigate = useNavigate();

    const updatePrice = (plan) => {
        if (plan === 'basic') {
            return basicDuration === 1 ? 9.99 : basicDuration === 3 ? 27.99 : 99.99;
        } else if (plan === 'premium') {
            return premiumDuration === 1 ? 29.99 : premiumDuration === 3 ? 79.99 : 249.99;
        }
        return 0;
    };

    const redirectToPurchase = (plan) => {
        const duration = plan === 'basic' ? basicDuration : premiumDuration;
        const price = updatePrice(plan);
        alert(`Has seleccionado el ${plan === 'basic' ? 'Plan Básico' : 'Plan Premium'} por ${duration} ${duration === 1 ? 'Mes' : 'Meses'} a $${price}.`);
        navigate(`/compra?plan=${plan}&duration=${duration}`);
    };

    return (
        <main className="product-section container">
            <div className="text-center mb-5">
                <h2>Nuestros Planes</h2>
                <p>Encuentra el plan perfecto para proteger y supervisar a tus seres queridos.</p>
            </div>
            <div className="row">
                <div className="col-md-6">
                    <div className="product-card">
                        <div className="card-body text-center">
                            <h4>Plan Básico</h4>
                            <p>La opción ideal para comenzar a proteger a tus seres queridos.</p>
                            <ul className="list-unstyled">
                                <li>Monitoreo de llamadas y SMS</li>
                                <li>Rastreo de ubicación en tiempo real</li>
                                <li>Acceso al historial de navegación</li>
                            </ul>
                            <label>Selecciona la duración:</label>
                            <select onChange={(e) => setBasicDuration(parseInt(e.target.value))}>
                                <option value="1">1 Mes - $9.99</option>
                                <option value="3">3 Meses - $27.99</option>
                                <option value="12">1 Año - $99.99</option>
                            </select>
                            <div className="price-display">${updatePrice('basic')}</div>
                            <button onClick={() => redirectToPurchase('basic')}>Comprar Plan</button>
                        </div>
                    </div>
                </div>
                <div className="col-md-6">
                    <div className="product-card border border-warning">
                        <div className="card-body text-center">
                            <span className="premium-highlight">Plan más Popular</span>
                            <h4>Plan Premium</h4>
                            <p>La mejor opción para la máxima supervisión y seguridad.</p>
                            <ul className="list-unstyled">
                                <li>Todo lo del Plan Básico</li>
                                <li>Grabación del entorno del dispositivo</li>
                                <li>Alertas y notificaciones en tiempo real</li>
                                <li>Atención al cliente 24/7</li>
                            </ul>
                            <label>Selecciona la duración:</label>
                            <select onChange={(e) => setPremiumDuration(parseInt(e.target.value))}>
                                <option value="1">1 Mes - $29.99</option>
                                <option value="3">3 Meses - $79.99</option>
                                <option value="12">1 Año - $249.99</option>
                            </select>
                            <div className="price-display">${updatePrice('premium')}</div>
                            <button onClick={() => redirectToPurchase('premium')}>Comprar Plan</button>
                        </div>
                    </div>
                </div>
            </div>
            <button className="btn-back" onClick={() => navigate(-1)}>Volver Atrás</button>
        </main>
    );
};

export default Compras;
