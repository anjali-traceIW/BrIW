def calculate_column_width(rows):
    longest_item = len(max(rows, key=len))
    if longest_item+6 > 20:
        return longest_item+6
    return 20

def make_row(text, table_width, use_index=True, index=""):
    if use_index:
        return "| {} {}{} |\n".format(index, text, " "*(table_width-6-len(text)))
    else:
       return "| {}{} |\n".format(text, " "*(table_width-4-len(text)))

def make_table_break(table_width):
    return "+{}+\n".format("-"*(table_width-2))

def _print_as_table(header, rows, table_width, use_index):
    text = make_table_break(table_width) + make_row(header, table_width, use_index, index=" ") + make_table_break(table_width)
    for index in range(len(rows)):
        text += make_row(rows[index], table_width, use_index, index=index+1)
    text += make_table_break(table_width)
    return text

def print_single_column_table(header, rows):
    return _print_as_table(header, rows, calculate_column_width(rows), True)

def extract_people_and_drinks(people):
    list_of_people =[]
    list_of_drinks=[]
    for person in people:
        list_of_people.append(person.name)
        list_of_drinks.append(person.favourite_drink.name)
    return list_of_people, list_of_drinks
    
def extract_drinks_names(drinks):
    list_of_drinks=[]
    for drink in drinks:
        list_of_drinks.append(drink.name)
    return  list_of_drinks

def print_people_drinks(people_data, headers=("Person", "Fav Drink")):
    people, drinks = extract_people_and_drinks(people_data)
    names_width = calculate_column_width(people)-6
    drinks_width = calculate_column_width(drinks)-6
    header = "{}{} | {} {}".format(headers[0], " "*(names_width-1-len(headers[0])), headers[1], " "*(drinks_width-len(headers[1])))
    rows = []
    for person in people_data:
        name = person.name
        drink = person.favourite_drink.name
        rows.append("{}{} | {}{}".format(name, " "*(names_width-len(name)-1), drink, " "*(drinks_width-len(drink)-1)))
    return _print_as_table(header, rows, calculate_column_width(rows), False)
