// Alternar la edición de nombre
function toggleEdit(button) {
    const input = button.previousElementSibling;
    if (input.disabled) {
        input.disabled = false;
        button.textContent = "Guardar";
        input.focus();
    } else {
        input.disabled = true;
        button.textContent = "Editar";

        // Llamar a la función para actualizar el nombre y la contraseña
        actualizarUsuario();  // Actualizar tanto el nombre como la contraseña
    }
}

// Obtener información del usuario
async function obtenerUsuario() {
<<<<<<< HEAD

    const token = localStorage.getItem('access_token');  // Usar el token correcto


    const token = localStorage.getItem('access_token');  // Usar el token correcto


    const token = localStorage.getItem('access_token');  // Usar el token correcto


    const token = localStorage.getItem('token');

    const token = localStorage.getItem('access_token');  // Usar el token correcto
 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
=======
<<<<<<< HEAD
    const token = localStorage.getItem('access_token');  // Usar el token correcto
=======
<<<<<<< HEAD
    const token = localStorage.getItem('access_token');  // Usar el token correcto
=======
<<<<<<< HEAD
    const token = localStorage.getItem('access_token');  // Usar el token correcto
=======
<<<<<<< HEAD
    const token = localStorage.getItem('token');
=======
    const token = localStorage.getItem('access_token');  // Usar el token correcto
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
    const errorMessage = document.getElementById('error-message');
    errorMessage.style.display = 'none'; // Ocultar errores previos

    try {
        const response = await fetch('http://localhost:8000/api/usuarios/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
<<<<<<< HEAD







=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
            console.log("User data received:", data);  // <-- Agregar para verificar

            // Asigna los valores obtenidos de la API a los campos del formulario
            document.getElementById('nombre').value = data.nombre;
            document.getElementById('email').value = data.email;

            // Asegúrate de que el campo 'date_joined' existe
            const fechaRegistro = new Date(data.date_joined);
            document.getElementById('fecha-creacion').value = fechaRegistro.toLocaleDateString();

            // Para el estado activo, usa data.es_activo
            console.log("User es_activo:", data.es_activo); 
            document.getElementById('es-activo').value = data.es_activo ? "Activo" : "Inactivo";

<<<<<<< HEAD

 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
=======
=======
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
            console.log("User data received:", data);

            // Asignar los valores obtenidos de la API a los campos del formulario
            document.getElementById('nombre').value = data.nombre;
            document.getElementById('email').value = data.email;
            const fechaRegistro = new Date(data.date_joined);
            document.getElementById('fecha-creacion').value = fechaRegistro.toLocaleDateString();
            document.getElementById('es-activo').value = data.es_activo ? "Activo" : "Inactivo";
<<<<<<< HEAD






 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
        } else {
            errorMessage.textContent = 'Error al cargar los datos del usuario';
            errorMessage.style.display = 'block';
        }
    } catch (error) {
        console.error('Error al obtener la información del usuario:', error);
        errorMessage.textContent = 'Error al conectarse al servidor';
        errorMessage.style.display = 'block';
    }
}

// Actualizar el nombre y/o la contraseña del usuario
async function actualizarUsuario() {
<<<<<<< HEAD

    const token = localStorage.getItem('access_token');  // Usar el token correcto


    const token = localStorage.getItem('access_token');  // Usar el token correcto


    const token = localStorage.getItem('access_token');  // Usar el token correcto


    const token = localStorage.getItem('token');

    const token = localStorage.getItem('access_token');  // Usar el token correcto
 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
=======
<<<<<<< HEAD
    const token = localStorage.getItem('access_token');  // Usar el token correcto
=======
<<<<<<< HEAD
    const token = localStorage.getItem('access_token');  // Usar el token correcto
=======
<<<<<<< HEAD
    const token = localStorage.getItem('access_token');  // Usar el token correcto
=======
<<<<<<< HEAD
    const token = localStorage.getItem('token');
=======
    const token = localStorage.getItem('access_token');  // Usar el token correcto
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
    const nombre = document.getElementById('nombre').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');
    errorMessage.style.display = 'none'; // Ocultar errores previos

    // Validar contraseña
    if (password && password.length < 8) {
        errorMessage.textContent = 'La contraseña debe tener al menos 8 caracteres.';
        errorMessage.style.display = 'block';
        return;
    }

    try {
        const response = await fetch('http://localhost:8000/api/usuarios/', {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre: nombre,  // Envía el nuevo nombre
                password: password || undefined  // Solo envía la contraseña si está presente
            })
        });

        if (response.ok) {
            alert('Usuario actualizado');
            obtenerUsuario();  // Refrescar los datos
        } else {
            errorMessage.textContent = 'Error al actualizar el usuario.';
            errorMessage.style.display = 'block';
        }
    } catch (error) {
        console.error('Error al actualizar el usuario:', error);
        errorMessage.textContent = 'Error al conectarse al servidor.';
        errorMessage.style.display = 'block';
    }
}

// Manejar el formulario de actualización de la contraseña y el nombre
document.getElementById('update-form').addEventListener('submit', function (e) {
    e.preventDefault();
    actualizarUsuario();  // Actualizar tanto el nombre como la contraseña
});

// Cargar datos del usuario cuando se carga la página
document.addEventListener('DOMContentLoaded', function() {
    obtenerUsuario();
});

<<<<<<< HEAD

// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');


// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');


// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');


=======
<<<<<<< HEAD
// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');
=======
<<<<<<< HEAD
// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');
=======
<<<<<<< HEAD
// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');
=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
// Funcionalidad para mostrar y ocultar el menú de usuario
document.getElementById('user-icon').addEventListener('click', function () {
    const dropdown = document.getElementById('user-dropdown');
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
});

// Cerrar sesión
function logout() {
    localStorage.removeItem('token');
<<<<<<< HEAD

// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');
 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
    alert('Has cerrado sesión.');
    window.location.href = '/login';
}
=======
=======
// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');
>>>>>>> a8d19f143da4dcdf7a22fd08e935b212cf57580a
>>>>>>> b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
    alert('Has cerrado sesión.');
    window.location.href = '/login';
}
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
