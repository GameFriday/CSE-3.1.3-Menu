sandwich_type = input("Please choose the type of sandwich (Chicken $5.25, Beef $6.25, or Tofu $5.75): ")
if sandwich_type.lower() == "chicken" or sandwich_type.lower() == "beef" or sandwich_type.lower() == "tofu":
  print("You choose:", sandwich_type)
elif sandwich_type.lower() == "":
  print("you didn't choose anything")
else: 
  print("Please make sure it is spelled correctly and has no spaces.")
Beverage = input("Would you like a beverage?")
if Beverage.lower() == "yes":
  Beverage = input("What size would you like? Small $1.00, Medium $1.75, or Large $2.25?")
elif Beverage.lower() == "":
  print("you didn't choose anything")
else: 
  print("Please make sure it is spelled correctly and has no spaces.")
if sandwich_type.lower() == "chicken":
  sandwichPrice = 5.25
elif sandwich_type.lower() == "beef":
    sandwichPrice = 6.25
elif sandwich_type.lower() == "tofu":
    sandwichPrice = 5.75
if Beverage.lower() == "no":
  drinkPrice = 0
elif Beverage.lower() == "small":
  drinkPrice = 1.00
elif Beverage.lower() == "medium":
    drinkPrice = 1.75
elif Beverage.lower() == "large":
    drinkPrice = 2.25
totalcost =(drinkPrice + sandwichPrice)
print("You choose a", sandwich_type, "sandwich", "and", Beverage, "beverage.")
print("The total cost will be:", totalcost, "dollars.")
