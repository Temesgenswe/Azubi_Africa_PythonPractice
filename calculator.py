# as the finance officer of Asanka Hotel, the food and beverages has 
#requested a program that calculate the total amount of a meal purchased and 
# with a fixed tip
chare_for_food = int(input(" Enter  Charge of the food: "))
percent_tip = chare_for_food * (18/100)
percent_tax = chare_for_food * (7/100)

print("These are the Amount of Tip_rate, Tax_rate and Grand Total ")
print(" ")
print("Tip = $" + str(percent_tip))
print(" ")
print(" Sales tax = $" + str(percent_tax))
print(" ")
print(" Grand Total = $" + str (chare_for_food + percent_tip + percent_tax))
