document.addEventListener('DOMContentLoaded', function() {
    const characterElement = document.querySelector('#character');
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
    
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error!`);
        }
        return response.json();
      })
      .then(data => {
        characterElement.textContent = data.name;
      })
      .catch(error => {
        console.error('Fetch error:', error);
      });
  });