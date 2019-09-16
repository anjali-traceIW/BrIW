import table_maker

class Round:

    def __init__(self, owner):
        self.owner=owner
        self.orders = {}

    def add_order(self, person, drink):
        self.orders[person] = drink

    def print_orders(self):
        return table_maker.print_people_drinks(orders, ("Name", "Drink"))

    def get_people(self):
        return orders.keys()

    def get_drinks(self):
        return orders.values()