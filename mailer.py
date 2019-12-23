import smtplib as smtp
import ssl
import email as mail
import json
import csv
import mail_beautifier as mb
import time

# Fetching sender configuration.
with open('assets/config.json') as cf:
    send_config = json.load(cf)

# Set Attachments Here.
attachments = ['assets/Brochure.pdf', 'assets/corporate_sponsorship_avenues.pdf']

# Set Mail Draft Settings in file 'draft_config.json'
with open('assets/draft_config.json') as df:
    draft_config = json.load(df)

# Fetching password for given Email ID.
password = input(f"Enter Password for {draft_config['sender']}\n")

# Fetch Mail body.
with open("assets/mail.txt") as mail:
    mail_str = mail.read()

with open("assets/test_db.csv") as contacts_file:
    contacts = csv.reader(contacts_file)

    for contact in contacts:    # Fetching Individual contacts.
        mail_body = mail_str.format(contact[0]) # Fill in the name of the Contact accordingly.

        # Populating default context for SSL.
        ssl_context = ssl.create_default_context()

        with smtp.SMTP_SSL(send_config['ProvidorUrl'], send_config['Port'], context=ssl_context) as server:
            message = mb.prepare_draft(draft_config, mail_body, attachments)
            server.login(draft_config['sender'], password)
            server.sendmail(draft_config['sender'], [contact[1], contact[2]], message.as_string())
            time.sleep(1)