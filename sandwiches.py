# practice filling dictionaries from inputs and looping
# Set a flag to indicate ordering is active
order_active = True
group_orders = {}
name = ''
menu = ['ham', 'turkey', 'pb&j', 'salami', 'roost beef']
unavailable = 'turkey'

print("Welcome to group sandwich ordering. " +
	"Type 'done' at any time to quit orders")

print("\n We offer ham, turkey, pb&j, salami, and roost beef sandwichs")

while order_active:

	#prompt for a name and sandwich order and check if order finished
	name = input("\nWhat is your name? ")
	if name == 'done':
		break
	# Check if name is already taken
	if name in group_orders.keys():
		print("Name already used, please use a different name.")
		continue

	order = input("What sandwich would you like? ")
	
	#See if selected sandwich is on the menu
	while order.lower() not in (menu_item.lower() for menu_item in menu):
		prompt = "Please select a sandwich from the menu. " + "\n"
		for j in range(len(menu)-1):
			prompt = prompt + menu[j].lower() + (", ")
		prompt = prompt + "or " + menu[-1] + ": "
		order = input(prompt)
		if order == "done":
			break

	if order == "done":
		break

	#add order to the dictionary
	group_orders[name] = order
	more = input("Would you like to order more? Type 'yes' or 'no' ")
	if more == 'no':
		order_active = False

#print the orders
print('\n')
if group_orders != {}:
	for name, order in group_orders.items():
		print(name + " ordered the " + order + " sandwich")

	if group_orders != {}:
		print("\nMaking sandwiches now.")
else:
	print("You did not order any sandwiches :-(.")


# Remove orders requesting Turkey sandwiches
for name in list(group_orders.keys()):
	if group_orders[name].title() == unavailable.title():
		del group_orders[name]
		print("Sorry " + name + ", " + unavailable + " is not available." +
			" Your order has been deleted.")


for name, order in group_orders.items():
	print(name + ", we made your " + order + " sandwich.")