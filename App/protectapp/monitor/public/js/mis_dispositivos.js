// mis_dispositivos.js

// Obtener los tokens desde localStorage
let token = localStorage.getItem('access_token');
const refreshToken = localStorage.getItem('refresh_token');
const errorMessage = document.getElementById('error-message');

// Verificar si no hay token de acceso, redirigir al login
if (!token) {
    alert("Token no encontrado, por favor inicia sesión.");
    window.location.href = '/login/';
}

// Función para renovar el token de acceso usando el token de refresh
async function renovarToken() {
    if (refreshToken) {
        try {
            const response = await fetch('/api/token/refresh/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ refresh: refreshToken })
            });

            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('access_token', data.access);
                token = data.access;
                return true;
            } else {
                alert('Tu sesión ha expirado. Por favor, inicia sesión nuevamente.');
                window.location.href = '/login/';
                return false;
            }
        } catch (error) {
            console.error('Error al renovar el token:', error);
            alert('Error al renovar el token. Por favor, inicia sesión de nuevo.');
            window.location.href = '/login/';
            return false;
        }
    } else {
        alert('No se encontró un refresh token. Por favor, inicia sesión.');
        window.location.href = '/login/';
        return false;
    }
}

// Función para verificar si el token es válido o necesita renovación
async function verificarYRenovarToken() {
    if (!token) {
        alert("Token no encontrado, por favor inicia sesión.");
        window.location.href = '/login/';
        return false;
    } else {
        try {
            const response = await fetch('/api/dispositivos/', {
                method: 'GET',
                headers: { 'Authorization': `Bearer ${token}` }
            });

            if (response.status === 401 || response.status === 403) {
                const tokenRenovado = await renovarToken();
                return tokenRenovado;
            } else {
                return true;
            }
        } catch (error) {
            console.error('Error verificando el token:', error);
            window.location.href = '/login/';
            return false;
        }
    }
}

// Función para obtener dispositivos
async function obtenerDispositivos() {
    const tokenValido = await verificarYRenovarToken();

    if (!tokenValido) return;

    try {
        const response = await fetch('/api/dispositivos/', {
            method: 'GET',
            headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            const data = await response.json();
            const listaDispositivos = document.getElementById('lista-dispositivos');
            listaDispositivos.innerHTML = '';
            data.forEach(dispositivo => {
                const card = `
                    <div class="col-md-4 mb-4">
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">${dispositivo.nombre}</h5>
                                <p class="card-text">Modelo: ${dispositivo.modelo || 'Desconocido'}</p>
                                <p class="card-text">Estado: ${dispositivo.estado ? 'Activo' : 'Inactivo'}</p>
                                <button class="btn btn-info" onclick="editarNombreDispositivo(${dispositivo.id}, '${dispositivo.nombre}')">Cambiar Nombre</button>
                                <button class="btn btn-info" onclick="redirigirAEventos(${dispositivo.id})">Historial de eventos</button>
                            </div>
                        </div>
                    </div>
                `;
                listaDispositivos.insertAdjacentHTML('beforeend', card);
            });
        } else {
            throw new Error('Error obteniendo los dispositivos');
        }
    } catch (error) {
        console.error('Error obteniendo los dispositivos:', error);
        errorMessage.textContent = 'Error al cargar los dispositivos';
        errorMessage.style.display = 'block';
    }
}

// Función para redirigir a eventos
function redirigirAEventos(dispositivoId) {
    localStorage.setItem('dispositivoSeleccionado', dispositivoId);
    window.location.href = `/dispositivo/${dispositivoId}/reg_event`;
}

// Función para abrir el modal de cambiar nombre
let dispositivoIdActual = null;

function editarNombreDispositivo(dispositivoId, nombreActual) {
    dispositivoIdActual = dispositivoId;
    document.getElementById('nombre-dispositivo').value = nombreActual;
    $('#addDeviceModal').modal('show');
}

// Función para cambiar el nombre del dispositivo
document.getElementById('add-device-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    
    const nuevoNombre = document.getElementById('nombre-dispositivo').value;

    if (!dispositivoIdActual) return;

    try {
        const response = await fetch(`/api/dispositivos/${dispositivoIdActual}/`, {
            method: 'PUT',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nombre: nuevoNombre })
        });

        if (response.ok) {
            $('#addDeviceModal').modal('hide');
            obtenerDispositivos();
        } else if (response.status === 401 || response.status === 403) {
            window.location.href = '/login/';
        } else {
            throw new Error('Error cambiando el nombre del dispositivo');
        }
    } catch (error) {
        console.error('Error cambiando el nombre del dispositivo:', error);
        errorMessage.textContent = 'Error al cambiar el nombre. Intente de nuevo.';
        errorMessage.style.display = 'block';
    }
});

<<<<<<< HEAD
<<<<<<< HEAD


=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
// Sondeo para actualizar el estado de los dispositivos cada 10 segundos
setInterval(obtenerDispositivos, 10000);

// Ejecutar la función al cargar la página
obtenerDispositivos();
