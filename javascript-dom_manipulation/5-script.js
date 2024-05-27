document.addEventListener('DOMContentLoaded', function() {
    const update = document.querySelector('#update_header');
    const header = document.querySelector('header');

    update.addEventListener('click', function() {
        header.textContent = 'New Header!!!'
    });
});