document.addEventListener('DOMContentLoaded', function() {
    const movies = document.querySelector('#list_movies');
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('HTTP error');
        }
        return response.json();
      })
      .then(data => {
        data.results.forEach(movie => {
          const listItem = document.createElement('li');
          listItem.textContent = movie.title;
          movies.appendChild(listItem);
        });
      })
      .catch(error => {
        console.error('Fetch error:', error);
      });
  });