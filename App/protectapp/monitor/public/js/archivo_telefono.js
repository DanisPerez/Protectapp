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

// Función para cargar las llamadas
async function obtenerLlamadas() {
    try {
        const data = await fetchData(`http://localhost:8000/api/dispositivos/${dispositivoId}/llamadas/`);
        const listaLlamadas = document.getElementById('lista-llamadas');
        listaLlamadas.innerHTML = '';  // Limpiar antes de actualizar
        data.forEach((llamada, index) => {
            listaLlamadas.innerHTML += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${llamada.numero}</td>
                    <td>${llamada.duracion} segundos</td>
                    <td>${llamada.fecha}</td>
                    <td>${llamada.hora}</td>
                    <td>${llamada.tipo}</td>  
                </tr>
            `;
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-llamadas').textContent = 'Error al cargar las llamadas.';
    }
}


// Función para cargar los mensajes
async function obtenerMensajes() {
    try {
        const data = await fetchData(`http://localhost:8000/api/dispositivos/${dispositivoId}/mensajes/`);
        const listaMensajes = document.getElementById('lista-mensajes');
        listaMensajes.innerHTML = '';  // Limpiar antes de actualizar
        data.forEach((mensaje, index) => {
            listaMensajes.innerHTML += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${mensaje.numero}</td>
                    <td>${mensaje.contenido}</td>
                    <td>${mensaje.fecha}</td>
                    <td>${mensaje.hora}</td>
                    <td>${mensaje.tipo}</td>  
                </tr>
            `;
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-mensajes').textContent = 'Error al cargar los mensajes.';
    }
}


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
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-contactos').textContent = 'Error al cargar los contactos.';
    }
}

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
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-fotos').textContent = 'Error al cargar las fotos.';
    }
}

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
        });
    } catch (error) {
        console.error(error);
        document.getElementById('loading-videos').textContent = 'Error al cargar los videos.';
    }
}

// Llamar a las funciones correspondientes dependiendo de la pestaña activa
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
