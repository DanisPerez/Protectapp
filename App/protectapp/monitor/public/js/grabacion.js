<<<<<<< HEAD
<<<<<<< HEAD
// Obtener el token y dispositivoId desde localStorage
const token = localStorage.getItem('access_token');
let dispositivoId = localStorage.getItem('dispositivoSeleccionado');

// Forzar un dispositivoId manual para pruebas (descomenta esta línea para pruebas manuales)
// dispositivoId = 13; // Sustituye por un ID válido si necesitas probar manualmente

// Verificar si el token o el dispositivoId están ausentes o inválidos
if (!token || !dispositivoId) {
    console.error('Faltan token o dispositivoId en localStorage. Redirigiendo al login.');
    alert('Tu sesión ha expirado o no se ha seleccionado un dispositivo.');
    window.location.href = '/login';  // Redirigir si no hay token o dispositivo seleccionado
} else {
    console.log(`Dispositivo seleccionado: ${dispositivoId}`);
    // Validar dispositivoId antes de continuar
    if (dispositivoId === 'undefined' || dispositivoId === null || dispositivoId === '') {
        console.error('dispositivoId es inválido. Asegúrate de que esté correctamente almacenado.');
        alert('Error: No se ha seleccionado un dispositivo válido.');
        window.location.href = '/mis_dispositivos';  // Redirigir si no hay dispositivo válido
    }
}

=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
// Función para mostrar alertas
function mostrarAlerta(id, mensaje, tipo = 'info') {
    const alerta = document.getElementById(id);
    alerta.className = `alert alert-${tipo}`;
    alerta.innerText = mensaje;
    alerta.style.display = 'block';
<<<<<<< HEAD
<<<<<<< HEAD
    setTimeout(() => {
        alerta.style.display = 'none';
    }, 3000);  // Ocultar la alerta después de 3 segundos
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
}

// Función para mostrar el spinner mientras se procesa
function mostrarSpinner(idSpinner, mostrar = true) {
    const spinner = document.getElementById(idSpinner);
    spinner.style.display = mostrar ? 'inline-block' : 'none';
}

<<<<<<< HEAD
<<<<<<< HEAD
// Habilitar y deshabilitar botones
function cambiarEstadoBotones(iniciarBtn, detenerBtn, iniciar = true) {
    document.getElementById(iniciarBtn).disabled = !iniciar;
    document.getElementById(detenerBtn).disabled = iniciar;
}

// Función genérica para iniciar o detener grabación con fetch
async function manejarGrabacion(url, alertaId, spinnerId, iniciarBtn, detenerBtn, mensajeExito, mensajeError) {
    if (!dispositivoId) {
        console.error('Error: dispositivoId no está definido.');
        mostrarAlerta(alertaId, 'Error al obtener el ID del dispositivo.', 'danger');
        return;
    }

=======
// Función genérica para iniciar o detener grabación con fetch
async function manejarGrabacion(url, alertaId, spinnerId, mensajeExito, mensajeError) {
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
// Función genérica para iniciar o detener grabación con fetch
async function manejarGrabacion(url, alertaId, spinnerId, mensajeExito, mensajeError) {
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
<<<<<<< HEAD
            cambiarEstadoBotones(iniciarBtn, detenerBtn, false);  // Deshabilitar botón de iniciar y habilitar el de detener
=======
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
        } else {
            mostrarAlerta(alertaId, mensajeError, 'danger');
        }
    } catch (error) {
        mostrarSpinner(spinnerId, false);
        mostrarAlerta(alertaId, mensajeError, 'danger');
        console.error('Error al manejar la grabación:', error);
    }
}

<<<<<<< HEAD
<<<<<<< HEAD
// Eventos para grabación de llamadas
document.getElementById('iniciarLlamada').addEventListener('click', function () {
    if (dispositivoId) {
        manejarGrabacion(`http://localhost:8000/api/dispositivos/${dispositivoId}/grabar-llamada/`, 
            'alertLlamada', 'spinnerLlamada', 'iniciarLlamada', 'detenerLlamada',
            'Grabación de llamada iniciada.', 'Error al iniciar la grabación de llamada.');
    } else {
        console.error('dispositivoId no está definido.');
    }
});

document.getElementById('detenerLlamada').addEventListener('click', function () {
    if (dispositivoId) {
        manejarGrabacion(`http://localhost:8000/api/dispositivos/${dispositivoId}/detener-grabacion/`, 
            'alertLlamada', 'spinnerLlamada', 'detenerLlamada', 'iniciarLlamada',
            'Grabación de llamada detenida.', 'Error al detener la grabación de llamada.');
    } else {
        console.error('dispositivoId no está definido.');
    }
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
});

// Eventos para grabación de pantalla
document.getElementById('iniciarPantalla').addEventListener('click', function () {
<<<<<<< HEAD
<<<<<<< HEAD
    if (dispositivoId) {
        manejarGrabacion(`http://localhost:8000/api/dispositivos/${dispositivoId}/grabar-pantalla/`, 
            'alertPantalla', 'spinnerPantalla', 'iniciarPantalla', 'detenerPantalla',
            'Grabación de pantalla iniciada.', 'Error al iniciar la grabación de pantalla.');
    } else {
        console.error('dispositivoId no está definido.');
    }
});

document.getElementById('detenerPantalla').addEventListener('click', function () {
    if (dispositivoId) {
        manejarGrabacion(`http://localhost:8000/api/dispositivos/${dispositivoId}/detener-grabacion-pantalla/`, 
            'alertPantalla', 'spinnerPantalla', 'detenerPantalla', 'iniciarPantalla',
            'Grabación de pantalla detenida.', 'Error al detener la grabación de pantalla.');
    } else {
        console.error('dispositivoId no está definido.');
    }
});

// Función para obtener las grabaciones
async function obtenerGrabaciones(url, listaId) {
    if (!dispositivoId) {
        console.error('Error: dispositivoId no está definido.');
        return;
    }

    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + token
            }
        });
        if (response.ok) {
            const data = await response.json();
            const lista = document.getElementById(listaId);
            lista.innerHTML = '';  // Limpiar la lista

            data.forEach((grabacion, index) => {
                const item = document.createElement('li');
                item.classList.add('list-group-item');
                item.innerHTML = `
                    <span>${index + 1}. ${grabacion.fecha} - ${grabacion.hora}</span>
                    <audio controls>
                        <source src="${grabacion.ruta_archivo}" type="audio/mpeg">
                        Tu navegador no soporta el elemento de audio.
                    </audio>
                `;
                lista.appendChild(item);
            });
        } else {
            console.error('Error al obtener las grabaciones: ', response.status);
        }
    } catch (error) {
        console.error('Error al obtener las grabaciones:', error);
    }
}

// Obtener las grabaciones al cargar la página
document.addEventListener('DOMContentLoaded', function () {
    if (dispositivoId) {
        obtenerGrabaciones(`http://localhost:8000/api/dispositivos/${dispositivoId}/grabaciones/llamadas/`, 'listaGrabacionesLlamadas');
        obtenerGrabaciones(`http://localhost:8000/api/dispositivos/${dispositivoId}/grabaciones/pantalla/`, 'listaGrabacionesPantalla');
    } else {
        console.error('dispositivoId no está definido.');
    }
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
});

// Cerrar sesión
document.getElementById('cerrar-sesion').addEventListener('click', function () {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
<<<<<<< HEAD
<<<<<<< HEAD
    localStorage.removeItem('dispositivoSeleccionado');
    window.location.href = '/login';  // Redirigir al login después de cerrar sesión
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

    localStorage.removeItem('dispositivoSeleccionado');
    window.location.href = '/login';  // Redirigir al login después de cerrar sesión

    window.location.href = '/login'; // Redirigir al login después de cerrar sesión
 afc917d1d14c3730d6946130d053056968a08dc6
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
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
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======

>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
});

// Redirigir a la página de registro de eventos
document.getElementById('registro-link').addEventListener('click', function () {
<<<<<<< HEAD
<<<<<<< HEAD
=======
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    if (dispositivoId) {
        window.location.href = `/dispositivo/${dispositivoId}/reg_event`;
    } else {
        alert('No se ha seleccionado un dispositivo.');
        window.location.href = '/mis_dispositivos';  // Redirigir si no hay ID
    }
});
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29


});


});

});
 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
<<<<<<< HEAD
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
