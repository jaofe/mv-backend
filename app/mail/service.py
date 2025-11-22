import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Union
from app.config import settings


def send_email(
    recipient: Union[str, List[str]],
    subject: str,
    message: str,
    html: bool = False
) -> bool:
    try:
        # Validate configuration
        if not settings.MAIL_USERNAME or not settings.MAIL_PASSWORD:
            raise ValueError("Email credentials not configured in environment variables")
        
        if not settings.MAIL_FROM:
            raise ValueError("MAIL_FROM not configured in environment variables")
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = settings.MAIL_FROM
        msg['Subject'] = subject
        
        # Handle single recipient or list
        if isinstance(recipient, list):
            msg['To'] = ', '.join(recipient)
            recipients = recipient
        else:
            msg['To'] = recipient
            recipients = [recipient]
        
        # Attach message body
        if html:
            msg.attach(MIMEText(message, 'html'))
        else:
            msg.attach(MIMEText(message, 'plain'))
        
        # Connect to SMTP server and send
        with smtplib.SMTP(settings.MAIL_SERVER, settings.MAIL_PORT) as server:
            if settings.MAIL_STARTTLS:
                server.starttls()
            
            server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
            server.sendmail(settings.MAIL_FROM, recipients, msg.as_string())
        
        return True
        
    except Exception as e:
        # Log the error (you can integrate with a logging system)
        print(f"Failed to send email: {str(e)}")
        raise


def send_html_email(recipient: Union[str, List[str]], subject: str, html_content: str) -> bool:
    return send_email(recipient, subject, html_content, html=True)
