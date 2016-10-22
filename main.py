from bicycles import Bicycle, Shop, Customer
import random

myvelo = Bicycle("myvelo-333", 500, 120) #bike instance 1
panda = Bicycle("panda-444", 400, 350) #bike instance 2
ferrari = Bicycle("ferrari-777", 300, 700) #bike instance 3
fiat = Bicycle("fiat-888", 600, 150) #bike instance 4
express = Bicycle("express-456", 200, 400) #bike instance 5
city = Bicycle("city-1000", 100, 900) #bike instance 6
bikes = [myvelo, panda, ferrari, fiat, express, city]

my_shop = Shop("Velo4u", bikes, 10) #shop instance

anna = Customer("Anna", 200) #customer instance 1
ruben = Customer("Ruben", 500) #customer instance 2
maxim = Customer("Maxim", 1000) #customer instance 3
customers = [anna, ruben, maxim]

def display(self):
        print(self.shop_name + "'s inventory: ")
        for bike in self.inventory:
            print(bike.model + ": " + "weight(gr) - " + str(bike.weight) + ", price($) - " + str(self.price(bike)))

print(display(my_shop))

def offer(self):
        offered_bikes = []
        for item in my_shop.inventory:
            if self.budget >= my_shop.price(item):
                offered_bikes.append(item.model)
        print(self.name + ", this is the choice you have: " + ", ".join(offered_bikes))
        return offered_bikes
      
def sell(self, offered_bikes):
        choice = random.choice(offered_bikes)
        budget_left = 0
        print("Ok, I'll go for this one: " + choice)
        for bike in my_shop.inventory:
            if choice == bike.model:
                budget_left = self.budget - my_shop.price(bike)
                my_shop.inventory.remove(bike)
                my_shop.sold_bikes.append(bike)
        print(self.name + ", enjoy your new bike! You still have $" + str(budget_left) + " left in your budget. Fancy some accessories?")

for customer in customers:
    offered_bikes = offer(customer)
    print(sell(customer, offered_bikes))

print(display(my_shop))

def calc_profit(self): #calculating profit
        sell_profit = 0
        for bike in self.sold_bikes:
            sell_profit = int((bike.cost*self.margin)/100 - self.expenses)
            self.profit += sell_profit
        return self.profit

print("Shop's profit is $" + str(calc_profit(my_shop)))