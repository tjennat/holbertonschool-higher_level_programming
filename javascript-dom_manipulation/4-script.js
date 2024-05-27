document.addEventListener("DOMContentLoaded", function () {
    const add = document.querySelector("#add_item");
    const myList = document.querySelector(".my_list");

    add.addEventListener('click', function() {
        const newListItem = document.createElement('li');
        newListItem.textContent = 'Item';
        myList.appendChild(newListItem);
    });
});