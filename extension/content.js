(function() {
    'use strict';
    
    let agentAvailable = false;
    
    function checkAgent() {
        chrome.runtime.sendMessage({ action: 'checkAgent' }, (response) => {
            agentAvailable = response && response.available;
            if (agentAvailable) {
                console.log('Agente de impresión local disponible');
            }
        });
    }
    
    function printWithAgent(url) {
        if (!agentAvailable) {
            return false;
        }
        
        chrome.runtime.sendMessage(
            { action: 'print', url: url },
            (response) => {
                if (response && response.status === 'ok') {
                    console.log('Documento enviado a la impresora automáticamente');
                    showNotification('Documento enviado a la impresora', 'success');
                } else {
                    return false;
                }
            }
        );
        return true;
    }
    
    function showNotification(message, type) {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#4CAF50' : '#2196F3'};
            color: white;
            padding: 15px 20px;
            border-radius: 5px;
            z-index: 10000;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            font-family: Arial, sans-serif;
            font-size: 14px;
        `;
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
    
    function isPrintableDocument(url) {
        if (!url) return false;
        const urlLower = url.toLowerCase();
        return urlLower.endsWith('.pdf') || 
               urlLower.endsWith('.html') || 
               urlLower.endsWith('.htm') ||
               urlLower.includes('/pdf') ||
               urlLower.includes('/imprimir') ||
               urlLower.includes('/print') ||
               urlLower.includes('content-type=application/pdf');
    }
    
    document.addEventListener('click', function(e) {
        let target = e.target;
        while (target && target.tagName !== 'A' && target.tagName !== 'BUTTON') {
            target = target.parentElement;
        }
        
        if (!target) return;
        let url = null;
        if (target.tagName === 'A') {
            url = target.href;
        } else if (target.tagName === 'BUTTON') {
            url = target.getAttribute('data-url') || 
                  target.getAttribute('data-href') ||
                  target.getAttribute('onclick')?.match(/https?:\/\/[^\s'"]+/)?.[0];
        }
        
        if (url && isPrintableDocument(url)) {
            const isDownload = target.hasAttribute('download') || 
                              target.getAttribute('target') === '_blank' ||
                              e.ctrlKey || e.metaKey;
            
            if (!isDownload && agentAvailable) {
                e.preventDefault();
                e.stopPropagation();
                printWithAgent(url);
                return false;
            }
        }
    }, true);
    
    const originalPrint = window.print;
    window.print = function() {
        if (window.location.href.toLowerCase().endsWith('.pdf')) {
            if (agentAvailable && printWithAgent(window.location.href)) {
                return;
            }
        }
        originalPrint.call(window);
    };
    
    const originalOpen = window.open;
    window.open = function(url, target, features) {
        if (url && isPrintableDocument(url) && agentAvailable) {
            if (printWithAgent(url)) {
                return null;
            }
        }
        return originalOpen.call(window, url, target, features);
    };
    
    const originalFetch = window.fetch;
    window.fetch = function(...args) {
        const url = args[0];
        const result = originalFetch.apply(this, args);
        if (typeof url === 'string' && isPrintableDocument(url) && agentAvailable) {
            result.then(response => {
                const contentType = response.headers.get('content-type') || '';
                if (contentType.includes('pdf') || contentType.includes('application/pdf')) {
                    response.clone().blob().then(blob => {
                        const blobUrl = URL.createObjectURL(blob);
                        if (printWithAgent(blobUrl)) {
                            setTimeout(() => URL.revokeObjectURL(blobUrl), 1000);
                        }
                    }).catch(() => {});
                }
                return response;
            }).catch(() => {});
        }
        return result;
    };
    
    const originalXHROpen = XMLHttpRequest.prototype.open;
    const originalXHRSend = XMLHttpRequest.prototype.send;
    
    XMLHttpRequest.prototype.open = function(method, url, ...rest) {
        this._url = url;
        return originalXHROpen.apply(this, [method, url, ...rest]);
    };
    
    XMLHttpRequest.prototype.send = function(...args) {
        if (this._url && isPrintableDocument(this._url) && agentAvailable) {
            this.addEventListener('load', function() {
                const contentType = this.getResponseHeader('content-type') || '';
                if (contentType.includes('pdf') || contentType.includes('application/pdf')) {
                    const blob = new Blob([this.response], { type: 'application/pdf' });
                    const blobUrl = URL.createObjectURL(blob);
                    if (printWithAgent(blobUrl)) {
                        setTimeout(() => URL.revokeObjectURL(blobUrl), 1000);
                    }
                }
            });
        }
        return originalXHRSend.apply(this, args);
    };
    
    document.addEventListener('click', function(e) {
        const target = e.target;
        if (target.tagName === 'A' && target.hasAttribute('download')) {
            const href = target.getAttribute('href');
            if (href && isPrintableDocument(href) && agentAvailable) {
                e.preventDefault();
                e.stopPropagation();
                if (printWithAgent(href)) {
                    return false;
                }
            }
        }
    }, true);
    
    const originalCreateElement = document.createElement;
    document.createElement = function(tagName, ...args) {
        const element = originalCreateElement.call(this, tagName, ...args);
        if (tagName.toLowerCase() === 'a' && agentAvailable) {
            const originalSetAttribute = element.setAttribute;
            element.setAttribute = function(name, value) {
                originalSetAttribute.call(this, name, value);
                if (name === 'href' && isPrintableDocument(value) && this.hasAttribute('download')) {
                    this.addEventListener('click', function(e) {
                        e.preventDefault();
                        e.stopPropagation();
                        printWithAgent(value);
                        return false;
                    }, true);
                }
            };
        }
        return element;
    };
    
    window.addEventListener('print-agent-print', function(e) {
        if (e.detail && e.detail.url) {
            printWithAgent(e.detail.url);
        }
    });
    
    window.printAgent = {
        print: function(url) {
            printWithAgent(url);
        },
        check: function() {
            return new Promise((resolve) => {
                chrome.runtime.sendMessage({ action: 'checkAgent' }, (response) => {
                    resolve(response && response.available);
                });
            });
        }
    };
    
    checkAgent();
    setInterval(checkAgent, 30000);
    
    console.log('Agente de Impresión Local: Extensión activa');
})();

