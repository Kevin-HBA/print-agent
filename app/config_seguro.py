import os
from typing import List, Optional


class ConfigSeguro:
    PORT: int = int(os.getenv("PRINT_AGENT_PORT", "8765"))
    HOST: str = "127.0.0.1"
    PRINT_TOKEN: str = os.getenv("PRINT_AGENT_TOKEN", "ixj17zpiaFvy9CAccxYyM27LNpDnzMg__M0vLCiqRLI")
    ALLOWED_DOMAINS: List[str] = []
    RATE_LIMIT_PER_MINUTE: int = int(os.getenv("PRINT_AGENT_RATE_LIMIT", "10"))
    TEMP_DIR: str = os.path.join(os.path.expanduser("~"), ".print_agent_temp")
    DOWNLOAD_TIMEOUT: int = 30
    MAX_FILE_SIZE_MB: int = 50
    
    @classmethod
    def ensure_temp_dir(cls) -> None:
        os.makedirs(cls.TEMP_DIR, exist_ok=True)
    
    @classmethod
    def validate_url(cls, url: str) -> bool:
        if not cls.ALLOWED_DOMAINS:
            return True
        
        from urllib.parse import urlparse
        try:
            domain = urlparse(url).netloc
            domain = domain.split(':')[0]
            return domain in cls.ALLOWED_DOMAINS
        except Exception:
            return False
    
    @classmethod
    def validate_token(cls, token: str) -> bool:
        return token == cls.PRINT_TOKEN

