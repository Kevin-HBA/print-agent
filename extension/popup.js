const AGENT_URL = 'http://localhost:8765';

async function checkAgent() {
    const statusDiv = document.getElementById('status');
    const refreshBtn = document.getElementById('refresh');
    
    statusDiv.textContent = 'Verificando...';
    statusDiv.className = 'status';
    refreshBtn.disabled = true;
    
    try {
        const response = await fetch(`${AGENT_URL}/health`);
        const data = await response.json();
        
        if (data.status === 'ok') {
            statusDiv.textContent = '✅ Agente disponible';
            statusDiv.className = 'status available';
        } else {
            throw new Error('Agente no responde correctamente');
        }
    } catch (error) {
        statusDiv.textContent = '❌ Agente no disponible';
        statusDiv.className = 'status unavailable';
    } finally {
        refreshBtn.disabled = false;
    }
}

document.getElementById('refresh').addEventListener('click', checkAgent);
checkAgent();

