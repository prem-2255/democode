menu={
    'samosa' :20,
    'vadapav' :30,
    'dabeli' :25,
    'sandwich' :30,
}
print("wellcome to my restursnt")
print("samosa:RS20\nvadapav:RS30\ndabeli:RS25\nsandwich:RS30")

order_total = 0

item_1 = input("enter the name of item you like=")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet!")

another_order = input("do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f" item {item_2} has been added to order ")
    else:
        print(f"ordered item {item_2} is not available yet!")

print (f"the total amount is {order_total}")