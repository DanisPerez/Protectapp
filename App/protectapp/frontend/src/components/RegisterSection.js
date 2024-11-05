// src/components/RegisterSection.js
import React, { useState } from 'react';
<<<<<<< HEAD
import { Link } from 'react-router-dom';
=======
import { Link } from 'react-router-dom'; // Importa Link
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
import '../css/RegisterSection.css';
import LoginImage from '../assets/img/Login.png';
import BackImage from '../assets/img/atras.JPG';

const RegisterSection = () => {
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
<<<<<<< HEAD
=======
    const [errorMessage, setErrorMessage] = useState('');
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f

    const handleSubmit = async (event) => {
        event.preventDefault();

<<<<<<< HEAD
        // Validaciones del formulario con alertas
        if (!username.match(/^[a-zA-Z0-9@.+-_]+$/)) {
            alert('Error: El nombre de usuario contiene caracteres no válidos.');
            return;
        }
        if (password.length < 8) {
            alert('Error: La contraseña debe tener al menos 8 caracteres.');
=======
        // Validaciones del formulario
        if (!username.match(/^[a-zA-Z0-9@.+-_]+$/)) {
            setErrorMessage('El nombre de usuario contiene caracteres no válidos.');
            return;
        }
        if (password.length < 8) {
            setErrorMessage('La contraseña debe tener al menos 8 caracteres.');
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/api/register/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, username, password }),
            });

            const data = await response.json();

            if (response.ok) {
<<<<<<< HEAD
                alert('Registro exitoso. Redirigiendo a la página de inicio de sesión...');
                window.location.href = '/login';
            } else {
                // Muestra un mensaje de error específico si el correo ya existe
                if (data.email && data.email[0] === "El correo ya está registrado.") {
                    alert("Error: El correo ya está registrado. Por favor, utilice otro correo.");
                } else {
                    alert(data.error || 'Error en el registro. Intente de nuevo.');
                }
            }
        } catch (error) {
            alert('Ocurrió un error. Intente de nuevo.');
=======
                alert('Registro exitoso');
                window.location.href = '/login';
            } else {
                setErrorMessage(data.error || 'Error en el registro. Intente de nuevo.');
            }
        } catch (error) {
            setErrorMessage('Ocurrió un error. Intente de nuevo.');
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
        }
    };

    return (
        <section className="register-section" data-aos="fade-up">
            <div className="register-image">
                <img src={LoginImage} alt="Register Image" className="img-fluid rounded" />
            </div>
            <div className="register-form-container">
                <h2>Regístrese en Protect</h2>
                <p className="text-center">
<<<<<<< HEAD
                    ¿Ya tiene una cuenta? <Link to="/login">Inicie sesión</Link>
=======
                ¿Ya tiene una cuenta? <Link to="/login">Inicie sesión</Link>
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                </p>

                <div className="social-buttons">
                    <button type="button" id="googleSignInBtn" className="btn-google">
                        <i className="fab fa-google"></i> Registrarse con Google
                    </button>
                </div>

                <div className="divider">o</div>

                <form onSubmit={handleSubmit} className="register-form">
                    <div className="form-group">
                        <label htmlFor="email">Dirección de correo electrónico</label>
                        <input
                            type="email"
                            className="form-control"
                            id="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="Ingrese su correo electrónico"
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="username">Nombre de usuario</label>
                        <input
                            type="text"
                            className="form-control"
                            id="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Ingrese su nombre de usuario"
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Contraseña</label>
                        <input
                            type="password"
                            className="form-control"
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Ingrese su contraseña"
                            required
                        />
                    </div>
<<<<<<< HEAD

=======
                    {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
                    <button type="submit" className="btn btn-primary btn-block mt-3">Crear cuenta</button>
                </form>

                <div className="text-center mt-3">
                    <p>
                        Al crear una cuenta, confirmo que he leído y aceptado los{' '}
                        <a href="/terminos">Términos de Uso</a> y la{' '}
                        <a href="/politica">Política de Privacidad</a>.
                    </p>
                </div>

                <div className="back-button">
                    <Link to="/login">
                        <img src={BackImage} alt="Regresar" title="Regresar a la página de inicio de sesión" />
                    </Link>
                </div>
            </div>
        </section>
    );
};

export default RegisterSection;
