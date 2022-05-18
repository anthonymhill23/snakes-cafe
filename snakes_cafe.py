"""
Lab 1: Intro to Python
Overview: Today I will begin to work on a command line utility to whill mimic the functionaliaty of a restaurant, using our very basic understanding of python.
"""

ticket = {}
Appetizers = ['Wings', 'Cookies', 'Spring Rolls']
Entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
Desserts = ['Ice Cream','Cake','Pie']
Drinks = ['Coffee','Tea', 'Unicorn Tears']

print('$ python snakes_cafe.py')
print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**                                  **')
print('** To quit at any time, type "quit" **')
print('**************************************')
print('')
print('Appetizers')
print('----------')
for Appetizer in Appetizers:
    print(Appetizer)
print('')
print('Entrees')
print('----------')
for Entree in Entrees:
    print(Entree)
print('')
print('Desserts')
print('----------')
for Dessert in Desserts:
    print(Dessert)
print('')
print('Drinks')
print('----------')
for Drink in Drinks:
    print(Drink)
print('')
print('***********************************')
print('** What would you like to order? **')
print('***********************************')
print('')
while True:
    order = input('> ').capitalize()
    if order == 'Quit':
        break
    elif order not in Desserts + Drinks + Entrees + Appetizers:
        print('\n**That is not a valid menu item, we do not serve that here.**\n')
        continue
    elif order not in ticket:
        ticket.update({order: 0})
    ticket[order] += 1 
    print(f'\n** {ticket[order]} orders of {order} have been added to your meal.**\n')