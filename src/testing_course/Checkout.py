
class Checkout:
    class Discount:
        def __init__(self, n_items, price):
            self.n_items = n_items
            self.price = price
    
    
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0
    
    
    def add_discount(self, item, n_items, price):
        discount = self.Discount(n_items, price)
        self.discounts[item] = discount

    
    
    def add_item_price(self, item, price):
        self.prices[item] = price
    
    
    def add_item(self, item):
        if item not in self.prices:
            raise Exception("Bad item")
        
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
    
    
    def calculate_total(self):
        total = 0
        for item, c in self.items.items():
            total += self.calculate_item_total(item, c)
        return total
    
    
    def calculate_item_total(self, item, c):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if c >= discount.n_items:
                total += self.calculate_item_discounted_total(item, c, discount)
            else:
                total += self.prices[item] * c
        else:        
            total += self.prices[item] * c
            
        return total
    
    def calculate_item_discounted_total(self, item, c, discount):
        total = 0
        n_discounts = c / discount.n_items
        total += n_discounts * discount.price
        remaining = c % discount.n_items
        total += remaining * self.prices[item]
        return total