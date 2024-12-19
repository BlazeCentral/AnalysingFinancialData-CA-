#Receipt Generater Project 
#Project 2 under Hello World, Analysing Financial Data w Python

# Products
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00
stylish_settee_description = '''Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'''
stylish_settee_price = 180.50
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price = 52.15
#Tax
sales_tax = 0.088
#Initial count for customers
customer_one_total = 0
#Customer Shopping cart 
customer_one_itemization = ""
#Shopping procedure
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += stylish_settee_price
customer_one_itemization += stylish_settee_description

# Calc checkout price
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Receipt
print('RECEIPT')

print('Customer One Items:')
print(customer_one_itemization)
print('Customer One Total:')
print(customer_one_total)




