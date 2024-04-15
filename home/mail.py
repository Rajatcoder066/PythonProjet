import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from flask import Flask, request

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    # Get the HTML bill from the AJAX request
    html = request.form['html']

    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = 'sender@example.com'
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = 'Your Bill'
    body = 'Please find your bill attached.'
    msg.attach(MIMEText(body, 'plain'))

    # Attach the HTML bill as a file to the email message
    attachment = MIMEApplication(html, _subtype='html')
    attachment.add_header('Content-Disposition', 'attachment', filename='bill.html')
    msg.attach(attachment)

    # Connect to the SMTP server and send the email
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'sender@example.com'
    smtp_password = 'password'
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())

    return 'Email sent successfully!'

if __name__ == '__main__':
    app.run()
