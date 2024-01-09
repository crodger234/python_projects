MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

Revenue = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# This is the resources of the Cappuccino: Water, Milk and Coffee. Just the values. This also includes the cost of the drink. 

cap_water = MENU['cappuccino']['ingredients']['water']
cap_milk = MENU['cappuccino']['ingredients']['milk']
cap_coffee = MENU['cappuccino']['ingredients']['coffee']

cap_cost = (MENU['cappuccino']['cost'])

#//////////////////////////////////////////////////////////////////////////////////

# This is the resources of the Espresso: Water and Coffee. Just the values. This also includes the cost of the drink. 

esp_water = MENU['espresso']['ingredients']['water']
esp_coffee = MENU['espresso']['ingredients']['coffee']

esp_cost = (MENU['espresso']['cost'])

#//////////////////////////////////////////////////////////////////////////////////

# This is the resources of the latte: Water, Milk and Coffee. Just the values. This also includes the cost of the drink. 

lat_water = MENU['latte']['ingredients']['water']
lat_milk = MENU['latte']['ingredients']['milk']
lat_coffee = MENU['latte']['ingredients']['coffee']

lat_cost = (MENU['latte']['cost'])

#//////////////////////////////////////////////////////////////////////////////////

# The resources of the coffee machine: Milk, Water, and Coffee 

res_water = resources['water']
res_coffee = resources['coffee']
res_milk = resources['milk']

#//////////////////////////////////////////////////////////////////////////////////


# These are the valid options to choose from the coffee machine: Cappuccino, Espresso, and Latte

options = ['espresso' , 'latte' , 'cappuccino']

#//////////////////////////////////////////////////////////////////////////////////




# This what runs when the coffee machine is on 

while True:
    user = input("What would you like? (espresso/latte/cappuccino): ")
    user = user.lower()
    if user not in options:
        print("Not a valid option. Please choose one of the three.")
        
    #//////////////////  This is where if a user selects Cappuccino //////////////////////////////////////////////////

    if user == "cappuccino":
        if cap_coffee > res_coffee or cap_milk > res_milk or cap_water > res_water:
            print("There is not enough resources to make a cappuccino.")
        else:
            while True:
                print("Please insert coins")
                quarters = input("How many quarters: ")
                dimes = input("How many dimes: ")
                nickels = input("How many nickels: ")
                pennies = input("How many pennies: ")
                
                quarters = float(quarters) *.25
                dimes = float(dimes) * .10
                nickels = float(nickels) * .05
                pennies = float(pennies) * .01
                total = quarters + dimes + nickels + pennies
                change_back = total - cap_cost
                change_back = float(change_back)
                
                if total < cap_cost:
                    print("You did not provide enough money. Please provide more.")
                else:
                    res_coffee = res_coffee - cap_coffee
                    res_milk = res_milk - cap_milk
                    res_water = res_water - cap_water 
                    break
            print(f"The cost of the drink was {cap_cost}. This is your change {round(change_back,2)}")
            
    #//////////////////  This is where if a user selects Latte /////////////////////////////////////////////////////////

    if user == "latte":
        if lat_coffee > res_coffee or lat_milk > res_milk or lat_water > res_water:
            print("There is not enough resources to make a Latte.")
        else:
            while True:
                print("Please insert coins")
                quarters = input("How many quarters: ")
                dimes = input("How many dimes: ")
                nickels = input("How many nickels: ")
                pennies = input("How many pennies: ")
                
                quarters = float(quarters) *.25
                dimes = float(dimes) * .10
                nickels = float(nickels) * .05
                pennies = float(pennies) * .01
                total = quarters + dimes + nickels + pennies
                change_back = total - cap_cost
                change_back = float(change_back)
                
                if total < lat_cost:
                    print("You did not provide enough money. Please provide more.")
                else:
                    res_water = res_water - lat_water
                    res_milk = res_milk - lat_milk
                    res_coffee = res_coffee - lat_coffee 
                    break    
            print(f"The cost of the drink was {lat_cost}. This is your change {round(change_back,2)}")

    #//////////////////  This is where if a user selects Espresso /////////////////////////////////////////////////////////
        
    if user == "espresso":
        if esp_coffee > res_coffee or esp_water > res_water:
            print("There is not enough resources to make a Espresso.")
        else:
            while True:
                print("Please insert coins")
                quarters = input("How many quarters: ")
                dimes = input("How many dimes: ")
                nickels = input("How many nickels: ")
                pennies = input("How many pennies: ")
                
                quarters = float(quarters) *.25
                dimes = float(dimes) * .10
                nickels = float(nickels) * .05
                pennies = float(pennies) * .01
                total = quarters + dimes + nickels + pennies
                change_back = total - cap_cost
                change_back = float(change_back)
                
                if total < lat_cost:
                    print("You did not provide enough money. Please provide more.")
                else:
                    res_water = res_water - esp_water
                    res_coffee = res_coffee - esp_coffee 
                    break
            print(f"The cost of the drink was {esp_cost}. This is your change {round(change_back,2)}")
        pass
        
    if user == "report":
        print(f" Water: {res_water}\n Milk: {res_milk}\n Coffee: {res_coffee}")
        
    if user == "off":
        break 
  
    
        
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
   
 








