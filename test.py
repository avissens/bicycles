#got rid of dependecies in functions like "my_shop" in offer()
import random

class Bicycle(object): #new class of bike
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
myvelo = Bicycle("myvelo-333", 500, 120) #instance 1
panda = Bicycle("panda-444", 400, 350) #instance 2
ferrari = Bicycle("ferrari-777", 300, 700) #instance 3
fiat = Bicycle("fiat-888", 600, 150) #instance 4
express = Bicycle("express-456", 200, 400) #instance 5
city = Bicycle("city-1000", 100, 900) #instance 6
        
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
        
my_shop = Shop("Velo4u", [myvelo, panda, ferrari, fiat, express, city], 10) #new instance
        
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
        budget_left = 0
        print("Ok, I'll go for this one: " + choice)
        for item in shop.inventory:
            if choice == item.model:
                budget_left = self.budget - shop.price(item)
                shop.inventory.remove(item)
                shop.sold_bikes.append(item)
        print(self.name + ", enjoy your new bike! You still have $" + str(budget_left) + " left in your budget. Fancy some accessories?")

anna = Customer("Anna", 200) #instance 1
ruben = Customer("Ruben", 500) #instance 2
maxim = Customer("Maxim", 1000) #instance 3

if __name__ == "__main__":
    my_shop.display()
    offered_bikes = anna.offer(my_shop)
    anna.sell(offered_bikes, my_shop)
    offered_bikes = ruben.offer(my_shop)
    ruben.sell(offered_bikes, my_shop)
    offered_bikes = maxim.offer(my_shop)
    maxim.sell(offered_bikes, my_shop)
    my_shop.display()
    my_shop.calc_profit()
    