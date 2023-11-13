const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

// URL de la página web que deseas analizar
const url = 'https://www.facebook.com/search/top?q=claudia%20sheinbaum';

// Realizar una solicitud HTTP a la página web
axios.get(url)
  .then((response) => {
    // Cargar el contenido HTML de la página en Cheerio
    const $ = cheerio.load(response.data);

    // Seleccionar los elementos que contienen los enlaces (puedes ajustar esto según la estructura de la página)
    const links = $('a');

    // Array para almacenar los URL
    const urls = [];

    // Iterar sobre los elementos seleccionados y obtener los URL
    links.each((index, element) => {
      const href = $(element).attr('href');
      if (href) {
        urls.push(href);
      }
    });

    // Guardar los URL en un archivo
    fs.writeFileSync('urls.txt', urls.join('\n'));

    console.log('URLs extraídos y guardados en urls.txt');
  })
  .catch((error) => {
    console.error('Error al obtener la página:', error.message);
  });
