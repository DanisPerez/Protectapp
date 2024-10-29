<<<<<<< HEAD

const token = localStorage.getItem('access_token');
const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
=======
const token = localStorage.getItem('access_token');
<<<<<<< HEAD
const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
const spinner = document.getElementById('spinner');

// Mostrar el spinner mientras se cargan los permisos
function mostrarSpinner(mostrar = true) {
    spinner.style.display = mostrar ? 'inline-block' : 'none';
}

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
// Verificar si el usuario está autenticado y si hay un dispositivo seleccionado
function verificarSesion() {
    if (!token || !dispositivoId) {
        alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
        window.location.href = '/login';  // Redirigir si no hay token o dispositivo
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
// Verificar si el usuario está autenticado al cargar la página
function verificarSesion() {
    if (!token) {
        alert('Tu sesión ha expirado o no has iniciado sesión.');
        window.location.href = '/login'; // Redirigir a la página de inicio de sesión si no hay token
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
    }
}

// Llamar a la verificación de sesión
verificarSesion();

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
// Función para obtener el estado de los permisos
async function obtenerPermisos() {
    try {
        mostrarSpinner(true);
<<<<<<< HEAD
        const response = await fetch(`/api/dispositivos/${dispositivoId}/verificacion-permisos/`, {
=======
<<<<<<< HEAD
        const response = await fetch(`/api/dispositivos/${dispositivoId}/verificacion-permisos/`, {
=======
        const response = await fetch('/api/dispositivos/1/verificacion-permisos/', {
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
            method: 'GET',
            headers: { 
                'Authorization': 'Bearer ' + token
            }
        });

        if (!response.ok) {
            throw new Error('Error al obtener los permisos');
        }

        const permisos = await response.json();
        const listaPermisos = document.getElementById('lista-permisos');
        listaPermisos.innerHTML = ''; // Limpiar tabla antes de llenarla

        if (permisos.length > 0) {
            permisos.forEach((permiso, index) => {
                const row = `
                    <tr>
                        <td>${index + 1}</td>
                        <td>${permiso.permiso}</td>
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
                        <td>${permiso.tipo_permiso || 'No disponible'}</td> <!-- Mostrar el tipo de permiso -->
                        <td>${permiso.estado ? 'Concedido' : 'Denegado'}</td>
                        <td>${permiso.critico ? 'Sí' : 'No'}</td> <!-- Mostrar si el permiso es crítico -->
                        <td>${permiso.fecha_verificacion || 'No disponible'}</td> <!-- Mostrar la fecha de verificación -->
<<<<<<< HEAD
=======
=======
                        <td>${permiso.estado ? 'Concedido' : 'Denegado'}</td>
                        <td>
                            ${!permiso.estado ? `<button class="btn btn-warning btn-request" onclick="solicitarPermiso(${permiso.id})">Solicitar Permiso</button>` : ''}
                        </td>
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
                    </tr>
                `;
                listaPermisos.insertAdjacentHTML('beforeend', row);
            });
        } else {
<<<<<<< HEAD
            listaPermisos.innerHTML = '<tr><td colspan="6" class="text-center">No hay permisos disponibles.</td></tr>';
=======
<<<<<<< HEAD
            listaPermisos.innerHTML = '<tr><td colspan="6" class="text-center">No hay permisos disponibles.</td></tr>';
=======
            listaPermisos.innerHTML = '<tr><td colspan="4" class="text-center">No hay permisos disponibles.</td></tr>';
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
        }

        mostrarSpinner(false);
        
    } catch (error) {
        console.error('Error al obtener los permisos:', error);
        alert('Error al cargar los permisos.');
        mostrarSpinner(false);
    }
}

// Función para solicitar un permiso
async function solicitarPermiso(permisoId) {
    try {
<<<<<<< HEAD
        const response = await fetch(`/api/dispositivos/${dispositivoId}/solicitar-permiso/${permisoId}/`, {
=======
<<<<<<< HEAD
        const response = await fetch(`/api/dispositivos/${dispositivoId}/solicitar-permiso/${permisoId}/`, {
=======
        const response = await fetch(`/api/dispositivos/1/solicitar-permiso/${permisoId}/`, {
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
            method: 'POST',
            headers: { 
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            alert('Permiso solicitado exitosamente');
            obtenerPermisos();  // Actualizar la lista de permisos después de solicitar uno nuevo
        } else {
            alert('Error al solicitar el permiso.');
        }
        
    } catch (error) {
        console.error('Error al solicitar el permiso:', error);
        alert('Error al solicitar el permiso.');
    }
}

<<<<<<< HEAD
=======
<<<<<<< HEAD
// Redirigir a la página de registro de eventos
document.getElementById('registro-link').addEventListener('click', function () {
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    
    if (dispositivoId) {
        window.location.href = `/dispositivo/${dispositivoId}/reg_event`;
    } else {
        alert('No se ha seleccionado un dispositivo.');
        window.location.href = '/mis_dispositivos';  // Redirigir a la lista de dispositivos si no hay ID
    }
});

=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
// Sondeo para actualizar el estado de los permisos cada 10 segundos
setInterval(obtenerPermisos, 10000);

// Cargar permisos cuando la página se carga por primera vez
document.addEventListener('DOMContentLoaded', obtenerPermisos);
