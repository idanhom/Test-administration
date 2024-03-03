from config_loader import load_config
from candidate_info import get_candidate_info, get_candidate_info_manual
from teamtailor_integration import add_note_to_candidate
from file_operations import update_excel_file
from email_service import send_email

def main():
    config = load_config()
    candidate_id = input("Please enter candidate id: ")
    api_key = config.get('DEFAULT', 'API_KEY')

    if config.get('DEFAULT', 'GET_INFO_FROM_API').lower() == 'true':
        first_name, last_name, email = get_candidate_info(candidate_id, api_key)
    else:
        first_name, last_name, email = get_candidate_info_manual()

    note_content = input("Please enter the note content to be added: ")
    add_note_to_candidate(candidate_id, api_key, note_content, config.get('DEFAULT', 'ADMIN_ID'))

    excel_file_path = config.get('DEFAULT', 'EXCEL_FILE_PATH')
    update_excel_file(excel_file_path, first_name, last_name, email)

    email_subject = "New candidate information"
    email_body = f"Candidate {first_name} {last_name} has been added to the system."
    to_email = config.get('DEFAULT', 'TO_EMAIL')
    send_email(email_subject, email_body, to_email)

if __name__ == "__main__":
    main()
