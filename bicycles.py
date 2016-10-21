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

    def price(self, bike): #calculating price
        for item in self.inventory:
            price = bike.cost + (bike.cost*self.margin)/100
        return price

    def calc_profit(self, bike): #calculating profit
        profit = (bike.cost*self.margin)/100 - self.expenses
        print("Shop's profit is", my_shop.calc_profit(bike.model), "dollars.")
        return profit
        
    def display(self):
        print(my_shop.shop_name + " offers today: ")
        for bike in my_shop.inventory:
            price = bike.cost + int((bike.cost*self.margin)/100)
            print(bike.model + ": " + "weight(gr) - " + str(bike.weight) + ", price($) - " + str(price))
        
my_shop = Shop("Velo4u", [myvelo, panda, ferrari, fiat, express, city], 10) #new instance
        
class Customer(object): #new class of customers
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def offer(self):
        offered_bikes = []
        for item in my_shop.inventory:
            if self.budget >= my_shop.price(item):
                offered_bikes.append(item.model)
        print(self.name + ", this is the choice you have: " + ", ".join(offered_bikes))
        return offered_bikes

    def sell(self):
        choice = random.choice(offered_bikes)
        print("Ok, I'll go for this one: " + choice)
        budget_left = self.budget - my_shop.price(choice)
        print(self.name + ", enjoy your new bike! You still have" + budget_left + "left in your budget. May be you fancy some accessories?")
            
anna = Customer("Anna", 200) #instance 1
ruben = Customer("Ruben", 500) #instance 2
maxim = Customer("Maxim", 1000) #instance 3

if __name__ == "__main__":
    my_shop.display()
    anna.offer()
    ruben.offer()
    maxim.offer()
    anna.sell()