import csv
from app.classes.animal import Animal
from app.classes.zoo import Zoo
from app.db.database import Database

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

def generate_csv_report(animals, filename="animal_report.csv"):
    """Generate a CSV report of animals."""
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["ID", "Name", "Species"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for animal in animals:
            writer.writerow({"ID": animal[0], "Name": animal[1], "Species": animal[2]})

def display_all_animals(database):
    animals = database.get_all_animals()
    if animals:
        print("All animals in the database:")
        for animal in animals:
            print(f"ID: {animal[0]}, Name: {animal[1]}, Species: {animal[2]}")

        while True:
            try:
                report_choice = input("Do you want to generate a CSV report? (yes/no): ").lower()
                if report_choice == "yes":
                    generate_csv_report(animals)
                    print("CSV report generated as 'animal_report.csv'")
                    break
                elif report_choice == "no":
                    print("No CSV report generated.")
                    break
                else:
                    raise ValueError("Invalid choice. Please enter 'yes' or 'no'.")
            except ValueError as e:
                print(f"Error: {e}")
    else:
        print("No animals found.")

def remove_animal(database):
    try:
        animal_id = int(input("Enter the ID of the animal to remove: "))
        database.remove_animal(animal_id)
        print(f"Animal with ID {animal_id} has been removed from the database.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

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

def remove_zoo(database):
    try:
        zoo_id = int(input("Enter the ID of the zoo to remove: "))
        database.remove_zoo(zoo_id)
        print(f"Zoo with ID {zoo_id} has been removed from the database.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")        

def main():
    db_path = "app/db/database.db"
    database = Database(db_path)

    while True:
        print("")
        print("1. Add a new animal")
        print("2. Display all animals")
        print("3. Remove an animal")
        print("4. Add a new zoo")
        print("5. Display all zoos")
        print("6. Remove a zoo")
        print("7. Stop the application")
        print("")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            add_animal(database)

        elif choice == "2":
            display_all_animals(database)
        
        elif choice == "3":
            remove_animal(database)

        elif choice == "4":
            add_zoo(database)

        elif choice == "5":
            display_all_zoos(database)

        elif choice == "6":
            remove_zoo(database)    

        elif choice == "7":
            print("Application is being stopped.")
            break

        else:
            print("Invalid choice. Please try again.")

    database.close_connection()

if __name__ == "__main__":
    main()
