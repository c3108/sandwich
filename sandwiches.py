# practice filling dictionaries from inputs and looping
# Set a flag to indicate ordering is active
order_active = True
group_orders = {}

print("Welcome to group sandwich ordering. " +
	"Type 'done' at any time to quit orders")

while order_active:

	#prompt for a name and sandwich order and check if order finished
	name = input("\nWhat is your name? ")
	if name == 'done':
		break
	order = input("What sandwich would you like? ")
	if order == "done":
		break
	#add order to the dictionary
	group_orders[name] = order
	more = input("Would you like to order more? Type 'yes' or 'no' ")
	if more == 'no':
		order_active = False

#print the orders
print('\n')
for name, order in group_orders.items():
	print(name + " ordered the " + order + " sandwich")

print("\nMaking sandwiches now.")

# Remove orders requesting Turkey sandwiches
for name in list(group_orders.keys()):
	if group_orders[name].title() == 'Turkey':
		del group_orders[name]
		print("Sorry " + name + " turkey is not available." +
			" Your order has been deleted.")


for name, order in group_orders.items():
	print(name + ", we made your " + order + " sandwich.")