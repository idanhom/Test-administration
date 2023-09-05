
## README for Candidate Management Script

---

### Overview

This script is designed to assist in the management of candidate data. It automates the processes of fetching candidate information, updating an Excel sheet, adding notes to a candidate's profile on Teamtailor, and sending an email notification via Outlook.

### Prerequisites

- Python 3.x
- Required Python libraries: 
    - `configparser`
    - `json`
    - `os`
    - `requests`
    - `sys`
    - `time`
    - `openpyxl`
    - `selenium`
    - `win32com.client`

### Configuration

Before running the script, you need to set up a configuration file (`config.ini`) which will include:

- API keys
- Usernames
- Passwords
- Email information
- Excel file path
- Any other necessary configuration details

Sample `config.ini` format:
```
[DEFAULT]
API_KEY = your_api_key_here
GET_INFO_FROM_API = true_or_false
EXCEL_FILE_PATH = path_to_your_excel_file
TO_EMAIL = recipient_email_here
...
```

**Note:** Ensure that the configuration file is kept confidential and is not shared or uploaded to public repositories.

### Usage

1. Update the path to the `config.ini` file in the `load_config` function within the script.
2. Run the script using:
    ```
    python script_name.py
    ```
3. Follow the on-screen prompts to enter the required information.

### Features

1. **Load Configuration Data:** Fetches all necessary details like API keys, email information, and other configurations from a `.ini` file.
2. **Retrieve Candidate Information:** Can fetch candidate details either manually or using the Teamtailor API.
3. **Add Notes:** Adds a note for the candidate on Teamtailor.
4. **Update Excel:** Updates an Excel sheet with the fetched candidate details.
5. **Send Email:** Sends an email notification through Outlook with the candidate's information.

### Error Handling

In the event of an error (e.g., API call failure, file not found), the script will display an error message and exit. Ensure to check any displayed error messages for troubleshooting.

### Future Considerations

1. Enhance error handling for a more user-friendly experience.
2. Consider moving all hardcoded values, like API version, to the configuration file.
3. Expand functionalities based on evolving requirements.

### Contribution & Support

For any bugs, feature requests, or queries, please open an issue or reach out to the script maintainer at [maintainer_email_here].

---

