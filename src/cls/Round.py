import src.table_maker

class Round:

    def __init__(self, owner, active=False):
        self.owner = owner
        self.orders = {}
        self.active = active

    def get_people(self):
        return orders.keys()

    def get_drinks(self):
        return orders.values()

    def add_order(self, person, drink):
        self.orders[person] = drink

    def print_orders(self):
        return table_maker.print_people_drinks(orders, ("Name", "Drink"))
