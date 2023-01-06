import random
import string

primesti = False

def handle_response(message) -> str:
    p_message = message.lower()
    if message.content == '-nitro':
        return 'Nu poti folosi comana `-nitro` aici. Incearca pe un server.'