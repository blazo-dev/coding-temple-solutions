# 📌 Brief Overview
# Regular Expressions (Regex) are a powerful tool for matching patterns in text.
# They are used in situations like data validation, web scraping, and extracting information such as emails, phone numbers, etc.

import re

# Examples of Regex use cases:
# - Validation: Checking if a string fits a particular format (e.g., emails or phone numbers)
# - Data Extraction: Extracting useful data such as hashtags, email addresses, etc.
# - Text Replacement: Replacing text, such as anonymizing user data
# - String Splitting: Breaking up text based on specific delimiters
# - Searching for Patterns: Finding occurrences of a particular pattern

# Example 1: Finding All Matches with re.findall()
text = "Hi my name is Travis, and I like to go and do things and stuff"
ands = re.findall(r"and",
                  text)  # re.findall() returns a list of all occurrences of the given regex pattern within the text.
print(ands)  # Output: ['and', 'and', 'and']
print(len(ands))  # Output: 3

# Example 2: Extracting Hashtags
post = "I LOVE # learning #Python_is_lyfe and #Regex, this is so fun! #Code"
tags = re.findall(r"#\w+", post)
print(tags)  # Output: ['#Python_is_lyfe', '#Regex', '#Code']

# Example 3: Searching for Patterns with re.search()
email = "kareem33-34-28@gmail.com"
found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
if found:
    print(f"{found.group()} is a valid email! Please click continue!")
# Output: kareem33-34-28@gmail.com is a valid email! Please click continue!

# Example 4: Matching Patterns at the Start of a String with re.match()
url = "https://something.com"
secure = re.match(r"https", url)
if secure:
    print("This link goes to a secure website!")  # Output: This link goes to a secure website!

# Example 5: Splitting Text with re.split()
text = 'Python,Regex;Splitting-Example. Fun, right?'
words = re.split(r"[,.;\s-]+", text)
print(words)  # Output: ['Python', 'Regex', 'Splitting', 'Example', 'Fun', 'right', '']

# Example 6: Substituting Text with re.sub()
# Formatting Phone Numbers
number = "(770) 888-1180"
formatted_number = re.sub(r"\D", '', number)
print(formatted_number)  # Output: 7708881180

# Anonymizing Chat User Mentions
chat = '''
@Yve-bee123 : "I think I love Regex"
@Travis : "Aren't you married?"
@Yve_bee123 : "It's just not the same"
@Travis : "They better not see this!"
'''
anon_chat = re.sub(r"@[\w-]+", '@user-anon', chat)
print(anon_chat)

# Example 7: Grouping with Regex
# Capturing Parts of a Phone Number
text = "123-456"
pattern = r"(\d+)-(\d+)"
thematch = re.search(pattern, text)
if thematch:
    print(f"Group 1: {thematch.group(1)}")  # Output: 123
    print(f"Group 2: {thematch.group(2)}")  # Output: 456
