// Obtener el token de autenticación
const token = localStorage.getItem('token');

// Función para actualizar el contenido de la sección activa
function updateSectionData(section) {
    let url = '';
    
    if (section === 'registro') {
        url = '/api/dispositivos/1/registro';
    } else if (section === 'ubicacion') {
        url = '/api/dispositivos/1/ubicaciones';
    }
    // Añadir más secciones según sea necesario

    if (url) {
        fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Aquí actualizas la sección activa con los datos
            console.log(`Datos de ${section} actualizados`, data);
            // Actualiza el DOM con los datos recibidos
        })
        .catch(error => console.error('Error al actualizar los datos:', error));
    }
}

$(document).ready(function() {
    // Manejar el cambio de contenido al hacer clic en los enlaces laterales
    $('.sidebar a').on('click', function(e) {
        e.preventDefault();
        // Quitar la clase 'active' de todos los enlaces
        $('.sidebar a').removeClass('active');
        // Agregar la clase 'active' al enlace actual
        $(this).addClass('active');
        
        // Ocultar todo el contenido
        $('.tab-pane').removeClass('active');
        // Mostrar el contenido correspondiente
        const target = $(this).attr('href');
        $(target).addClass('active');

        // Actualizar datos inmediatamente al hacer clic
        const activeSection = $(target).attr('id');
        updateSectionData(activeSection);
    });

    // Sondeo en tiempo real cada 10 segundos
    setInterval(() => {
        const activeSection = $('.tab-pane.active').attr('id');
        updateSectionData(activeSection);
    }, 10000);
});
