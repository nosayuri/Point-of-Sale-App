# shopping_cart.py


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
#to exit a loop ctrl+c

#INPUTS
product_ids = []

while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if product_id == "DONE":
        break
    elif int(product_id) > 20:
        print ("Invalid Product. Type again:")
    else:
        product_ids.append(int(product_id))

#RECEIPT HEADER
print ("------------------")
print ("J-Mart Grocery Store")
print ("Phone: +1(233)455-6778")
print ("Web: j-mart.com")


import datetime
checkout_time = datetime.datetime.now()
print (checkout_time.strftime("%A | %B %d, %Y | %I:%M %p"))

#RECEIPT ITEMS LIST
print ("------------------")
print ("Shopping Cart Items:")

raw_total = 0

for pid in product_ids:
    matching_products= [product for product in products if product ["id"]== pid]
    matching_product = matching_products[0]
    raw_total = raw_total + matching_product["price"]
    print ("+ " + matching_product["name"] + " ($" + str("{0:.2f}".format(matching_product["price"])) + ")")

#TOTALS
print ("-------------")
print ("Subtotal: $" + str("{0:.2f}".format(raw_total)))

taxes = raw_total * 0.08875
print ("Plus NYC Taxes (8.875%): $" + str("{0:.2f}".format(taxes)))

total = taxes + raw_total
print ("Total: $" + str("{0:.2f}".format(total)))

print ("-------------")

#FINAL MESSAGE
print ("Thank you for shopping at J-Mart! Please come again.")
