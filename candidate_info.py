import sys
import requests

def get_candidate_info(candidate_id, api_key):
    try:
        url = f"https://api.teamtailor.com/v1/candidates/{candidate_id}"
        headers = {
            "Authorization": f"Token token={api_key}",
            "X-Api-Version": "20210218",
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        first_name = data["data"]["attributes"]["first-name"].split()[0]
        last_name = data["data"]["attributes"]["last-name"].split()[-1]
        email = data["data"]["attributes"]["email"]
        return first_name, last_name, email
    except Exception as e:
        print(f"Error getting candidate info: {e}")
        sys.exit(1)

def get_candidate_info_manual():
    first_name = input("Enter the candidate's first name: ")
    last_name = input("Enter the candidate's last name: ")
    email = input("Enter the candidate's email: ")
    return first_name, last_name, email
