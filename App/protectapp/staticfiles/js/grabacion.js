const token = localStorage.getItem('access_token');

const dispositivoId = localStorage.getItem('dispositivoSeleccionado');

if (!token || !dispositivoId) {
    alert('Tu sesión ha expirado o no se ha seleccionado un dispositivo.');
    window.location.href = '/login';  // Redirigir si no hay token o dispositivo seleccionado
}









 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
// Verificar si el usuario está autenticado al cargar la página
if (!token) {
    alert('Tu sesión ha expirado o no has iniciado sesión.');
    window.location.href = '/login'; // Redirigir a la página de inicio de sesión si no hay token
}





 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
// Función para mostrar alertas
function mostrarAlerta(id, mensaje, tipo = 'info') {
    const alerta = document.getElementById(id);
    alerta.className = `alert alert-${tipo}`;
    alerta.innerText = mensaje;
    alerta.style.display = 'block';

    setTimeout(() => {
        alerta.style.display = 'none';
    }, 3000);  // Ocultar la alerta después de 3 segundos


    setTimeout(() => {
        alerta.style.display = 'none';
    }, 3000); // Oculta la alerta después de 3 segundos


    setTimeout(() => {
        alerta.style.display = 'none';
    }, 3000); // Oculta la alerta después de 3 segundos


    setTimeout(() => { alerta.style.display = 'none'; }, 3000); // Oculta la alerta después de 3 segundos

    setTimeout(() => {
        alerta.style.display = 'none';
    }, 3000); // Oculta la alerta después de 3 segundos
 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
}

// Función para mostrar el spinner mientras se procesa
function mostrarSpinner(idSpinner, mostrar = true) {
    const spinner = document.getElementById(idSpinner);
    spinner.style.display = mostrar ? 'inline-block' : 'none';
}

// Función genérica para iniciar o detener grabación con fetch
async function manejarGrabacion(url, alertaId, spinnerId, mensajeExito, mensajeError) {
    try {
        mostrarSpinner(spinnerId, true);
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            }
        });
        mostrarSpinner(spinnerId, false);

        if (response.ok) {
            mostrarAlerta(alertaId, mensajeExito, 'success');
        } else {
            mostrarAlerta(alertaId, mensajeError, 'danger');
        }
    } catch (error) {
        mostrarSpinner(spinnerId, false);
        mostrarAlerta(alertaId, mensajeError, 'danger');
        console.error('Error al manejar la grabación:', error);
    }
}


// Eventos para grabación de llamadas
document.getElementById('iniciarLlamada').addEventListener('click', function () {
    manejarGrabacion(`http://localhost:8000/api/dispositivos/${dispositivoId}/grabar-llamada/`, 'alertLlamada', 'spinnerLlamada',






// Grabación de Llamadas
document.getElementById('iniciarLlamada').addEventListener('click', function() {
    manejarGrabacion('http://localhost:8000/api/dispositivos/1/grabar-llamada/', 'alertLlamada', 'spinnerLlamada', 
        'Grabación de llamada iniciada.', 'Error al iniciar la grabación de llamada.');
});

document.getElementById('detenerLlamada').addEventListener('click', function() {
    manejarGrabacion('http://localhost:8000/api/dispositivos/1/detener-grabacion/', 'alertLlamada', 'spinnerLlamada', 
        'Grabación de llamada detenida.', 'Error al detener la grabación de llamada.');
});

// Grabación de Pantalla
document.getElementById('iniciarPantalla').addEventListener('click', function() {
    manejarGrabacion('http://localhost:8000/api/dispositivos/1/grabar-pantalla/', 'alertPantalla', 'spinnerPantalla', 
        'Grabación de pantalla iniciada.', 'Error al iniciar la grabación de pantalla.');
});

document.getElementById('detenerPantalla').addEventListener('click', function() {
    manejarGrabacion('http://localhost:8000/api/dispositivos/1/detener-grabacion-pantalla/', 'alertPantalla', 'spinnerPantalla', 
        'Grabación de pantalla detenida.', 'Error al detener la grabación de pantalla.');
});

 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
// Eventos para grabación de llamadas
document.getElementById('iniciarLlamada').addEventListener('click', function () {
    manejarGrabacion('http://localhost:8000/api/dispositivos/1/grabar-llamada/', 'alertLlamada', 'spinnerLlamada',
 afc917d1d14c3730d6946130d053056968a08dc6
        'Grabación de llamada iniciada.', 'Error al iniciar la grabación de llamada.');
});

document.getElementById('detenerLlamada').addEventListener('click', function () {

    manejarGrabacion(`http://localhost:8000/api/dispositivos/${dispositivoId}/detener-grabacion/`, 'alertLlamada', 'spinnerLlamada',

    manejarGrabacion('http://localhost:8000/api/dispositivos/1/detener-grabacion/', 'alertLlamada', 'spinnerLlamada',
 afc917d1d14c3730d6946130d053056968a08dc6
        'Grabación de llamada detenida.', 'Error al detener la grabación de llamada.');
});

// Eventos para grabación de pantalla
document.getElementById('iniciarPantalla').addEventListener('click', function () {

    manejarGrabacion(`http://localhost:8000/api/dispositivos/${dispositivoId}/grabar-pantalla/`, 'alertPantalla', 'spinnerPantalla',

    manejarGrabacion('http://localhost:8000/api/dispositivos/1/grabar-pantalla/', 'alertPantalla', 'spinnerPantalla',
 afc917d1d14c3730d6946130d053056968a08dc6
        'Grabación de pantalla iniciada.', 'Error al iniciar la grabación de pantalla.');
});

document.getElementById('detenerPantalla').addEventListener('click', function () {

    manejarGrabacion(`http://localhost:8000/api/dispositivos/${dispositivoId}/detener-grabacion-pantalla/`, 'alertPantalla', 'spinnerPantalla',

    manejarGrabacion('http://localhost:8000/api/dispositivos/1/detener-grabacion-pantalla/', 'alertPantalla', 'spinnerPantalla',
 afc917d1d14c3730d6946130d053056968a08dc6
        'Grabación de pantalla detenida.', 'Error al detener la grabación de pantalla.');
});

// Cerrar sesión
document.getElementById('cerrar-sesion').addEventListener('click', function () {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');

    localStorage.removeItem('dispositivoSeleccionado');
    window.location.href = '/login';  // Redirigir al login después de cerrar sesión

    window.location.href = '/login'; // Redirigir al login después de cerrar sesión
 afc917d1d14c3730d6946130d053056968a08dc6
});

// Función para alternar el despliegue del menú del usuario
document.getElementById('user-icon').addEventListener('click', function () {
    const dropdown = document.getElementById('user-dropdown');
    dropdown.style.display = (dropdown.style.display === 'none' || dropdown.style.display === '') ? 'block' : 'none';
});

// Cerrar el menú si se hace clic fuera de él
document.addEventListener('click', function (event) {
    const dropdown = document.getElementById('user-dropdown');
    if (!event.target.closest('.user-info')) {
        dropdown.style.display = 'none';
    }

});

// Redirigir a la página de registro de eventos
document.getElementById('registro-link').addEventListener('click', function () {
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    if (dispositivoId) {
        window.location.href = `/dispositivo/${dispositivoId}/reg_event`;
    } else {
        alert('No se ha seleccionado un dispositivo.');
        window.location.href = '/mis_dispositivos';  // Redirigir si no hay ID
    }
});


});


});

});
 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6