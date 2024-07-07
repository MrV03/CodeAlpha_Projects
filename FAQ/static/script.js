document.getElementById('user-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the default form submission
        sendMessage();
    }
});

async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');

    if (userInput.trim() === '') {
        alert('Please enter a message.');
        return;
    }

    const userMessage = document.createElement('div');
    userMessage.className = 'chat-message user';
    userMessage.innerText = userInput;
    chatBox.appendChild(userMessage);

    try {
        const response = await fetch('/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput }),
        });

        const result = await response.json();
        const botMessage = document.createElement('div');
        botMessage.className = 'chat-message bot';
        botMessage.innerText = result.response;
        chatBox.appendChild(botMessage);
    } catch (error) {
        const botMessage = document.createElement('div');
        botMessage.className = 'chat-message bot';
        botMessage.innerText = 'There was an error processing your request.';
        chatBox.appendChild(botMessage);
    }

    document.getElementById('user-input').value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
}
