document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.querySelector("#toggle_header");
    const header = document.querySelector('header');

    toggle.addEventListener('click', function() {
        header.classList.toggle('red');
        header.classList.toggle('green');
    })
});
