import pytest

@pytest.mark.regression
@pytest.mark.xfail(reason="Swagger Petstore demo API does not consistently persist updates")
def test_put_pet_updates_existing_pet(session, base_url, pet_payload):
    """
    Test the PUT /pet endpoint to update an existing pet in the Swagger Petstore API.

    This test performs the following steps:
    1. Create a new pet using POST /pet with the given payload.
    2. Verify that the pet was successfully created by checking the GET /pet/{pet_id} response.
    3. Update the pet's name and status using PUT /pet.
    4. Verify that the update was successful by retrieving the pet again via GET /pet/{pet_id}.

    The test is marked as xfail because the Swagger Petstore demo API does not consistently persist updates.

    Assertions:
    - POST /pet returns status code 200.
    - GET /pet/{pet_id} after creation returns status code 200 or 404 and contains the correct name.
    - PUT /pet returns status code 200.
    - GET /pet/{pet_id} after update returns the updated name, status, and the same pet ID.
    
    Parameters:
    - session: requests.Session object used to make HTTP requests.
    - base_url: Base URL of the Swagger Petstore API.
    - pet_payload: Dictionary containing the initial pet data for creation.
    """
    
    # Step 1: Create a pet
    create_response = session.post(f"{base_url}/pet", json=pet_payload)
    assert create_response.status_code == 200
    created_pet = create_response.json()
    pet_id = created_pet["id"]


    # Step 2: Verify creation
    get_response = session.get(f"{base_url}/pet/{pet_id}", timeout=5)
    new_pet_json = get_response.json()
    assert get_response.status_code == 200 or get_response.status_code == 404
    assert new_pet_json["name"] == pet_payload["name"]
    

    # Step 3: Update
    new_pet_json["name"] = "Better_Doggo"
    new_pet_json["status"] = "sold"
    put_response = session.put(f"{base_url}/pet", json=new_pet_json)
    assert put_response.status_code == 200


    # Step 4: Verify update
    get_updated = session.get(f"{base_url}/pet/{pet_id}")
    updated_pet = get_updated.json()
    assert updated_pet["name"] == "Better_Doggo"
    assert updated_pet["status"] == "sold"
    assert updated_pet["id"] == pet_id

