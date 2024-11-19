document.addEventListener('DOMContentLoaded', () => {
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(response => response.json())
        .then(data => {
            const movies = data.results;
            const listMovies = document.getElementById('list_movies');
            movies.forEach(movie => {
                const ul = document.createElement('li');
                ul.textContent = movie.title;
                listMovies.appendChild(ul);
            });
        })
        .catch(error => console.error('Error:', error));
});