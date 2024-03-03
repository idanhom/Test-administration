import requests

def add_note_to_candidate(candidate_id, api_key, note_content, admin_id):
    url = "https://api.teamtailor.com/v1/notes"
    headers = {
        "Authorization": f"Token token={api_key}",
        "X-Api-Version": "20210218",
        "Content-Type": "application/vnd.api+json",
    }
    payload = {
        "data": {
            "type": "notes",
            "attributes": {"note": note_content},
            "relationships": {
                "candidate": {"data": {"id": candidate_id}},
                "user": {"data": {"id": admin_id}},
            },
        }
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error POST request add note: {e}")
