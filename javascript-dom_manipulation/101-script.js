document.addEventListener('DOMContentLoaded', () => {
    const btnTranslate = document.getElementById('btn_translate');
    const languageCodeInput = document.getElementById('language_code');
    const helloDiv = document.getElementById('hello');

    btnTranslate.addEventListener('click', () => {
        const languageCode = languageCodeInput.value;
        if (languageCode) {
            fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    helloDiv.textContent = data.hello;
                })
                .catch(error => {
                    console.error('Error:', error);
                    helloDiv.textContent = 'Error fetching translation';
                });
        } else {
            helloDiv.textContent = 'Please select a language code';
        }
    });
});