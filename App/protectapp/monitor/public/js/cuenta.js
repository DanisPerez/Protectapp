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

// Obtener el token de autenticación
function getToken() {
    return localStorage.getItem('access_token');
}

// Obtener información del usuario
async function obtenerUsuario() {
    const token = getToken();
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
            console.log("User data received:", data);

            // Asignar los valores obtenidos de la API a los campos del formulario
            document.getElementById('nombre').value = data.nombre;
            document.getElementById('email').value = data.email;
            const fechaRegistro = new Date(data.date_joined);
            document.getElementById('fecha-creacion').value = fechaRegistro.toLocaleDateString();
            document.getElementById('es-activo').value = data.es_activo ? "Activo" : "Inactivo";
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
    const token = getToken();
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

// Cerrar sesión
function logout() {
    localStorage.removeItem('access_token');
    alert('Has cerrado sesión.');
    window.location.href = '/login';
}

// Funcionalidad para mostrar y ocultar el menú de usuario
document.getElementById('user-icon').addEventListener('click', function () {
    const dropdown = document.getElementById('user-dropdown');
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
});

