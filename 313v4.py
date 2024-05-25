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
elif Beverage.lower() == "no":
  print("Are you sure you don't want a drink?")
else: 
  print("Please make sure it is spelled correctly and has no spaces.")
print("You choose", Beverage, "drink.")
Fries = input("Would you like fries?")
if Fries.lower() == "yes":
    global FriesSize
    FriesSize = input("What size would you like? Small $1.00, Medium $1.50, or Large $2.00?")
    if FriesSize.lower() == "small":
        MegaSize = input("Would you like to mega-size your fries for $1.00 more?")
        if MegaSize.lower() == "yes":
            print("You chose to mega-size your fries.")
            FriesSize = "Large"
    print("You choose a", FriesSize, "fries.")
if Fries.lower() == "no":
  print("You sure you don't want fries?")
  FriesSize = "no"
ketchup = abs(int(input("How many ketchup packets would you like? ($0.25 each)")))
print("You choose", ketchup, "ketchup packets.")
print("You ordered", sandwich_type, "sandwich,", Beverage, "drink,", FriesSize, "fries,", str(ketchup), "ketchup packets.")
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
if Fries.lower() == "no":
  friesPrice = 0
else:
  if FriesSize.lower() == "small":
      friesPrice = 1.00
  elif FriesSize.lower() == "medium":
      friesPrice = 1.50
  elif FriesSize.lower() == "large":
      friesPrice = 2.00
discount = 0
if Beverage.lower() != "no" and Fries.lower() != "no":
  discount = 1.00
ketchupPrice = float(ketchup) * 0.25
total =(sandwichPrice + drinkPrice + friesPrice + ketchupPrice - discount)
print("The order total will be", total, "dollars")
