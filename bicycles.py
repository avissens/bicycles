import random

class Bicycle(object): #new class of bike
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
class Shop(object): #new class of shops
    margin = 20
    def __init__(self, shop_name, inventory, expenses):
        self.shop_name = shop_name
        self.inventory = inventory
        self.expenses = expenses
        self.profit = 0
        self.sold_bikes = []

    def price(self, bike): #calculating price
        for item in self.inventory:
            price = bike.cost + (bike.cost*self.margin)/100
        return int(price)

    def calc_profit(self): #calculating profit
        sell_profit = 0
        for item in self.sold_bikes:
            sell_profit = int((item.cost*self.margin)/100 - self.expenses)
            self.profit += sell_profit
        print("Shop's profit is $" + str(self.profit))
        return self.profit
        
    def display(self):
        print(self.shop_name + "'s inventory: ")
        for item in self.inventory:
            print(item.model + ": " + "weight(gr) - " + str(item.weight) + ", price($) - " + str(self.price(item)))

class Customer(object): #new class of customers
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def offer(self, shop):
        offered_bikes = []
        for item in shop.inventory:
            if self.budget >= shop.price(item):
                offered_bikes.append(item.model)
        print(self.name + ", this is the choice you have: " + ", ".join(offered_bikes))
        return offered_bikes
        
    def sell(self, offered_bikes, shop):
        choice = random.choice(offered_bikes)
        print("Ok, I'll go for this one: " + choice)
        for item in shop.inventory:
            if choice == item.model:
                self.budget -= shop.price(item)
                shop.inventory.remove(item)
                shop.sold_bikes.append(item)
        return self.budget        




    