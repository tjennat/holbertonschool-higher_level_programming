document.addEventListener('DOMContentLoaded', function() {
    const Hello = document.querySelector('#hello');
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
  
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('HTTP error');
        }
        return response.json()
      })
      .then(data => {
        Hello.textContent = data.hello;
      })
      .catch(error => {
        console.error('Fetch error:', error);
      });
  });