import smtplib as smtp
import ssl
import email as mail
import json
import mail_beautifier as mb

# Fetching sender configuration.
with open('assets/config.json') as cf:
    send_config = json.load(cf)

print(send_config['ProvidorUrl'], send_config['Port'])

with open('assets/draft_config.json') as df:
    draft_config = json.load(df)

# Fetching password for given Email ID.
password = input(f"Enter Password for {draft_config['sender']}\n")

# Populating default context for SSL.
ssl_context = ssl.create_default_context()

with smtp.SMTP_SSL(send_config['ProvidorUrl'], send_config['Port'], context=ssl_context) as server:
    message = mb.prepare_draft(draft_config, "This is a Test mail.", "assets/sample.pdf")
    server.login(draft_config['sender'], password)
    server.sendmail(draft_config['sender'], [draft_config['receiver'], draft_config['bcc']], message.as_string())