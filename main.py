from app.classes.animal import Animal
from app.db.database import Database
from app.classes.zoo import Zoo

def add_animal(database):
    while True:
        try:
            name = input("Enter the name of the animal: ")
            if not name:
                raise ValueError("Field cannot be empty.")
            
            species = input("Enter the species of the animal: ")
            if not species:
                raise ValueError("Field cannot be empty.")
            
            new_animal = Animal(name, species)
            database.add_animal(new_animal)

            print(f"Animal '{name}' has been added.")
            break

        except ValueError as e:
            print(f"Error: {e}")

def display_all_animals(database):
    animals = database.get_all_animals()
    if animals:
        print("All animals in the database:")
        for animal in animals:
            print(f"ID: {animal[0]}, Name: {animal[1]}, Species: {animal[2]}")
    else:
        print("No animals found in the database.")

def display_all_animals(database):
    animals = database.get_all_animals()
    if animals:
        print("All animals in the database:")
        for animal in animals:
            print(f"ID: {animal[0]}, Name: {animal[1]}, Species: {animal[2]}")
    else:
        print("No animals found.")

def add_zoo(database):
    while True:
        try:
            name = input("Enter the name of the zoo: ")
            if not name:
                raise ValueError("Field cannot be empty.")
            
            location = input("Enter the location of the zoo: ")
            if not location:
                raise ValueError("Field cannot be empty.")
            
            new_zoo = Zoo(name, location)
            database.add_zoo(new_zoo)
            print(f"Zoo '{name}' has been added to the database.")
            break
        except ValueError as e:
            print(f"Error: {e}")


def display_all_zoos(database):
    zoos = database.get_all_zoos()
    if zoos:
        print("All zoos in the database:")
        for zoo in zoos:
            print(f"ID: {zoo[0]}, Name: {zoo[1]}, Location: {zoo[2]}")
    else:
        print("No zoos found in the database.")


def main():
    db_path = "app/db/database.db"
    database = Database(db_path)

    while True:
        print("")
        print("1. Add a new animal")
        print("2. Display all animals")
        print("3. Add a new zoo")
        print("4. Display all zoos")
        print("5. Stop the application")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            add_animal(database)

        elif choice == "2":
            display_all_animals(database)

        elif choice == "3":
            add_zoo(database)

        elif choice == "4":
            display_all_zoos(database)

        elif choice == "5":
            print("Application is being stopped.")
            break

        else:
            print("Invalid choice. Please try again.")

    database.close_connection()

if __name__ == "__main__":
    main()
