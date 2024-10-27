let apiKey = '';

async function connectAPI() {
    const apiKeyInput = document.getElementById('api-key-input');
    apiKey = apiKeyInput.value.trim();

    if (apiKey) {
        try {
            const response = await fetch('/connect_api', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ api_key: apiKey }),
            });

            const data = await response.json();

            if (data.success) {
                document.getElementById('api-key-container').style.display = 'none';
                document.getElementById('chat-container').style.display = 'block';
                initChat();
            } else {
                alert(`Failed to connect: ${data.error || 'Unknown error'}`);
            }
        } catch (error) {
            console.error('Error:', error);
            alert(`An error occurred while connecting: ${error.message}`);
        }
    } else {
        alert('Please enter your OpenAI API key.');
    }
}

async function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const message = userInput.value.trim();

    if (message) {
        chatMessages.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
        userInput.value = '';

        chatMessages.innerHTML += `<p><em>QNN is processing...</em></p>`;
        
        try {
            const response = await fetch('/qnn_process', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message, api_key: apiKey }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            chatMessages.removeChild(chatMessages.lastElementChild);
            
            if (data.response.includes('Generated and Optimized Code:')) {
                const codeResponse = parseCodeResponse(data.response);
                chatMessages.innerHTML += `
                    <div class="ai-response">
                        <h3>QNN:</h3>
                        <h4>Generated and Optimized Code:</h4>
                        <pre><code>${codeResponse.code}</code></pre>
                        <h4>Execution Output:</h4>
                        <pre>${codeResponse.output}</pre>
                    </div>`;
            } else {
                chatMessages.innerHTML += `<div class="ai-response"><h3>QNN:</h3>${formatAIResponse(data.response)}</div>`;
            }
        } catch (error) {
            console.error('Error:', error);
            chatMessages.innerHTML += `<p><strong>Error:</strong> ${error.message}</p>`;
        }

        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

function parseCodeResponse(response) {
    const codeMatch = response.match(/```python\n([\s\S]*?)```/);
    const outputMatch = response.match(/Execution Output:\n([\s\S]*)/);
    
    return {
        code: codeMatch ? codeMatch[1] : 'No code found',
        output: outputMatch ? outputMatch[1] : 'No output found'
    };
}

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});

function initChat() {
    const chatMessages = document.getElementById('chat-messages');
    chatMessages.innerHTML = `<div class="ai-response"><h3>QNN:</h3><p>Welcome to the Quantum Neural Network. How can I assist you today?</p></div>`;
}

function formatAIResponse(response) {
    // Split the response into paragraphs
    const paragraphs = response.split('\n\n');
    
    // Format each paragraph
    const formattedParagraphs = paragraphs.map(paragraph => {
        // Check if the paragraph is a heading (starts with #)
        if (paragraph.startsWith('#')) {
            const level = paragraph.match(/^#+/)[0].length;
            const text = paragraph.replace(/^#+\s*/, '');
            return `<h${level}>${text}</h${level}>`;
        }
        // Otherwise, wrap it in a paragraph tag
        return `<p>${paragraph}</p>`;
    });
    
    // Join the formatted paragraphs and return
    return formattedParagraphs.join('');
}

// IDE Execution Code
document.getElementById('execute-button').addEventListener('click', () => {
    const code = document.getElementById('code-input').value;

    fetch('/execute_code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: code, api_key: apiKey }),
    })
    .then(response => response.json())
    .then(data => {
        let output = '';

        if (data.results) {
            output += `Results:\n${data.results}\n\n`;
        }
        if (data.logs) {
            output += `Stdout:\n${data.logs.stdout}\n\n`;
            output += `Stderr:\n${data.logs.stderr}\n\n`;
        }
        if (data.error) {
            output += `Error:\n${data.error}\n\n`;
        }
        document.getElementById('code-output').innerText = output;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while executing the code.');
    });
});