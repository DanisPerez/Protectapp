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

// Función para obtener eventos
async function obtenerEventos() {
    try {
        const eventos = await fetchData('http://localhost:8000/api/dispositivos/1/eventos/');
        eventosLista.innerHTML = '';  // Limpiar la tabla antes de actualizar

        eventos.forEach(evento => {
            const row = `
                <tr>
                    <td>${evento.id}</td>
                    <td>${evento.tipo}</td>
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
            <p><strong>Tipo de Evento:</strong> ${evento.tipo}</p>
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

// Sondeo para actualizar los eventos cada 10 segundos
setInterval(obtenerEventos, 10000);

// Llamar a la función una vez al cargar la página
<<<<<<< HEAD
document.addEventListener('DOMContentLoaded', obtenerEventos);
=======
document.addEventListener('DOMContentLoaded', obtenerEventos);
>>>>>>> 6ed65ad7429d47b5a2bed51bfa4f1a8fd6c2a470
