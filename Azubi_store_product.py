# Product, Price and Number of customer in Azubi Product store
# The given data that we are going to use 
product = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", 
           "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
old_price = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average for all product
# total price average is equal to the sum of the individual divide by the number of products

total_average_price =sum(old_price)/len(old_price)
print('Total price average for all products: ', total_average_price)

#create new price list that reduce the old price by 5$
new_price = [price -5 for price in old_price]
print('New Price List after $5 reduction: ', new_price)

# Total revenu generated from the product
data_on_product = {}
revenue_last_week = 0

for i in range(len(product)):
    price = old_price[i]
    quantity = last_week[i]
    revenue = price * quantity
    data_on_product[product[i]] = (price, quantity, revenue)
    revenue_last_week += revenue

print("Total Revenue Last Week:", revenue_last_week)
# calculate the average dialy revenu (which means divide last week revenu by 7)
daily_revenue = revenue_last_week/7
print('Average daily Revenue: ',daily_revenue)

#Products less than 30$ 
print('Products less than $30 after reduction:')
print('--------------------')
price_dict = dict(zip(product, new_price))

for product, price in price_dict.items():
    if price < 30:
        print(f"{product}: {price}")
print('--------------------')