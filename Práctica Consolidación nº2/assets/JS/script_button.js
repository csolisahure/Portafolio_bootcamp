// Busqueda información vía NAVBAR
document.addEventListener("DOMContentLoaded", function () {
    const searchButton = document.getElementById("searchButton");
    const searchInput = document.getElementById("searchInput");
    const contenidoTabla = document.getElementById("contenido_tabla");

    function realizarBusqueda() {
        const filtro = searchInput.value.toLowerCase();

        // Obtener todas las filas de la tabla
        const filas = contenidoTabla.getElementsByTagName("tr");

        // Recorrer las filas y mostrar/ocultar según la búsqueda
        for (const fila of filas) {
            const nombreDigimon = fila.getElementsByTagName("td")[0].innerText.toLowerCase();

            if (nombreDigimon.includes(filtro)) {
                fila.style.display = "";
            } else {
                fila.style.display = "none";
            }
        }
    }

    searchButton.addEventListener("click", realizarBusqueda);
    searchInput.addEventListener("input", realizarBusqueda);
});