print("\nTo-Do List")

from prettytable import PrettyTable

print("\nHere's a list of commands you can use to create your list:")

instructions = "\n1: Enter A or a to add a new item. \n2: Enter D or d to delete an item. \n3: Enter U or u to update an item. \n4: Enter E or e to exit the program. \n5: Enter L or l to view your To-Do list."
print(instructions)

my_todo_list = []

x = PrettyTable()


def my_list():
    x.field_names = ["Item Names"]
    for i in my_todo_list:
        x.add_row([i])
    print(x.get_string(title="To-Do List"))
    x.clear_rows()


running = True
while running:
    user_input = input("\nWhat do you want to do? (A, D, U, E, L) ").lower()
    if user_input == "a" or user_input == "A":
        new_todo = input("\nWhat would you like to add to your list? ").lower()
        print(f"\n{new_todo} has been added to your To-Do list.")
        my_todo_list.append(new_todo)

    elif user_input == "d" or user_input == "D":
        while True:
            item_name = input("\nPlease enter the name of an item you wish to delete. ").lower()
            try:
                if item_name in my_todo_list:
                    choice = input(f"Are you sure to delete {item_name} from your To-Do list? (Y/N) ").lower()
                    if choice == "y" or choice == "Y":
                        my_todo_list.remove(item_name)
                        print("Your To-Do List has been updated.")
                        my_list()
                        break
                else:
                    print("Item not found")
            except Exception:
                print("Something went wrong.")
    elif user_input == "u" or user_input == "U":
        while True:
            item_name = input("\nWhich item do you want to update?: ").lower()
            try:
                if item_name in my_todo_list:
                    choice = input(
                        f"\nAre you sure you want to update {item_name} from your To-Do list? (Y/N) ").lower()
                    if choice == "y" or choice == "Y":
                        update_item = input(f"\nPlease enter your updated response for {item_name} ").lower()
                        index = my_todo_list.index(item_name)
                        my_todo_list[index] = update_item
                        print("Your To-Do list has been updated.")
                        my_list()
                        break
                else:
                    print("Item not found.")
            except Exception:
                print("Something went wrong.")
    elif user_input == "e" or user_input == "E":
        ask_user = input("\nAre you sure you want to exit? (Y/N): ").lower()
        if ask_user == "y" or ask_user == "Y":
            running = False
    elif user_input == "l" or user_input == "L":
        my_list()
    elif user_input == "" or user_input == " ":
        print("Please enter a response.")
    else:
        print("Please enter a valid command.")
