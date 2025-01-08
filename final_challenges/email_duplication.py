"""
👾 Final Challenge: Email List Deduplication
You have two email lists, but some people may be in both. Write a function to:

Remove duplicates.
Show which emails exist in both lists.
Show emails that are unique to each list.
"""


def clean_email_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    # Remove duplicates and merge
    all_unique = set1.union(set2)
    print("All unique emails:", all_unique)

    # Common emails
    common_emails = set1.intersection(set2)
    print("Emails in both lists:", common_emails)

    # Emails unique to each list
    unique_emails = set1.symmetric_difference(set2)
    print("Emails unique to each list:", unique_emails)


email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

clean_email_lists(email_list1, email_list2)

