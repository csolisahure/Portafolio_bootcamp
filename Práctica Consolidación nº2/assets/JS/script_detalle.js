document.addEventListener('DOMContentLoaded', () => {
    const digimonList = document.getElementById('digimon-list');
    const digimonDetails = document.getElementById('digimon-details');

    // Función para mostrar los detalles del Digimon seleccionado
    function showDigimonDetails(digimon) {
        digimonDetails.innerHTML = `
            <h3>${digimon.name}</h3>
            <img src="${digimon.img}" alt="${digimon.name}">
            <p>Nivel: ${digimon.level}</p>
        `;
    }

    // Función para mostrar la lista de Digimon
    function showDigimonList(digimons) {
        digimonList.innerHTML = '';
        digimons.forEach(digimon => {
            const listItem = document.createElement('li');
            listItem.textContent = digimon.name;
            listItem.addEventListener('click', () => showDigimonDetails(digimon));
            digimonList.appendChild(listItem);
        });
    }

    // Obtener datos de la API de Digimon
    fetch('https://digimon-api.vercel.app/api/digimon')
        .then(response => response.json())
        .then(data => {
            const digimons = data.map(digimon => ({
                name: digimon.name,
                img: digimon.img,
                level: digimon.level
            }));
            showDigimonList(digimons);
        })
        .catch(error => console.error('Error al obtener datos:', error));
});
