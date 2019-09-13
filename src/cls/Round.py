class Round:
    
    def __init__(self, owner):
        self.owner=owner
        self.orders = {}

    def add_order(self, person, drink):
        self.orders[person] = drink

    def print_orders(self):

    def get_people(self):
        return orders.keys()

    def get_drinks(self):
        return orders.values()