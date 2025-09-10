import pytest

@pytest.mark.integration
def test_pet_creation_and_update(session, base_url, pet_payload):
    """
    Integration test for creating and updating a pet in the Swagger Petstore API.

    Note:
    - The live Swagger Petstore API does not persist updates reliably.
    - Therefore, after updating a pet via PUT, the GET request may not reflect changes.
    - This test asserts the response from the PUT request instead of the subsequent GET.

    Steps:
    1. Modify the base pet payload and create a new pet via POST /pet.
    2. Assert that the created pet has the expected name and status.
    3. Update the pet's name and status via PUT /pet.
    4. Assert that the PUT response contains the updated values.
    """

    # Modify payload for creation
    new_pet_payload = pet_payload.copy()
    new_pet_payload["name"] = "German_Sheppard"
    new_pet_payload["status"] = "sold"

    # Create the pet
    create_pet_response = session.post(f"{base_url}/pet", json=new_pet_payload)
    assert create_pet_response.status_code == 200

    pet = create_pet_response.json()
    assert pet["name"] == "German_Sheppard"
    assert pet["status"] == "sold"

    pet_id = pet["id"]

    # Update the pet
    updated_pet_payload = new_pet_payload.copy()
    updated_pet_payload["name"] = "Retriever"
    updated_pet_payload["status"] = "available"
    updated_pet_payload["id"] = pet_id

    update_pet_response = session.put(f"{base_url}/pet", json=updated_pet_payload)
    assert update_pet_response.status_code == 200

    updated_pet = update_pet_response.json()
    # Assert the updated values directly from the PUT response
    assert updated_pet["name"] == "Retriever"
    assert updated_pet["status"] == "available"
