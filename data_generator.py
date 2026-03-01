import random

def generate_data():
    return [
        random.randint(60, 140),      # heart rate
        random.randint(85, 100),      # spo2
        round(random.uniform(35, 40), 1),  # temperature
        random.randint(90, 160)       # blood pressure
    ]