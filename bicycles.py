class Bicycles(object): #new class of bicycles
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
myvelo = Bicycles("myvelo-333", 500, 150) #instance 1
panda = Bicycles("panda-444", 400, 350) #instance 2
ferrari = Bicycles("ferrari-777", 300, 700) #instance 3
fiat = Bicycles("fiat-888", 600, 170) #instance 4
express = Bicycles("express-456", 200, 400) #instance 5
city = Bicycles("city-1000", 100, 900) #instance 6
        
class Shops(object): #new class of shops
    margin = 20
    def __init__(self, shop_name, inventory, expenses):
        self.shop_name = shop_name
        self.inventory = inventory
        self.expenses = expenses

    def price(self, bicycles): #calculating price
        for item in self.inventory:
            price = bicycles.cost + (bicycles.cost*self.margin)/100
        return price

    def calc_profit(self, bicycles): #calculating profit
        profit = (bicycles.cost*self.margin)/100 - self.expenses
        print("Shop's profit is", my_shop.calc_profit(bicycles.model), "dollars.")
        return profit
        
    def display(self, bicycles):
        for item in my_shop.inventory:
            print(my_shop.shop_name + "offers today:" + my_shop.inventory(item))
        
my_shop = Shops("Velo4u", [myvelo, panda, ferrari, fiat, express, city], 10) #new instance
        
class Customers(object): #new class of customers
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        
    def offer(self):
        offer = []
        for item in my_shop.inventory:
            if self.budget >= my_shop.price(item):
                offer.append(item.model)
        print(self.name + ", this is the choice you have: " + ", ".join(offer))
        return offer

#    def sell(self, bicycles):
        
            
anna = Customers("Anna", 200) #instance 1
ruben = Customers("Ruben", 500) #instance 2
maxim = Customers("Maxim", 1000) #instance 3

anna.offer()
maxim.offer()