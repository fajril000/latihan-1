#cashier_task_14

print('==== Parfum Store Nota =====')

item_name = input('input item name   : ')
price = float(input('input price item   : '))
quantity = float(input('input quantity of the item   : '))
total_money = float(input('input total money you payn   : '))
re_money= total_money - quantity * price

#Nota

text= f'''
================================================
                 ROLINS HERBAL
================================================
- your item name            : {item_name}
-your item price            : {price}
-your item quantity         : {quantity}
-your total of money        : {total_money}
-you total of change        : IDR{re_money}
================================================
'''
#open and make new file txt

file= open('nota.txt', 'w')

#writing ito file
file.write(text)