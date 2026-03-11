import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "modbox.noreply@gmail.com"
SMTP_PASSWORD = "phgd whjv vgrh ecaw"

TEMPLATE_PATH = Path(__file__).parent / "templates"

def load_template(template_name):
    path = TEMPLATE_PATH / template_name
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def render_template(template, data):
    for key, value in data.items():
        template = template.replace("{{" + key + "}}", str(value))
    return template

def send_email(to_email, template, data, subject="MODBOX Notification"):
    html_template = load_template(template)
    html_content = render_template(html_template, data)

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = SMTP_USERNAME
    message["To"] = to_email

    part = MIMEText(html_content, "html")
    message.attach(part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(SMTP_USERNAME, to_email, message.as_string())
    server.quit()
