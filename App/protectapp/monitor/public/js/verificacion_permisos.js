<<<<<<< HEAD
=======

>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
const token = localStorage.getItem('access_token');
const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
const spinner = document.getElementById('spinner');

// Mostrar el spinner mientras se cargan los permisos
function mostrarSpinner(mostrar = true) {
    spinner.style.display = mostrar ? 'inline-block' : 'none';
}

// Verificar si el usuario está autenticado y si hay un dispositivo seleccionado
function verificarSesion() {
    if (!token || !dispositivoId) {
        alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
        window.location.href = '/login';  // Redirigir si no hay token o dispositivo
    }
}

// Llamar a la verificación de sesión
verificarSesion();

// Función para obtener el estado de los permisos
async function obtenerPermisos() {
    try {
        mostrarSpinner(true);
        const response = await fetch(`/api/dispositivos/${dispositivoId}/verificacion-permisos/`, {
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
                        <td>${permiso.tipo_permiso || 'No disponible'}</td> <!-- Mostrar el tipo de permiso -->
                        <td>${permiso.estado ? 'Concedido' : 'Denegado'}</td>
                        <td>${permiso.critico ? 'Sí' : 'No'}</td> <!-- Mostrar si el permiso es crítico -->
                        <td>${permiso.fecha_verificacion || 'No disponible'}</td> <!-- Mostrar la fecha de verificación -->
                    </tr>
                `;
                listaPermisos.insertAdjacentHTML('beforeend', row);
            });
        } else {
            listaPermisos.innerHTML = '<tr><td colspan="6" class="text-center">No hay permisos disponibles.</td></tr>';
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
        const response = await fetch(`/api/dispositivos/${dispositivoId}/solicitar-permiso/${permisoId}/`, {
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
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
// Sondeo para actualizar el estado de los permisos cada 10 segundos
setInterval(obtenerPermisos, 10000);

// Cargar permisos cuando la página se carga por primera vez
document.addEventListener('DOMContentLoaded', obtenerPermisos);
