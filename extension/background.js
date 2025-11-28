const AGENT_URL = 'http://localhost:8765';
const AGENT_TOKEN = 'ixj17zpiaFvy9CAccxYyM27LNpDnzMg__M0vLCiqRLI';

async function checkAgentHealth() {
    try {
        const response = await fetch(`${AGENT_URL}/health`, {
            method: 'GET',
            timeout: 2000
        });
        const data = await response.json();
        return data.status === 'ok';
    } catch (error) {
        return false;
    }
}

async function printDocument(documentUrl) {
    try {
        const response = await fetch(`${AGENT_URL}/print`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${AGENT_TOKEN}`
            },
            body: JSON.stringify({
                document_url: documentUrl
            }),
            timeout: 30000
        });
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error al imprimir:', error);
        return {
            status: 'error',
            message: 'El agente de impresión no está disponible'
        };
    }
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'print') {
        printDocument(request.url).then(result => {
            sendResponse(result);
        });
        return true;
    }
    
    if (request.action === 'checkAgent') {
        checkAgentHealth().then(isAvailable => {
            sendResponse({ available: isAvailable });
        });
        return true;
    }
});

checkAgentHealth().then(isAvailable => {
    console.log('Agente disponible:', isAvailable);
});

