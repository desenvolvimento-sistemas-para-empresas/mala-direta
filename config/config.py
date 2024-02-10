import os
from dotenv import load_dotenv

class EmailConfig:
    def __init__(self):
        load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
        self.smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
        self.email_port = int(os.environ.get('EMAIL_PORT', 587))
        self.sender_email = os.environ.get('SENDER_EMAIL')
        self.sender_email_pass = os.environ.get('SENDER_EMAIL_PASS')

# Você pode adicionar mais configurações aqui conforme necessário