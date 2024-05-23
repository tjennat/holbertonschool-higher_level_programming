document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector("#red_header");
    header.addEventListener('click', function() {
        document.querySelector('header').classList.add('red');
    });
});