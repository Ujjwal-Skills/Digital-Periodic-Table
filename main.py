# defining the function for the main menu
def main_menu():
    #seed = 53
    while True: #Return to the menu until player chooses to exit
        print("\n+=================== MAIN MENU ===================+\n")
        print("1. View Periodic Table")
        print("2. 🔍 Search Element")
        print("3. Campare Elements")
        print("4. 🧠 Quiz Challenge")
        print("5. Highest Scores")
        print("6. About")
        print("7. 🚪 Exit")
        print("="*45)

        choice = int(input("Enter your choice (1-7): ")) #taking input from user

        #handling the choices made by player
        if choice == 1:
            print("\nView Periodic Table feature coming soon.")

        elif choice == 2:
            #print("\nsearch element feature coming soon.")
            search_element(elements)
        
        elif choice == 3:
            #print("\nCompare Elements feature coming soon.")
            campare_elements(elements)
        
        elif choice == 4:
            print("\nQuiz feature coming soon.")

        elif choice == 5:
            print("\nHighest Scores feature coming soon.")

        elif choice == 6:
            print("\nHighest Scores feature coming soon.")

        elif choice == 7:
            print("\nThank you for using the project.")
            break

        else:
            print("Invalid choice. Please try again.")

#defining the function for reading the elements file 
def load_elements():

    elements = {}

    file = open("table/elements.txt", "r")

    for line in file:
        data = line.strip().split("|")

        atomic_number = int(data[0])

        elements[atomic_number] = {
            "atom_number": data[0],
            "name": data[1],
            "symbol": data[2],
            "atomic_mass": float(data[3]),
            "category": data[4],
            "group": int(data[5]),
            "period": int(data[6]),
            "state": data[7],
            "discovered_by": data[8],
            "year": data[9],
            "fun_fact": data[10]
        }

    file.close()
    return elements
elements = load_elements()

#defining function to display elements info
def info(number):
    if number in elements:
        element = elements[number]

        print("========================================")
        print("⚛️ ELEMENT INFORMATION")
        print("========================================")
        print("Name:",element["name"])
        print("Symbol:",element["symbol"])
        print("Atomic Number:",element["atom_number"])
        print("Atomic Mass:",element["atomic_mass"])
        print("Category:",element["category"])
        print("Group:",element["group"])
        print("Period:",element["period"])
        print("State:",element["state"])
        #print("Melting Point:",elements[number]["melting"])
        #print("Boiling Point:",elements[number]["boiling"])
        print("Discovered By:",element["discovered_by"])
        print("Year of Discovery:",element["year"])
        print("\n💡 Fun Fact:",element["fun_fact"])

        print("========================================")
    else:
        print("Element not found.")

#defining function to search elements
def search_element(elements):

    print("\n==== Search Element ====")
    print("1. Search by Atomic Number")
    print("2. Search by Name")
    print("3. Search by Symbol")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        number = int(input("Enter atomic number: "))
        info(number)

    elif choice == 2:
        element_name = input("Enter the element name: ").strip().lower()

        found = False

        for atomic_number in elements:
            if elements[atomic_number]["name"].strip().lower() == element_name:
                #element = elements[atomic_number]
                info(atomic_number)
                found = True
                break

            if not found:
                print("Element not found.")

    elif choice == 3:
        element_symbol = input("Enter the element symbol: ").strip().lower()

        found = False

        for atomic_number in elements:
            if elements[atomic_number]["symbol"].strip().lower() == element_symbol:
                info(atomic_number)
                found = True
                break

        if not found:
            print("Element not found.")
#search_element(elements)

#defining function to campare two elements
def campare_elements(elements):
    first = int(input("Enter first atomic number: "))
    second = int(input("Enter second atomic number: "))

    if first in elements and second in elements:
        element1 = elements[first]
        element2 = elements[second]

        print("\n==== COMPARISON ====")
        print("Propery            Element 1            Element 2")
        print("-"*50)

        print("Name:              ", element1["name"], "              ", element2["name"])
        print("Symbol:                ", element1["symbol"], "                ", element2["symbol"])
        print("Atomic Mass:        ", element1["atomic_mass"], "           ", element2["atomic_mass"])
        print("Category:         ", element1["category"], "            ", element2["category"])
        print("Group:                ", element1["group"], "                   ", element2["group"])
        print("Period:              ", element1["period"], "                   ", element2["period"])
        print("State:           ", element1["state"], "            ", element2["state"])

    else:
        print("One or both elements not found.")
#campare_elements(elements)


#defining function to search by categories
def categories(elements):
    print("==== Categories ====")
    print("1. Alkali Metal")
    print("2. Alkaline Earth Metal")
    print("3. Transition Metal")
    print("4. Post-transition Metal")
    print("5. Metalloid")
    print("6. Non-metal")
    print("7. Halogen")
    print("8. Noble Gas")
    print("9. Lanthanide")
    print("10. Actinide")

    choice = int(input("Enter the choice (1-10): "))

    for atomic_number in elements:

categories(elements)