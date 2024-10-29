<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
const dispositivoId = localStorage.getItem('dispositivoSeleccionado');

if (!dispositivoId) {
    alert('No se ha seleccionado un dispositivo.');
    window.location.href = '/mis_dispositivos';  // Redirigir si no hay ID
}

// Función para hacer las solicitudes de datos del dispositivo
async function fetchData(url) {
    const token = localStorage.getItem('access_token');
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
<<<<<<< HEAD

=======
=======
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
const token = localStorage.getItem('access_token');

// Función reutilizable para hacer peticiones con fetch
async function fetchData(url) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: { 
<<<<<<< HEAD
 afc917d1d14c3730d6946130d053056968a08dc6
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        return await response.json();
    } catch (error) {
        console.error('Error en la solicitud:', error);
        throw new Error('Error al obtener los datos');
    }
}

<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
// Función para cargar las llamadas
async function obtenerLlamadas() {
    try {
        const data = await fetchData(`http://localhost:8000/api/dispositivos/${dispositivoId}/llamadas/`);
        const listaLlamadas = document.getElementById('lista-llamadas');
        listaLlamadas.innerHTML = '';  // Limpiar antes de actualizar
<<<<<<< HEAD

=======
=======
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
// Funciones para obtener los datos de la API

async function obtenerLlamadas() {
    try {
        const data = await fetchData('http://localhost:8000/api/dispositivos/1/llamadas/');
        const listaLlamadas = document.getElementById('lista-llamadas');
        const loadingMessage = document.getElementById('loading-llamadas');
        listaLlamadas.innerHTML = '';
        loadingMessage.style.display = 'none';
<<<<<<< HEAD
 afc917d1d14c3730d6946130d053056968a08dc6
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
        data.forEach((llamada, index) => {
            listaLlamadas.innerHTML += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${llamada.numero}</td>
                    <td>${llamada.duracion} segundos</td>
                    <td>${llamada.fecha}</td>
                    <td>${llamada.hora}</td>
<<<<<<< HEAD

                    <td>${llamada.tipo}</td>  

 afc917d1d14c3730d6946130d053056968a08dc6
=======
<<<<<<< HEAD
                    <td>${llamada.tipo}</td>  
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
                </tr>
            `;
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-llamadas').textContent = 'Error al cargar las llamadas.';
    }
}

<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470

// Función para cargar los mensajes
async function obtenerMensajes() {
    try {
        const data = await fetchData(`http://localhost:8000/api/dispositivos/${dispositivoId}/mensajes/`);
        const listaMensajes = document.getElementById('lista-mensajes');
        listaMensajes.innerHTML = '';  // Limpiar antes de actualizar
<<<<<<< HEAD

=======
=======
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
async function obtenerMensajes() {
    try {
        const data = await fetchData('http://localhost:8000/api/dispositivos/1/mensajes/');
        const listaMensajes = document.getElementById('lista-mensajes');
        const loadingMessage = document.getElementById('loading-mensajes');
        listaMensajes.innerHTML = '';
        loadingMessage.style.display = 'none';
<<<<<<< HEAD
 afc917d1d14c3730d6946130d053056968a08dc6
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
        data.forEach((mensaje, index) => {
            listaMensajes.innerHTML += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${mensaje.numero}</td>
                    <td>${mensaje.contenido}</td>
                    <td>${mensaje.fecha}</td>
                    <td>${mensaje.hora}</td>
<<<<<<< HEAD

                    <td>${mensaje.tipo}</td>  

 afc917d1d14c3730d6946130d053056968a08dc6
=======
<<<<<<< HEAD
                    <td>${mensaje.tipo}</td>  
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
                </tr>
            `;
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-mensajes').textContent = 'Error al cargar los mensajes.';
    }
}

<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470

// Función para cargar los contactos
async function obtenerContactos() {
    try {
        const data = await fetchData(`http://localhost:8000/api/dispositivos/${dispositivoId}/contactos/`);
        const listaContactos = document.getElementById('lista-contactos');
        listaContactos.innerHTML = '';  // Limpiar antes de actualizar
        data.forEach(contacto => {
            listaContactos.innerHTML += `
                <li class="list-group-item">${contacto.nombre} - ${contacto.numero}</li>
            `;
<<<<<<< HEAD

=======
=======
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
async function obtenerContactos() {
    try {
        const data = await fetchData('http://localhost:8000/api/dispositivos/1/contactos/');
        const listaContactos = document.getElementById('lista-contactos');
        const loadingMessage = document.getElementById('loading-contactos');
        listaContactos.innerHTML = '';
        loadingMessage.style.display = 'none';
        data.forEach(contacto => {
            listaContactos.innerHTML += `<li class="list-group-item">${contacto.nombre} - ${contacto.numero}</li>`;
<<<<<<< HEAD
 afc917d1d14c3730d6946130d053056968a08dc6
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-contactos').textContent = 'Error al cargar los contactos.';
    }
}

<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
// Función para cargar las fotos
async function obtenerFotos() {
    try {
        const data = await fetchData(`http://localhost:8000/api/dispositivos/${dispositivoId}/fotos/`);
        const galeriaFotos = document.getElementById('galeria-fotos');
        galeriaFotos.innerHTML = '';  // Limpiar antes de actualizar
        data.forEach(foto => {
            galeriaFotos.innerHTML += `
                <img src="${foto.ruta_foto}" alt="Foto">
            `;
<<<<<<< HEAD

=======
=======
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
async function obtenerFotos() {
    try {
        const data = await fetchData('http://localhost:8000/api/dispositivos/1/fotos/');
        const galeriaFotos = document.getElementById('galeria-fotos');
        const loadingMessage = document.getElementById('loading-fotos');
        galeriaFotos.innerHTML = '';
        loadingMessage.style.display = 'none';
        data.forEach(foto => {
            galeriaFotos.innerHTML += `<img src="${foto.ruta_foto}" alt="Foto">`;
<<<<<<< HEAD
 afc917d1d14c3730d6946130d053056968a08dc6
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-fotos').textContent = 'Error al cargar las fotos.';
    }
}

<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
// Función para cargar los videos
async function obtenerVideos() {
    try {
        const data = await fetchData(`http://localhost:8000/api/dispositivos/${dispositivoId}/videos/`);
        const galeriaVideos = document.getElementById('galeria-videos');
        galeriaVideos.innerHTML = '';  // Limpiar antes de actualizar
        data.forEach(video => {
            galeriaVideos.innerHTML += `
                <video src="${video.ruta_video}" controls></video>
            `;
<<<<<<< HEAD

=======
=======
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
async function obtenerVideos() {
    try {
        const data = await fetchData('http://localhost:8000/api/dispositivos/1/videos/');
        const galeriaVideos = document.getElementById('galeria-videos');
        const loadingMessage = document.getElementById('loading-videos');
        galeriaVideos.innerHTML = '';
        loadingMessage.style.display = 'none';
        data.forEach(video => {
            galeriaVideos.innerHTML += `<video src="${video.ruta_video}" controls></video>`;
<<<<<<< HEAD
 afc917d1d14c3730d6946130d053056968a08dc6
=======
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-videos').textContent = 'Error al cargar los videos.';
    }
}

<<<<<<< HEAD

// Llamar a las funciones correspondientes dependiendo de la pestaña activa

// Sondeo para cada sección, que se actualiza cada 10 segundos
 afc917d1d14c3730d6946130d053056968a08dc6
=======
<<<<<<< HEAD
// Llamar a las funciones correspondientes dependiendo de la pestaña activa
=======
// Sondeo para cada sección, que se actualiza cada 10 segundos
>>>>>>> afc917d1d14c3730d6946130d053056968a08dc6
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
setInterval(() => {
    if (document.getElementById('llamadas-tab').classList.contains('active')) {
        obtenerLlamadas();
    } else if (document.getElementById('mensajes-tab').classList.contains('active')) {
        obtenerMensajes();
    } else if (document.getElementById('contactos-tab').classList.contains('active')) {
        obtenerContactos();
    } else if (document.getElementById('fotos-tab').classList.contains('active')) {
        obtenerFotos();
    } else if (document.getElementById('videos-tab').classList.contains('active')) {
        obtenerVideos();
    }
<<<<<<< HEAD

=======
<<<<<<< HEAD
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
}, 10000);  // Actualizar cada 10 segundos

// Función para redirigir a la página de registro de eventos
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

}, 10000);  // Actualiza cada 10 segundos







 a8d19f143da4dcdf7a22fd08e935b212cf57580a
 b4cb2bf817590ea6000bce461d5a50d14c9ce9b7
 b0b9b03a14308048bdfe4ae811ef3107c4b0cc5e
 afc917d1d14c3730d6946130d053056968a08dc6
=======
=======
}, 10000);  // Actualiza cada 10 segundos
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
