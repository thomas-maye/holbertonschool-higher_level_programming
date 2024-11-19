document.addEventListener('DOMContentLoaded', function() {
    const myList = document.querySelector('.my_list');

    document.getElementById('add_item').addEventListener('click', function() {
        const li = document.createElement('li');
        li.textContent = 'Item';
        myList.appendChild(li);
    });

    document.getElementById('remove_item').addEventListener('click', function() {
        if (myList.lastElementChild) {
            myList.removeChild(myList.lastElementChild);
        }
    });

    document.getElementById('clear_list').addEventListener('click', function() {
        myList.innerHTML = '';
    });
});