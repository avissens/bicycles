from bicycles_v2 import Bicycle, Shop, Customer

myvelo = Bicycle("myvelo-333", 500, 120) #bike instance 1
panda = Bicycle("panda-444", 400, 350) #bike instance 2
ferrari = Bicycle("ferrari-777", 300, 700) #bike instance 3
fiat = Bicycle("fiat-888", 600, 150) #bike instance 4
express = Bicycle("express-456", 200, 400) #bike instance 5
city = Bicycle("city-1000", 100, 900) #bike instance 6
bikes = [myvelo, panda, ferrari, fiat, express, city]

my_shop = Shop("Velo4u", bikes, 10) #shop instance
shops = [my_shop]

anna = Customer("Anna", 200) #customer instance 1
ruben = Customer("Ruben", 500) #customer instance 2
maxim = Customer("Maxim", 1000) #customer instance 3
customers = [anna, ruben, maxim]

if __name__ == "__main__":
    my_shop.display()
    for customer in customers:
        offered_bikes = customer.offer(my_shop)
        budget_left = customer.sell(offered_bikes, my_shop)
        print(customer.name + ", enjoy your new bike! You still have $" + str(customer.budget) + " left in your budget. Fancy some accessories?")
    my_shop.display()
    my_shop.calc_profit()