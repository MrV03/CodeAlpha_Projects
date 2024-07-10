async function translateText() {
    const text = document.getElementById('text').value;
    const target_language = document.getElementById('target_language').value;

    if (!text.trim() || !target_language.trim()) {
        alert('Please enter text and target language');
        return;
    }

    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text, target_language }),
        });

        if (!response.ok) {
            throw new Error('Failed to fetch translation');
        }

        const result = await response.json();
        document.getElementById('translation_result').innerText = result.translation;
    } catch (error) {
        console.error('Error fetching translation:', error);
        alert('Failed to fetch translation. Please try again.');
    }
}
