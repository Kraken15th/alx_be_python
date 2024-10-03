def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    def main():
     shopping_list = []
     while True:
        display_menu()
        choice = input("Enter your choice: ")
         choice == float
if input == "1":
   # Prompt for and add an item
   item = input("Enter item name: ")
 shopping_list.append(item) # type: ignore
print(f"{item} added to the list.")
if input == '2':
   # Prompt for and remove an item
   item_to_remove = input("Enter item name to remove: ")
   if item_to_remove in shopping_list: # type: ignore
      shopping_list.remove(item_to_remove) # type: ignore
      print(f"{item_to_remove} removed from the list.")
print(f"{item_to_remove} not found in the list.")
if input == '3':
# Display the shopping list
 if shopping_list: # type: ignore
   print("Shopping List:")
 for item in shopping_list: # type: ignore
   print(f"- {item}")
elif input == '4':
 print("Goodbye!")
print("Invalid choice. Please try again.")
