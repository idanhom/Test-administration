# Import the necessary modules
import configparser
import json
import os
import requests
import sys
import time
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import win32com.client as win32
from time import sleep

# Load user data from the config file.
# Config file should include API keys, usernames, passwords, and email information
def load_config():
    config = configparser.ConfigParser()
    # Provide the path to the config.ini file here
    config.read(r"<PATH TO CONFIG.INI FILE>")
    return config

# Get candidate information by parsing cand.id and api-key
# This function makes a GET request to the teamtailor API and retrieves candidate information
def get_candidate_info(candidate_id, api_key):
    try:
        url = f"https://api.teamtailor.com/v1/candidates/{candidate_id}"
        headers = {
            "Authorization": f"Token token=<API TOKEN>", # Replace <API TOKEN> with the actual API key
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

# Manually enter candidate information
def get_candidate_info_manual():
    first_name = input("Enter the candidate's first name: ")
    last_name = input("Enter the candidate's last name: ")
    email = input("Enter the candidate's email: ")
    return first_name, last_name, email

# Function to add a note to a candidate's profile on teamtailor using POST request
def add_note_to_candidate(candidate_id, api_key, note_content):
    url = f"https://api.teamtailor.com/v1/notes"
    int_candidate_id = int(candidate_id)
    headers = {
        "Authorization": f"Token token=<API TOKEN>", # Replace <API TOKEN> with the actual API key
        "X-Api-Version": "20210218",
        "Content-Type": "application/vnd.api+json",
    }
    # Replace <ID-ADMIN-ACCOUNT-TEAMTAILOR> with actual ID
    payload = json.dumps(
        {
            "data": {
                "type": "notes",
                "attributes": {"note": note_content},
                "relationships": {
                    "candidate": {"data": {"id": int_candidate_id}},
                    "user": {"data": {"id": <ID-ADMIN-ACCOUNT-TEAMTAILOR>}},
                },
            }
        }
    )

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
    except requests.exceptions.HTTPError as e:
        print("Error POST request add note: {}", e)

# This function updates an excel file with candidate information
def update_excel_file(excel_file_path, first_name, last_name, email):
    try:
        wb = load_workbook(excel_file_path)
    except FileNotFoundError:
        print(f"Error: Excel file not found at {excel_file_path}")
        sys.exit(1)
    ws = wb.active # Get active sheet
    ws.append([first_name, last_name, email]) # Append new row with candidate data
    wb.save(excel_file_path) # Save the changes

# This function will send an email using Outlook with the candidate information
def send_email(email_subject, email_body, to_email, config):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.Subject = email_subject
    mail.Body = email_body
    mail.To = to_email

    # Here the code is setup to use an SMTP server to send the email
    # You will need to update the server address, username and password in the config.ini file
    # Alternatively, if you're using Outlook, you can just call mail.Send() without needing the server details

    try:
        mail.Send()
    except Exception as e:
        print(f"Error sending email: {e}")
        sys.exit(1)

def main():
    config = load_config() # Load configuration data

    # Get candidate ID from user
    candidate_id = input("Please enter candidate id: ")
    
    # Load the API key from the config file
    api_key = config.get('DEFAULT', 'API_KEY')
    
    # Get candidate info from API or manual input based on config
    if config.get('DEFAULT', 'GET_INFO_FROM_API').lower() == 'true':
        first_name, last_name, email = get_candidate_info(candidate_id, api_key)
    else:
        first_name, last_name, email = get_candidate_info_manual()

    # Add note to candidate's profile on teamtailor
    note_content = input("Please enter the note content to be added: ")
    add_note_to_candidate(candidate_id, api_key, note_content)

    # Update excel file with candidate data
    excel_file_path = config.get('DEFAULT', 'EXCEL_FILE_PATH')
    update_excel_file(excel_file_path, first_name, last_name, email)

    # Send email with candidate info
    email_subject = "New candidate information"
    email_body = f"Candidate {first_name} {last_name} has been added to the system."
    to_email = config.get('DEFAULT', 'TO_EMAIL')
    send_email(email_subject, email_body, to_email, config)

if __name__ == "__main__":
    main()