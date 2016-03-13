import random
import re

WORDS = ["SUN", "SHINE"]

def isValid(text):
    return bool(re.search(r'\bmeaning of life\b', text, re.IGNORECASE))
	
def handle(text, mic, profile):
    messages = ["The sun is a mass of incandescent gas.",
                "The sun is a miasma of incandescent plasma."]

    message = random.choice(messages)

    mic.say(message)