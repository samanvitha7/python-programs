'''Write a program that repeatedly asks the user to enter product names and prices.Store all of
 these in a dictionary whose keys are the product names and whose values are theprices. When 
 the user is done entering products and prices, allow them to repeatedly enter a product name
   and print the corresponding price or a message if the product is not in the dictionary.'''
temp='y'
product={}
while temp=='y':
    name=input("Enter the product name:")
    price=int(input("Enter the price:"))
    product[name]=price
    temp=input("enter y if u want to continue:")
temp='y'
while temp=='y':
    item=input("enter the product whose price u want to view:")
    if item in product:
        print(product[item])
    else:
        print("Product not found:")
    temp=input("enter y if u want to continue:")

