import pytest


@pytest.mark.regression
@pytest.mark.xfail(reason="Swagger Petstore demo API does not persist created pets reliably")
def test_get_existing_pet_returns_200(session, base_url, pet_payload):
    """
    Test GET /pet/{petId} for retrieving an existing pet.

    Steps:
    1. Create a new pet with a specific name using POST /pet.
    2. Verify creation by asserting the status code is 200.
    3. Retrieve the created pet using GET /pet/{pet_id}.
    4. Assert that the response status code is 200.
    5. Validate the JSON structure, including top-level keys: id, category, name, photoUrls, tags, status.
    6. Verify that the retrieved values match the created pet's data (id, name, status).

    Parameters:
    - session: requests.Session object used to make HTTP requests.
    - base_url: Base URL of the Swagger Petstore API.
    - pet_payload: Dictionary containing the initial pet data for creation.
    """
    # Step 1: Create a pet
    pet_payload["name"] = "Retriever"
    create_response = session.post(f"{base_url}/pet", json=pet_payload)
    assert create_response.status_code == 200
    created_pet = create_response.json()
    pet_id = created_pet["id"]

    # Step 2: Retrieve the created pet
    get_response = session.get(f"{base_url}/pet/{pet_id}")
    assert get_response.status_code == 200
    response_data = get_response.json()

    # Assert top-level keys
    assert 'id' in response_data
    assert 'category' in response_data
    assert 'name' in response_data
    assert 'photoUrls' in response_data
    assert 'tags' in response_data
    assert 'status' in response_data

    # Assert values match what we created
    assert response_data['id'] == pet_id
    assert response_data['name'] == "Retriever"
    assert response_data['status'] == pet_payload['status']


@pytest.mark.parametrize("invalid_id, expected_status", [
    pytest.param(999999999, 404, marks=pytest.mark.xfail(reason="Swagger Petstore demo API may return 200 for nonexistent IDs")),
    (-1, 404),          # negative ID
])
def test_get_nonexistent_pet_returns_404(session, base_url, invalid_id, expected_status):
    """
    Test GET /pet/{petId} for retrieving a nonexistent pet.

    Steps:
    1. Attempt to retrieve a pet using an invalid or nonexistent pet ID.
    2. Assert that the response status code matches the expected status (typically 404).
       - Some cases are marked xfail due to API inconsistencies.

    Parameters:
    - session: requests.Session object used to make HTTP requests.
    - base_url: Base URL of the Swagger Petstore API.
    - invalid_id: Pet ID that does not exist in the system.
    - expected_status: The expected HTTP status code for this test case.
    """
    get_response = session.get(f"{base_url}/pet/{invalid_id}")
    assert get_response.status_code == expected_status
