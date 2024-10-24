const token = localStorage.getItem('access_token');
const dispositivoId = localStorage.getItem('dispositivoSeleccionado');

// Verificar si el usuario está autenticado y si hay un dispositivo seleccionado
function verificarSesion() {
    if (!token || !dispositivoId) {
        alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
        window.location.href = '/login';  // Redirigir si no hay token o dispositivo
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29




const token = localStorage.getItem('access_token');  // Usar 'access_token' si ese es el nombre correcto


const token = localStorage.getItem('access_token');  // Usar 'access_token' si ese es el nombre correcto

 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
const token = localStorage.getItem('access_token');

// Verificar si el usuario está autenticado al cargar la página
function verificarSesion() {
    if (!token) {
        alert('Tu sesión ha expirado o no has iniciado sesión.');
        window.location.href = '/login'; // Redirigir a la página de inicio de sesión si no hay token
 afc917d1d14c3730d6946130d053056968a08dc6
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
    }
}

// Llamar a la verificación de sesión
verificarSesion();

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29



 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6

<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
// Manejar clic en el botón de exportación
document.getElementById('exportarBtn').addEventListener('click', async function () {
    const formato = document.getElementById('formatoExportacion').value;
    const tipoDatos = document.getElementById('tipoDatos').value;

    iniciarProgreso();  // Inicializa la barra de progreso

    try {
<<<<<<< HEAD
<<<<<<< HEAD
        const response = await fetch( `/api/dispositivos/${dispositivoId}/exportar/${formato}/?tipo=${tipoDatos}`, {
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

        const response = await fetch( `/api/dispositivos/${dispositivoId}/exportar/${formato}/?tipo=${tipoDatos}`, {

        const response = await fetch(`/api/dispositivos/1/exportar/?formato=${formato}&tipo=${tipoDatos}`, {
 afc917d1d14c3730d6946130d053056968a08dc6
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + token,
            }
        });

        if (!response.ok) {
            throw new Error('Error en la exportación');
        }

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const link = document.getElementById('downloadLink');
        link.href = url;
        link.download = `${tipoDatos}_exportado.${formato}`;
        link.style.display = 'inline';
        alert('Exportación completada con éxito');
    } catch (error) {
        console.error('Error al exportar:', error);
        alert('Error al exportar los datos o de conexión.');
    }
});

// Función para inicializar la barra de progreso
function iniciarProgreso() {
    const progressBar = document.getElementById('barraProgreso');
    progressBar.style.width = '0%';
    progressBar.textContent = '0%';

    let progreso = 0;
    const intervalo = setInterval(() => {
        progreso += 10;
        progressBar.style.width = `${progreso}%`;
        progressBar.textContent = `${progreso}%`;

        if (progreso >= 100) {
            clearInterval(intervalo);
        }
    }, 300);  // Incremento del progreso cada 300ms
}

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29







 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6

<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
// Cerrar sesión
document.getElementById('cerrar-sesion').addEventListener('click', function () {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    alert('Has cerrado sesión.');
<<<<<<< HEAD
<<<<<<< HEAD
    window.location.href = '/login';  // Redirigir al login después de cerrar sesión
});

=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

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
<<<<<<< HEAD
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29


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


<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29

 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
<<<<<<< HEAD
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
=======
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 7abb30cb4dbdac2fb6787b7118a19056b324ee29
