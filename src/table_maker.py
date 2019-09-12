def calculate_column_width(rows):
    longest_item = 0
    for item in rows:
        if len(item) > longest_item:
            longest_item = len(item)
    
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

def print_people_drinks(preferences, headers=("Person", "Fav Drink")):
    names_width = calculate_column_width(people)-6
    drinks_width = calculate_column_width(drinks)-6
    header = "{}{} | {} {}".format(headers[0], " "*(names_width-1-len(headers[0])), headers[1], " "*(drinks_width-len(headers[1])))
    rows = []
    for name_id in preferences:
        name = get_person_from_id(name_id)
        if preferences[name_id] != "":
            drink = get_drink_from_id(preferences[name_id])
        else:
            drink = ""
        rows.append("{}{} | {}{}".format(name, " "*(names_width-len(name)-1), drink, " "*(drinks_width-len(drink)-1)))
    return _print_as_table(header, rows, calculate_column_width(rows), False)
