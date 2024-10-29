import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import '../css/LoginSection.css';
import LoginImage from '../assets/img/Login.png';
import BackImage from '../assets/img/atras.JPG';

const LoginSection = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!email || !password) {
            setErrorMessage('Por favor, completa todos los campos.');
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            });

            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('access_token', data.access);
                window.location.href = '/inicio';
            } else {
                const data = await response.json();
                setErrorMessage(data.detail || 'Credenciales inválidas');
            }
        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            setErrorMessage('Ocurrió un error. Intente nuevamente.');
        }
    };

    return (
        <section className="login-section">
            <div className="login-image">
                <img src={LoginImage} alt="Pantalla de inicio de sesión" className="img-fluid rounded" />
            </div>
            <div className="login-form-container">
                <h2>Inicie sesión con su ID de Protect</h2>
                <form onSubmit={handleSubmit} className="login-form">
                    <div className="form-group">
                        <label htmlFor="email">Dirección de correo electrónico</label>
                        <input
                            type="email"
                            className="form-control"
                            id="email"
                            name="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>
                    <div className="form-group password-container">
                        <label htmlFor="password">Contraseña</label>
                        <input
                            type="password"
                            className="form-control"
                            id="password"
                            name="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                    {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}
                    <button type="submit" className="btn btn-primary btn-block mt-3">Iniciar Sesión</button>
                </form>
                <div className="text-center mt-4">
                    <p>¿No tienes una cuenta? <Link to="/register">Inscribirse</Link></p>
                </div>
                <div className="back-button">
                    <Link to="/">
                        <img src={BackImage} alt="Regresar" title="Regresar a la página anterior" />
                    </Link>
                </div>
            </div>
        </section>
    );
};

export default LoginSection;
