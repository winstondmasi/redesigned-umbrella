document.getElementById('article-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const url = document.getElementById('article-url').value;
    fetch('/api/analyze_article/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url }),
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => console.error('Error:', error));
});

function displayResults(data) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = `<p>Analysis: ${data.analysis}</p>`;
}
