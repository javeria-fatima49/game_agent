import random

def generate_event():
    events = ["monster", "treasure", "empty path", "mystic fountain"]
    return random.choice(events)