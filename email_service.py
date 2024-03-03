import win32com.client as win32

def send_email(email_subject, email_body, to_email):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.Subject = email_subject
    mail.Body = email_body
    mail.To = to_email
    try:
        mail.Send()
    except Exception as e:
        print(f"Error sending email: {e}")
