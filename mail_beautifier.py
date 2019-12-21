import email
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import json

def prepare_attachment(filepath : str):
    # Extracting filename.
    filename = filepath.split('/')[-1]
    print(filename)
    # Reading Attachment File.
    with open(filepath, "rb") as attachment_file:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment_file.read())
    # Encoding Attachment to ASCII.
    encoders.encode_base64(part)
    # Adding required Key-Value pairs.
    part.add_header('Content-Disposition', 'attachment', filename=filename)
    part.add_header('Content-Transfer-Encoding', 'base64')
    return part

def prepare_draft(config : json, body : str, attachment_path : str):

    message = MIMEMultipart()
    message['To']      = config['receiver']
    message['From']    = config['sender']
    message['Subject'] = config['subject']
    message['Bcc']     = config['bcc']
    message.attach(MIMEText(body, "plain"))
    message.attach(prepare_attachment(attachment_path))
    return message