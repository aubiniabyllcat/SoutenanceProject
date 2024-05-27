import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .interfaces.email_service_interface import EmailServiceInterface

class EmailService(EmailServiceInterface):
    def __init__(self, smtp_server, smtp_port, smtp_username, smtp_password, from_email):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.from_email = from_email
        

    async def send_password_reset_email(self, email: str, reset_link: str):
        subject = "Password Reset Request"
        body = f"Please click the following link to reset your password: {reset_link}"

        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.from_email, email, msg.as_string())
            server.quit()
            return {"message": "Password reset email sent successfully"}
        except Exception as e:
            print(f"Failed to send email: {e}")
            raise Exception("Failed to send email")
