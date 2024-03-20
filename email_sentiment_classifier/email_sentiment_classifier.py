import os
import imaplib
import email
from email.header import decode_header

def filter_and_save_emails(username, password, word):
    # IMAP settings
    imap_server = 'imap.gmail.com'
    imap_port = 993
    save_dir = word.lower()  # Create directory named after the word to filter
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(username, password)
    mail.select("inbox")

    # Search for emails containing the specified word
    result, data = mail.search(None, '(TEXT "{}")'.format(word))
    if result == 'OK':
        for num in data[0].split():
            # Fetch the email
            result, data = mail.fetch(num, "(RFC822)")
            if result == 'OK':
                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)
                subject = decode_header(email_message["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                print("Email Subject:", subject)
                print("From:", email_message["From"])
                print("To:", email_message["To"])

                # Save email to the directory named after the word to filter
                file_name = os.path.join(save_dir, f"{subject}.eml")
                with open(file_name, 'wb') as f:
                    f.write(raw_email)
                print("Email saved to:", file_name)
                print("="*50)

    # Logout from the server
    mail.logout()

# Example usage
if __name__ == "__main__":
    # Input your email credentials
    username = "your_email@gmail.com"
    password = "your_password"
    # Input the word to filter emails
    word_to_filter = "important"

    filter_and_save_emails(username, password, word_to_filter)
