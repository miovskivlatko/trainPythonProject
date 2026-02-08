import pytest
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/test.log'),
        logging.StreamHandler()
    ]
)

@pytest.fixture
def api_logger():
    return logging.getLogger(__name__)

@pytest.fixture
def base_url():
    return os.getenv('BASE_URL', 'https://petstore.swagger.io/v2')
