import pytest


@pytest.mark.regression
def test_post_pet_valid_name_returns_200(session, base_url, pet_payload):
    """
    Test creating a pet with a valid name using POST /pet.

    Steps:
    1. Set the pet name to "Good_Doggo".
    2. Send a POST request to create the pet.
    3. Verify that the response status code is 200.
    4. Validate the structure and types of the returned JSON, including:
       - Top-level keys: id, category, name, photoUrls, tags, status.
       - Category is a dict with id and name.
       - photoUrls is a list of strings.
       - tags is a list of dicts with id and name.
    5. Validate the values of 'name' and 'status'.

    Parameters:
    - session: requests.Session object used to make HTTP requests.
    - base_url: Base URL of the Swagger Petstore API.
    - pet_payload: Dictionary containing the initial pet data for creation.
    """
    
    pet_payload["name"] = "Good_Doggo"
    response = session.post(f"{base_url}/pet", json=pet_payload)
    response_data = response.json()
    
    assert response.status_code == 200
    
    # Assert top-level keys exist
    assert 'id' in response_data
    assert 'category' in response_data
    assert 'name' in response_data
    assert 'photoUrls' in response_data
    assert 'tags' in response_data
    assert 'status' in response_data

    # Assert values
    assert response_data['name'] == "Good_Doggo"
    assert response_data['status'] == 'available'

    # Assert category structure
    category = response_data['category']
    assert isinstance(category, dict)
    assert 'id' in category
    assert 'name' in category

    # Assert photoUrls is a list
    assert isinstance(response_data['photoUrls'], list)
    assert all(isinstance(url, str) for url in response_data['photoUrls'])

    # Assert tags structure
    tags = response_data['tags']
    assert isinstance(tags, list)
    for tag in tags:
        assert isinstance(tag, dict)
        assert 'id' in tag
        assert 'name' in tag


@pytest.mark.regression  
@pytest.mark.parametrize("field, value, expected_status", [
    ("category", [], 500),
    ("name", "", 200),
    ("name", True, 200),
    ("name", False, 200),
    ("photoUrls", 1, 500),
    ("photoUrls", "", 500),
    pytest.param("status", "not_a_status", 400, marks=pytest.mark.xfail(reason="Petstore API does not validate status")),
    pytest.param("id", -123456, 400, marks=pytest.mark.xfail(reason="Petstore API accepts negative IDs")),
])
def test_post_pet_invalid_inputs(session, base_url, pet_payload, field, value, expected_status):
    """
    Test POST /pet with invalid or edge-case inputs using parameterization.

    Steps:
    1. Modify the pet_payload with the given field and value.
    2. Send a POST request to create the pet.
    3. Assert that the response status code matches the expected status.
       - Some cases are marked xfail due to API inconsistencies (e.g., invalid status or negative IDs).

    Parameters:
    - session: requests.Session object used to make HTTP requests.
    - base_url: Base URL of the Swagger Petstore API.
    - pet_payload: Dictionary containing the initial pet data for creation.
    - field: The specific field in pet_payload to modify.
    - value: The value to assign to the field for testing.
    - expected_status: The expected HTTP status code for this test case.
    """
    pet_payload[field] = value
    response = session.post(f"{base_url}/pet", json=pet_payload)
    assert response.status_code == expected_status
