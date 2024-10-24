const token = localStorage.getItem('access_token');
<<<<<<< HEAD
=======

>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
const dispositivoId = localStorage.getItem('dispositivoSeleccionado');

// Verificar si el usuario está autenticado y si hay un dispositivo seleccionado
function verificarSesion() {
    if (!token || !dispositivoId) {
        alert('Tu sesión ha expirado o no has seleccionado un dispositivo.');
        window.location.href = '/login';  // Redirigir si no hay token o dispositivo
<<<<<<< HEAD
=======








 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
// Verificar si el usuario está autenticado al cargar la página
function verificarSesion() {
    if (!token) {
        alert('Tu sesión ha expirado o no has iniciado sesión.');
        window.location.href = '/login'; // Redirigir a la página de inicio de sesión si no hay token
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
    }
}

// Llamar a la verificación de sesión
verificarSesion();

<<<<<<< HEAD
=======




 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
// Función para mostrar el spinner mientras se procesa
function mostrarSpinner(mostrar = true) {
    const spinner = document.getElementById('spinner');
    spinner.style.display = mostrar ? 'inline-block' : 'none';
}

// Función genérica para manejar capturas (pantalla/foto) con fetch
async function manejarCaptura(url, tipoCaptura) {
    try {
        mostrarSpinner(true);
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            }
        });

        mostrarSpinner(false);

        if (response.ok) {
            const data = await response.json();
            if (tipoCaptura === 'pantalla') {
                mostrarCaptura(data.ruta_captura);
            } else if (tipoCaptura === 'foto') {
                mostrarFoto(data.ruta_foto);
            }
            alert(`¡${tipoCaptura.charAt(0).toUpperCase() + tipoCaptura.slice(1)} realizada con éxito!`);
        } else {
<<<<<<< HEAD
            const errorData = await response.json();
            alert(`Error al realizar la ${tipoCaptura}: ${errorData.error || 'Desconocido'}`);
=======
            alert(`Error al realizar la ${tipoCaptura}.`);
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
        }
    } catch (error) {
        mostrarSpinner(false);
        console.error(`Error al realizar la ${tipoCaptura}:`, error);
        alert('Error de conexión.');
    }
}

// Capturar pantalla
document.getElementById('capturaPantallaBtn').addEventListener('click', function () {
<<<<<<< HEAD
    manejarCaptura(`http://localhost:8000/api/dispositivos/${dispositivoId}/capturas-pantalla/`, 'pantalla');
=======

    manejarCaptura(`http://localhost:8000/api/dispositivos/${dispositivoId}/capturas-pantalla/`, 'pantalla');

    manejarCaptura('http://localhost:8000/api/dispositivos/1/capturas-pantalla/', 'pantalla');
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
});

// Tomar foto
document.getElementById('tomarFotoBtn').addEventListener('click', function () {
<<<<<<< HEAD
    manejarCaptura(`http://localhost:8000/api/dispositivos/${dispositivoId}/fotos/`, 'foto');
=======

    manejarCaptura(`http://localhost:8000/api/dispositivos/${dispositivoId}/fotos/`, 'foto');

    manejarCaptura('http://localhost:8000/api/dispositivos/1/fotos/', 'foto');
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
});

// Mostrar la captura de pantalla en la sección de vista previa
function mostrarCaptura(ruta) {
    const previewSection = document.getElementById('preview-section');
    const imgElement = document.createElement('img');
    imgElement.src = ruta;
<<<<<<< HEAD
    imgElement.style.margin = '10px';  // Añadir espacio entre imágenes
    imgElement.style.maxWidth = '320px';  // Limitar el tamaño de la imagen
    previewSection.appendChild(imgElement);  // Añadir sin limpiar la vista previa anterior
=======

    previewSection.innerHTML = '';  // Limpiar la vista previa anterior

    previewSection.innerHTML = ''; // Limpiar la vista previa anterior
 afc917d1d14c3730d6946130d053056968a08dc6
    previewSection.appendChild(imgElement);
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
}

// Mostrar la foto tomada en la sección de vista previa
function mostrarFoto(ruta) {
    const previewSection = document.getElementById('preview-section');
    const imgElement = document.createElement('img');
    imgElement.src = ruta;
<<<<<<< HEAD
    imgElement.style.margin = '10px';  // Añadir espacio entre imágenes
    imgElement.style.maxWidth = '320px';  // Limitar el tamaño de la imagen
    previewSection.appendChild(imgElement);  // Añadir sin limpiar la vista previa anterior
=======

    previewSection.innerHTML = '';  // Limpiar la vista previa anterior
    previewSection.appendChild(imgElement);
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
}

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
=======

    previewSection.innerHTML = ''; // Limpiar la vista previa anterior
    previewSection.appendChild(imgElement);
}
 afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 140297cf9450a6de7652b1265e43fff63f4f0b04
