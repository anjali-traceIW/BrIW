import sys
# get-people, get-drinks (hardcoded), handle no/wrong/diff no. args
args = sys.argv
help = "HELP: Outputs list of people or drinks using commands get-people, get-drinks or get-both."
line_width = 20

def make_row(text):
    return "| {}{}|\n".format(text, " "*(line_width-3-len(text)))

def print_as_table(header, rows):
    table_break = "+{}+\n".format("-"*(line_width-2))
    text = table_break + make_row(header) + table_break
    for item in rows:
        text += make_row(item)
    text += table_break
    print(text)

if not len(args) == 2:
    print(f"Expected 1 argument, received {len(args)-1}.")
    exit()

# assert len(args) == 2, "Expected 1 argument, received {}.".format(len(args)-1)

people = ["Scooby", "Shaggy", "Fred", "Daphne", "Velma"]
drinks = ["coffee", "tea", "lemonade"]

if args[1] == "-h":
    print(help)
elif args[1] == "get-people":
    print_as_table("People", people)
elif args[1] == "get-drinks":
    print_as_table("Drink", drinks)
elif args[1] == "get-both":
    print_as_table("People", people)
    print()
    print_as_table("Drink", drinks)
else: 
    print("Unrecognised command. Use -h for help.")