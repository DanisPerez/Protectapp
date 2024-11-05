// mis_dispositivos.js








const token = localStorage.getItem('access_token');
const errorMessage = document.getElementById('error-message');

// Función para obtener dispositivos
async function obtenerDispositivos() {
    try {
        const response = await fetch('http://localhost:8000/api/dispositivos/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }

 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
// Obtener los tokens desde localStorage
let token = localStorage.getItem('access_token');
const refreshToken = localStorage.getItem('refresh_token');
const errorMessage = document.getElementById('error-message');

// Verificar si no hay token de acceso, redirigir al login
if (!token) {
    alert("Token no encontrado, por favor inicia sesión.");
    window.location.href = 'http://127.0.0.1:8000/login/';
}

// Función para renovar el token de acceso usando el token de refresh
async function renovarToken() {
    if (refreshToken) {
        try {
            const response = await fetch('http://localhost:8000/api/token/refresh/', {
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
                window.location.href = 'http://127.0.0.1:8000/login/';
                return false;
            }
        } catch (error) {
            console.error('Error al renovar el token:', error);
            alert('Error al renovar el token. Por favor, inicia sesión de nuevo.');
            window.location.href = 'http://127.0.0.1:8000/login/';
            return false;
        }
    } else {
        alert('No se encontró un refresh token. Por favor, inicia sesión.');
        window.location.href = 'http://127.0.0.1:8000/login/';
        return false;
    }
}

// Función para verificar si el token es válido o necesita renovación
async function verificarYRenovarToken() {
    if (!token) {
        alert("Token no encontrado, por favor inicia sesión.");
        window.location.href = 'http://127.0.0.1:8000/login/';
        return false;
    } else {
        try {
            const response = await fetch('http://localhost:8000/api/dispositivos/', {
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
            window.location.href = 'http://127.0.0.1:8000/login/';
            return false;
        }
    }
}

// Función para obtener dispositivos

// Función para obtener dispositivos

 afc917d1d14c3730d6946130d053056968a08dc6
async function obtenerDispositivos() {
    const tokenValido = await verificarYRenovarToken();

    if (!tokenValido) return;

    try {
        const response = await fetch('http://localhost:8000/api/dispositivos/', {
            method: 'GET',
            headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' }






 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
        });

        if (response.ok) {
            const data = await response.json();
            const listaDispositivos = document.getElementById('lista-dispositivos');

            listaDispositivos.innerHTML = '';


            listaDispositivos.innerHTML = '';


            listaDispositivos.innerHTML = '';


            listaDispositivos.innerHTML = ''; // Limpiar la lista antes de agregar dispositivos

            listaDispositivos.innerHTML = '';
 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
            data.forEach(dispositivo => {
                const card = `
                    <div class="col-md-4 mb-4">
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">${dispositivo.nombre}</h5>
                                <p class="card-text">Modelo: ${dispositivo.modelo || 'Desconocido'}</p>
                                <p class="card-text">Estado: ${dispositivo.estado ? 'Activo' : 'Inactivo'}</p>

                                <button class="btn btn-info" onclick="editarNombreDispositivo(${dispositivo.id}, '${dispositivo.nombre}')">Cambiar Nombre</button>
                                <!-- Nuevo botón para redirigir a la página de eventos -->
                                <button class="btn btn-info" onclick="redirigirAEventos(${dispositivo.id})">Historial de eventos</button>


                                <button class="btn btn-info" onclick="editarNombreDispositivo(${dispositivo.id}, '${dispositivo.nombre}')">Cambiar Nombre</button>


                                <button class="btn btn-info" onclick="editarNombreDispositivo(${dispositivo.id}, '${dispositivo.nombre}')">Cambiar Nombre</button>


                                <button class="btn btn-info" onclick="redirigirAlPanel(${dispositivo.id})">Ver Panel</button>

                                <button class="btn btn-info" onclick="editarNombreDispositivo(${dispositivo.id}, '${dispositivo.nombre}')">Cambiar Nombre</button>
 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
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



function redirigirAEventos(dispositivoId) {
    // Guardar el ID del dispositivo en localStorage
    localStorage.setItem('dispositivoSeleccionado', dispositivoId);
    // Redirigir a la página correcta de eventos
    window.location.href = `/dispositivo/${dispositivoId}/reg_event`;
}








// Función para agregar un nuevo dispositivo
document.getElementById('add-device-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const nombreDispositivo = document.getElementById('nombre-dispositivo').value;

    try {
        const response = await fetch('http://localhost:8000/api/dispositivos/', {
            method: 'POST',

 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
// Función para abrir el modal de cambiar nombre
let dispositivoIdActual = null; // Guardar el ID del dispositivo actual

function editarNombreDispositivo(dispositivoId, nombreActual) {
    dispositivoIdActual = dispositivoId;  // Guardar el ID del dispositivo que se va a editar
    document.getElementById('nombre-dispositivo').value = nombreActual;
    $('#addDeviceModal').modal('show');
}

// Función para cambiar el nombre del dispositivo al hacer submit en el formulario
document.getElementById('add-device-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    
    const nuevoNombre = document.getElementById('nombre-dispositivo').value;

    if (!dispositivoIdActual) return;  // Si no hay un dispositivo seleccionado, no hacer nada

    try {
        const response = await fetch(`http://localhost:8000/api/dispositivos/${dispositivoIdActual}/`, {
            method: 'PUT',






 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },







            body: JSON.stringify({
                nombre: nombreDispositivo
            })
        });

        if (response.ok) {
            $('#addDeviceModal').modal('hide'); // Cerrar el modal
            obtenerDispositivos(); // Refrescar la lista de dispositivos
        } else {
            throw new Error('Error agregando el dispositivo');
        }
    } catch (error) {
        console.error('Error agregando el dispositivo:', error);
        errorMessage.textContent = 'Error al agregar el dispositivo. Intente de nuevo.';
    }
});

// Función para redirigir al panel de control del dispositivo
function redirigirAlPanel(dispositivoId) {
    // Redirigir a dispositivo_control.html pasando el ID del dispositivo como parámetro en la URL
    window.location.href = `/dispositivo_control.html?id=${dispositivoId}`;
}


 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
            body: JSON.stringify({ nombre: nuevoNombre })
        });

        if (response.ok) {
            $('#addDeviceModal').modal('hide');
            obtenerDispositivos();  // Actualizar la lista de dispositivos
        } else if (response.status === 401 || response.status === 403) {
            window.location.href = 'http://127.0.0.1:8000/login/';
        } else {
            throw new Error('Error cambiando el nombre del dispositivo');
        }
    } catch (error) {
        console.error('Error cambiando el nombre del dispositivo:', error);
        errorMessage.textContent = 'Error al cambiar el nombre. Intente de nuevo.';
        errorMessage.style.display = 'block';
    }
});







 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
// Sondeo para actualizar el estado de los dispositivos cada 10 segundos
setInterval(obtenerDispositivos, 10000);

// Ejecutar la función al cargar la página

obtenerDispositivos();

obtenerDispositivos();
 afc917d1d14c3730d6946130d053056968a08dc6