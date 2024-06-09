shopping_list = []

def add_stuff():
    new_stuff = input("Enter new stuff to purchase: ")
    shopping_list.append(new_stuff)
    print(f"'{new_stuff}' has been added to the shopping list")

def delete():
    try:
        number = int(input('Enter position to delete (starting from 0): '))
        if 0 <= number < len(shopping_list):
            removed_item = shopping_list.pop(number)
            print(f"'{removed_item}' has been removed from the shopping list.")
        else:
            print("Invalid position. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def print_list():
    if shopping_list:
        print("\n--- Shopping List ---")
        for i,item in enumerate(shopping_list):
            print(f"{i}. {item}")
    else:
        print("\nThe shopping list is empty.")

def clear_list():
    shopping_list.clear()
    print("The shopping list has been cleared.")

def save_list(filename="shopping_list.txt"):
    with open(filename, 'w') as file:
        for item in shopping_list:
            file.write(f"{item}\n")
    print(f"Shopping list saved to {filename}.")

def load_list(filename="shopping_list.txt"):
    try:
        with open(filename, 'r') as file:
            global shopping_list
            shopping_list = [line.strip() for line in file]
        print(f"Shopping list loaded form {filename}.")
    except FileNotFoundError:
        print(f"No saved shopping list found at {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def menu():
    print("\n---SHOPPING LIST---")
    print("1 - Add new item")
    print("2 - Delete an item")
    print("3 - Print the list")
    print("4 - Clear the list")
    print("5 - Save the list")
    print("6 - Load the list")
    print("exit - Shut down app")

def main():
    while True:
        menu()
        option = input("Choose option: ").strip().lower()
        if option == "1":
            add_stuff()
        elif option == "2":
            delete()
        elif option == "3":
            print_list()
        elif option == "4":
            clear_list()
        elif option == "5":
            save_list()
        elif option == "6":
            load_list()
        elif option == "exit":
            print("See you next time")
            break
        else:
            print("Invalid option, try again")


if __name__ == "__main__":
    main()