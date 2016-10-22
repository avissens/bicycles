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
        
class Customer(object): #new class of customers
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
