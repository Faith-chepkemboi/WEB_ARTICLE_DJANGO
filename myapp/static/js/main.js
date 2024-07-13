// main.js

document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.querySelector('form[action="{% url 'search_articles' %}"]');
    const searchInput = searchForm.querySelector('input[name="q"]');
    const searchResults = document.getElementById('search-results');

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const query = searchInput.value;

        fetch(`/search/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                searchResults.innerHTML = '';
                data.articles.forEach(article => {
                    const articleElement = document.createElement('li');
                    articleElement.textContent = article.title;
                    searchResults.appendChild(articleElement);
                });
            });
    });
});
