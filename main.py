from file_manager import view_history, get_recipients, get_history_by_recipient
from email_generator import generate_email





def main():
    while True:
        print("========================================")
        print("       PROFESSIONAL EMAIL GENERATOR")
        print("========================================")

        print("1. Generate Email")
        print("2. View Email History")
        print("3. Exit")

        choice = input("Select an option: ")

    #Chooses to generate email
        if choice == "1":
            generate_email()

    # History
        elif choice == "2":
            while True:
                print()
                print("========== EMAIL HISTORY ==========")
                print("1. View All")
                print("2. View by Recipient")
                print("3. Back")

                history_choice = input("Select an option: ")
            #All history
                if history_choice == "1":
                    view_history()
            #By recipient
                elif history_choice == "2":
                    recipients = get_recipients()

                    if len(recipients) == 0:
                        print("No email history found.")
                    else:

                        print()
                        for index, recipient in enumerate(recipients, start=1):
                            print(f"{index}. {recipient}")

                        print(f"{len(recipients) +1}. Back")

                        recipient_choice = int(input("Select a recipient: "))

                        if recipient_choice == len(recipients) +1:
                            print("Returning to email history.")
                            break
                        else:
                            recipient_index = recipient_choice -1

                            if recipient_index >= 0 and recipient_index < len(recipients):
                                selected_recipient = recipients[recipient_index]

                                print()
                                print(f"========== HISTORY FOR {selected_recipient} ==========")

                                emails = get_history_by_recipient(selected_recipient)

                                for email in emails:
                                    print()
                                    print(email)

                            else:
                                print("invalid recipient selection")

                #return to main menu
                elif history_choice == "3":
                    print("Returning to main menu")
                    break
                else:
                    print("invalid selection")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
