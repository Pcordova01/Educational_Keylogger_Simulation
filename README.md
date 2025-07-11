# Python Keylogger with Email Reporting

** Disclaimer: This project is for ethical purposes only!! Please do not attempt to deploy this program **

## Description

This project is a simple Python keylogger that captures keystrokes using the `pynput` library and sends the recorded input to a specified email address after every 10 keystrokes. It simulates how attackers might exfiltrate data — providing insight into defensive security, ethical hacking, and automation.

## Features

- Logs all keystrokes typed on the keyboard
- Sends captured keystrokes to a Gmail inbox
- Triggers email after every 10 keys
- Built for testing and learning about keylogging mechanisms
  
## Demo
<video src="https://github.com/user-attachments/assets/e71172f6-4e8d-4a28-bc02-c7f5f5341897" controls width="400"></video>

## How to Run the App

- Clone the repository: https://github.com/your-username/python-keylogger-email-demo.git  
- Open the project folder in VS Code  
- Open the `send_email.py` file and replace the email, password, and receiver with your own Gmail and [App Password](https://myaccount.google.com/apppasswords)  
- Open a terminal and run:
  ```bash
  pip install pynput
  python main.py


