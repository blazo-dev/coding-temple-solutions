"""Final Challenge (End of Lesson Exercise)
Task: You are tasked with creating a simple email validation script that accepts a list of emails and checks if they are valid based on a regex pattern.
"""
import re

emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org"
]

email_pattern = r"[\w.-]+@[\w-]+\.[a-z]{2,3}"

# Write your code below to validate the emails using re.search()

for email in emails:
    # Implement regex search here
    is_match = re.search(email_pattern, email)

    if is_match:
        print(f"{email} is a valid email")
    else:
        print(f"{email} is not a valid email")
# Hint: Use the re.search() function and the pattern for a valid email structure ([\w.-]+@[\w-]+\.[a-z]{2,3}).
