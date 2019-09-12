def ask_to_continue(message):
    while True:
        print(f"{message} \nContinue anyway? (y/n)")
        choice = input().lower()
        if choice == "y":
            break
        elif choice == "n":
            exit()
        else:
            print("Unrecognised input. ")