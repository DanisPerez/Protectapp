const token = localStorage.getItem('access_token');
const eventosLista = document.getElementById('eventos-lista');
const errorMessage = document.getElementById('error-message');

// Función reutilizable para hacer peticiones con fetch 
async function fetchData(url) {
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

        return await response.json(); // Retorna los datos directamente
    } catch (error) {
        console.error('Error en la solicitud:', error);
        throw error;
    }
}


// Función para obtener eventos de un dispositivo específico
async function obtenerEventos() {
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    if (!dispositivoId) {
        alert('No se ha seleccionado un dispositivo.');
        window.location.href = '/mis_dispositivos';  // Redirigir si no hay ID
        return;
    }

    try {
        const eventos = await fetchData(`http://localhost:8000/api/dispositivos/${dispositivoId}/eventos/`);

// Función para obtener eventos
async function obtenerEventos() {
    try {
        const eventos = await fetchData('http://localhost:8000/api/dispositivos/1/eventos/');
 afc917d1d14c3730d6946130d053056968a08dc6
        eventosLista.innerHTML = '';  // Limpiar la tabla antes de actualizar

        eventos.forEach(evento => {
            const row = `
                <tr>
                    <td>${evento.id}</td>

                    <td>${evento.tipo_evento}</td> <!-- Ajustado a 'tipo_evento' -->

                    <td>${evento.tipo}</td>
 afc917d1d14c3730d6946130d053056968a08dc6
                    <td>${evento.fecha}</td>
                    <td>${evento.hora}</td>
                    <td><button class="btn btn-info" onclick="verDetalles(${evento.id})">Ver Detalles</button></td>
                </tr>
            `;
            eventosLista.insertAdjacentHTML('beforeend', row);
        });
    } catch (error) {
        errorMessage.style.display = 'block';  // Mostrar mensaje de error
    }
}

// Función para ver detalles de un evento
async function verDetalles(eventoId) {
    try {
        const evento = await fetchData(`http://localhost:8000/api/eventos/${eventoId}/`);
        const modalDetalles = document.getElementById('modal-detalles-evento');
        modalDetalles.innerHTML = `

            <p><strong>Tipo de Evento:</strong> ${evento.tipo_evento}</p>

            <p><strong>Tipo de Evento:</strong> ${evento.tipo}</p>
 afc917d1d14c3730d6946130d053056968a08dc6
            <p><strong>Fecha:</strong> ${evento.fecha}</p>
            <p><strong>Hora:</strong> ${evento.hora}</p>
            <p><strong>Detalles:</strong> ${evento.detalles}</p>
        `;

        // Mostrar el modal con los detalles
        $('#eventoModal').modal('show');
    } catch (error) {
        alert('Error al cargar los detalles del evento.');
    }
}


// Redirigir a la página de registro de eventos solo si no estás ya en ella
document.getElementById('registro-link').addEventListener('click', function () {
    const dispositivoId = localStorage.getItem('dispositivoSeleccionado');
    const currentUrl = window.location.href;
    const registroUrl = `/dispositivo/${dispositivoId}/reg_event`;

    if (currentUrl !== registroUrl) {
        window.location.href = registroUrl;
    } else {
        alert('Ya estás en la página de Registro de Eventos.');
    }
});


 afc917d1d14c3730d6946130d053056968a08dc6
// Sondeo para actualizar los eventos cada 10 segundos
setInterval(obtenerEventos, 10000);

// Llamar a la función una vez al cargar la página
document.addEventListener('DOMContentLoaded', obtenerEventos);