// Function to send a message to the QNN
async function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const message = userInput.value.trim();

    if (message) {
        // Add user message to chat
        chatMessages.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
        userInput.value = '';

        // Simulate QNN processing
        chatMessages.innerHTML += `<p><em>QNN is processing...</em></p>`;
        
        try {
            // Send request to QNN backend
            const response = await fetch('/qnn_process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();

            // Remove processing message
            chatMessages.removeChild(chatMessages.lastElementChild);

            // Add QNN response to chat
            chatMessages.innerHTML += `<p><strong>QNN:</strong> ${data.response}</p>`;
        } catch (error) {
            console.error('Error:', error);
            chatMessages.innerHTML += `<p><strong>Error:</strong> Unable to process request. Please try again.</p>`;
        }

        // Scroll to bottom of chat
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

// Event listener for Enter key in input field
document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});

// Function to initialize the chat
function initChat() {
    const chatMessages = document.getElementById('chat-messages');
    chatMessages.innerHTML = `<p><strong>QNN:</strong> Welcome to the Quantum Neural Network. How can I assist you today?</p>`;
}

// Initialize chat when page loads
window.onload = initChat;