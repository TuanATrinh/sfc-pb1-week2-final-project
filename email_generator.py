from file_manager import load_templates
from datetime import datetime


def generate_email():
    templates = load_templates()
    timestamp = datetime.now().strftime("%m/%d/%Y %I:%M %p")
    print()
    print("What do you need to communicate?")

    for template in templates:
        print(f"{template['id']}. {template['name']}")

    choice = input("Select an option: ")

    for template in templates:
        if template["id"] == choice:
            recipient = input("Who is this email for? ")
            details = input("What details should be included? ")

            print()
            print(f"To: {recipient}")
            print(f"Subject: {template['subject']}")
            print()
            body = template["body"].replace("\\n", "\n")
            print(body)
            print()
            print("Additional Details: ")
            print(details)

            with open("data/history.txt", "a") as file:
                file.write(f"Date: {timestamp}\n")
                file.write(f"To: {recipient}\n")
                file.write(f"Subject: {template['subject']}\n")
                file.write("\n")
                file.write(body + "\n")
                file.write(details + "\n")
                file.write("V/r\n")
                file.write("TUAN A. TRINH, MSGT, USSF\n")
                file.write("Intelligence Integrations Branch Chief\n")
                file.write("National Reconnaissance Office\n")
                file.write("\n")
                file.write("----------------------------------------\n")
                file.write("\n")

            print()
            print("V/r")
            print("TUAN A. TRINH, MSGT, USSF")
            print("Intelligence Integrations Branch Chief")
            print("National Reconnaissance Office")
            return

    print("Invalid selection.")