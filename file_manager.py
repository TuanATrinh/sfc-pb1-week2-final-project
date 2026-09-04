import csv
from datetime import datetime

def load_templates():
    templates = []

    with open("data/emails.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            templates.append(row)

    return templates


def view_history():
    with open("data/history.txt", "r") as file:
        history = file.read()

    emails = sort_history()

    print()
    print("==========  EMAIL HISTORY ==========")

    if history:
        for email in emails:
            lines = email.split("\n")

            print(lines[0])
            print(lines[1])
            print(lines[2])
            print()
            for line in lines[4:]:
                if line == "V/r":
                    break

                print(line)

            print("----------------------------------------")
    else:
        print("No email have been generated yet.")


def get_recipients():
    recipients = []

    with open("data/history.txt", 'r') as file:
        for line in file:
            if line.startswith("To:"):
                recipient = line.strip().replace("To: ", "")
                if recipient not in recipients:
                  recipients.append(recipient)

    return recipients


def get_history_by_recipient(recipient):
    matching_emails = []

    with open("data/history.txt", 'r') as file:
        history = file.read()

    emails = history.split("----------------------------------------")

    for email in emails:
        if f"To: {recipient}" in email:
            matching_emails.append(email.strip())

    return matching_emails

def get_email_date(email):
    first_line = email.split("\n")[0]
    date_text = first_line.replace("Date: ", "")
    date = datetime.strptime(date_text, "%m/%d/%Y %I:%M %p")

    return date

def sort_history():
    with open("data/history.txt", "r") as file:
        history = file.read()

    emails = history.split("----------------------------------------")

    clean_emails = []

    for email in emails:
        email = email.strip()

        if email:
            clean_emails.append(email)

    emails = clean_emails

    emails.sort(key=get_email_date, reverse=True)

    return emails