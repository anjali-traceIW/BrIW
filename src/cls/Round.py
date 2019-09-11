class Round:
    
    def __init__(self, owner):
        self.owner=owner
        self.orders = {}

    def add_order(self, person, drink):
        self.orders[person] = drink

    def print_orders(self):
        return print_people_drinks(orders, ("Name", "Drink"))