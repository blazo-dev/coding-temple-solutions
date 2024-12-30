"""
👾💻 Final Challenge: Build a text-based name generator that combines random first and last names using string manipulation.
HINT:  Look up and import the "random" module.
"""

import random

first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
last_names = ["Sachs", "Katina", "Peck", "Menhir"]

random_first_name = random.choice(first_names)
random_last_name = random.choice(last_names)

print(f"{random_first_name} {random_last_name}")
