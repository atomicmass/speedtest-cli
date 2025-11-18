import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

ses = boto3.client('ses', region_name='af-south-1')

msg = MIMEMultipart()
msg['Subject'] = 'Report with attachment'
msg['From'] = 'sceoan@gmail.com'
msg['To'] = 'sceoan@gmail.com'

# Body
msg.attach(MIMEText('See attached file', 'plain'))

# # Attachment
# with open('report.pdf', 'rb') as f:
#     part = MIMEApplication(f.read())
#     part.add_header('Content-Disposition', 'attachment', filename='report.pdf')
#     msg.attach(part)

resp = ses.send_raw_email(RawMessage={'Data': msg.as_string()})
print('MessageId:', resp['MessageId'])