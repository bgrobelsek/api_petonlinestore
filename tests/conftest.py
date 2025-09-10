import pytest
import requests
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """
    Fixture: base_url (session scope)
    Provides the base URL for the Petstore API.
    Used as the root endpoint for all requests.
    """
    return "https://petstore.swagger.io/v2"


@pytest.fixture(scope="session")
def api_key():
    """
    Fixture: api_key (session scope)
    Retrieves the API key for authentication.
    Reads from the PETSTORE_API_KEY environment variable.
    Raises a RuntimeError if the key is not set.
    """
    key = os.getenv("PETSTORE_API_KEY")
    if not key:
        raise RuntimeError(
            "PETSTORE_API_KEY is not set. Please add it to your .env file "
            "or set it as a GitHub Actions secret."
        )
    return key


@pytest.fixture(scope="session")
def session(api_key):
    """
    Fixture: session (session scope)
    Creates a persistent requests.Session with default headers:
      - Content-Type: application/json
      - api_key: <value from environment variable>

    All API requests in tests will use this session to ensure consistent
    authentication and headers.
    """
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json",
        "api_key": api_key,
    })
    return s


@pytest.fixture(scope="function")
def pet_payload():
    """
    Fixture: pet_payload (function scope)
    Provides a default JSON payload representing a valid Pet object.
    Tests can modify this payload for various scenarios.
    """
    return {
        "category": {"id": 0, "name": "string"},
        "name": "Good_Doggo",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }
