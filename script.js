document.addEventListener('DOMContentLoaded', () => {
    const seedTextInput = document.getElementById('seedText');
    const suggestionList = document.getElementById('suggestionList');
    const fullSentenceDisplay = document.getElementById('fullSentence');

    let debounceTimer;
    const DEBOUNCE_DELAY = 400;

    const fetchPredictions = async (text) => {
        if (!text.trim()) {
            suggestionList.innerHTML = '<p>Start typing to get predictions...</p>';
            return;
        }

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text })
            });

            const data = await response.json();
            const keys = Object.keys(data);

            if (keys.length === 0) {
                suggestionList.innerHTML = '<p>No suggestions found.</p>';
                return;
            }

            suggestionList.innerHTML = ''; 

           
            keys.forEach((word, index) => {
                const div = document.createElement('div');
                div.className = 'suggestion-item';
                if (index === 0) div.classList.add('top-suggestion');

                div.innerHTML = `
                    <span class="word">${word}</span>
                    <span class="prob">${data[word]}</span>
                `;

                
                div.addEventListener('click', () => {
                    let currentText = seedTextInput.value.trim();
                    if (!currentText.endsWith(' ')) currentText += ' ';
                    const newText = currentText + word + ' ';
                    seedTextInput.value = newText;

                    
                    fullSentenceDisplay.textContent = newText;

                    
                    fetchPredictions(newText);
                    seedTextInput.focus();
                });

                suggestionList.appendChild(div);
            });

        } catch (err) {
            console.error('Prediction error:', err);
            suggestionList.innerHTML = '<p style="color:red;">Error loading suggestions.</p>';
        }
    };

    seedTextInput.addEventListener('input', () => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            fetchPredictions(seedTextInput.value);
        }, DEBOUNCE_DELAY);
    });
});
