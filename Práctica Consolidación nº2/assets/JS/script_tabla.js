
// TODOS LOS DIGIMON
fetch('https://digimon-api.vercel.app/api/digimon/')
    .then(response => response.json())
    .then(resp => {
        crearTabla(resp)
    });

// Función para mostrar tabla de Digimon
function crearTabla(resp) {
    for (let datoTemporal of resp) {
        contenido_tabla.innerHTML +=
            `
     <td> <a href="vacio.html">${datoTemporal.name} </a></td>
     <td> <img src="${datoTemporal.img}" width="30%" heigth="30%"> </td>
     <td>${datoTemporal.level}</td>
 `
    }
}; 
