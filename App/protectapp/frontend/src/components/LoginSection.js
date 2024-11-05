<<<<<<< HEAD
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
=======
<<<<<<< HEAD
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
=======
// src/components/LoginSection.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom'; // Importa Link
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
import '../css/LoginSection.css';
import LoginImage from '../assets/img/Login.png';
import BackImage from '../assets/img/atras.JPG';

const LoginSection = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
<<<<<<< HEAD
    const [showPassword, setShowPassword] = useState(false);

    const toggleShowPassword = () => {
        setShowPassword(!showPassword);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!email || !password) {
            alert('Por favor, completa todos los campos.');
            return;
        }

        try {
=======
    const [errorMessage, setErrorMessage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!email || !password) {
            setErrorMessage('Por favor, completa todos los campos.');
            return;
        }
        try {
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            const response = await fetch('http://localhost:8000/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
<<<<<<< HEAD
=======
=======
            const response = await fetch('/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': 'csrftoken_placeholder', // Agregar el token CSRF si es necesario
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                },
                body: JSON.stringify({ email, password }),
            });

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('access_token', data.access);
                window.location.href = '/inicio';
            } else {
                const data = await response.json();
<<<<<<< HEAD
                
                if (data.detail === 'Correo no encontrado') {
                    alert('El correo electrónico no está registrado.');
                } else if (data.detail === 'Contraseña incorrecta') {
                    alert('La contraseña es incorrecta.');
                } else {
                    alert('Credenciales inválidas.');
                }
            }
        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            alert('Ocurrió un error. Intente nuevamente.');
=======
                setErrorMessage(data.detail || 'Credenciales inválidas');
            }
=======
            if (!response.ok) {
                const data = await response.json();
                setErrorMessage(data.detail || 'Credenciales inválidas');
                return;
            }

            window.location.href = '/inicio';
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            setErrorMessage('Ocurrió un error. Intente nuevamente.');
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
        }
    };

    return (
        <section className="login-section">
            <div className="login-image">
<<<<<<< HEAD
                <img src={LoginImage} alt="Pantalla de inicio de sesión" className="img-fluid rounded" />
=======
<<<<<<< HEAD
                <img src={LoginImage} alt="Pantalla de inicio de sesión" className="img-fluid rounded" />
=======
            <img src={LoginImage} alt="Pantalla de inicio de sesión" className="img-fluid rounded" />
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
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
<<<<<<< HEAD
                        <div className="password-wrapper">
                            <input
                                type={showPassword ? 'text' : 'password'}
                                className="form-control"
                                id="password"
                                name="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                            <span
                                className="toggle-password"
                                onClick={toggleShowPassword}
                                style={{ cursor: 'pointer', marginLeft: '10px' }}
                            >
                                {showPassword ? '🙈' : '👁️'}
                            </span>
                        </div>
                    </div>
=======
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
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
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
