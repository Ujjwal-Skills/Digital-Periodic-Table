import random

# defining the function for the main menu
def main_menu():
    while True: #Return to the menu until player chooses to exit
        #displaying main menu
        print("\n+=================== MAIN MENU ===================+\n")
        print("1. View Periodic Table")
        print("2. 🔍 Search Element")
        print("3. Campare Elements")
        print("4. Categories")
        print("5. Discovery Timeline")
        print("6. 🧠 Quiz Challenge")
        print("7. Highest Scores")
        print("8. About")
        print("9. 🚪 Exit")
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
            #print("\nCategory feature coming soon.")
            categories(elements)

        elif choice == 5:
            #print("\nDiscovery Timeline feature coming soon.")
            discovery_timeline(elements)

        elif choice == 6:
            #print("\nQuiz Challenge feature coming soon.")
            quiz(elements)

        elif choice == 7:
            #print("\nHighest Scores feature coming soon.")
            highest_scores()

        elif choice == 8:
            print("\nAbout feature coming soon.")

        elif choice == 8:
            print("\nThank you for using the project.")
            break

        else:
            print("Invalid choice. Please try again.")

#defining the function for reading the elements file 
def load_elements():

    elements = {} #empty dictionary which later updated by each element dictionary

    file = open("elements.txt", "r")

    for line in file:
        data = line.strip().split("|")

        atomic_number = int(data[0]) #returns the atomic number of current element

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
        element = elements[number] #assigning specific element dictionary data into element

        #displaying element info
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
    
    #displaying menu for search
    print("\n==== Search Element ====")
    print("1. Search by Atomic Number")
    print("2. Search by Name")
    print("3. Search by Symbol")

    choice = int(input("Enter your choice (1-3): "))

    #handling choice
    if choice == 1:
        number = int(input("Enter atomic number: "))
        info(number)

    elif choice == 2:
        element_name = input("Enter the element name: ").strip().lower()

        found = False #start with element not found

        for atomic_number in elements:
            if elements[atomic_number]["name"].strip().lower() == element_name: #checks the element name if its present in elements
                #element = elements[atomic_number]
                info(atomic_number)
                found = True
                break

            if not found:
                print("Element not found.")

    elif choice == 3:
        element_symbol = input("Enter the element symbol: ").strip().lower()

        found = False #start with element not found

        for atomic_number in elements:
            if elements[atomic_number]["symbol"].strip().lower() == element_symbol: #checks the element symbol if its present in elements
                info(atomic_number)
                found = True
                break

        if not found:
            print("Element not found.")
#search_element(elements)

#defining function to campare two elements
def campare_elements(elements):
    #taking input from user
    first = int(input("Enter first atomic number: "))
    second = int(input("Enter second atomic number: "))

    if first in elements and second in elements:
        #putting sepecific element dictionary asked into element1 and element2
        element1 = elements[first]
        element2 = elements[second]

        #displaying campareing table
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
    #displaying category menu
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

    #handling choice
    if choice == 1:
        category = "Alkali Metal"
    elif choice == 2:
        category = "Alkaline Earth Metal"
    elif choice == 3:
            category = "Transition Metal"
    elif choice == 4:
        category = "Post-transition Metal"
    elif choice == 5:
        category = "Metalloid"
    elif choice == 6:
        category = "Non-metal"
    elif choice == 7:
        category = "Halogen"
    elif choice == 8:
        category = "Noble Gas"
    elif choice == 9:
        category = "Lanthanide"
    elif choice == 10:
        category = "Actinide"
    else:
        print("Invalid choice.")
        return

    #displaying category table
    print("\nAtomic No.\tSymbol\tName")
    print("-"*30)

    for atomic_number in elements:
        if elements[atomic_number]["category"] == category: #checks the element category if its present in elements
            print(
                atomic_number,
                elements[atomic_number]["symbol"],
                elements[atomic_number]["name"]
            )
#categories(elements)

#defining the discovery timeline function
def discovery_timeline(elements):

    #displaying the discovery timeline menu
    print("===== Discovery Timeline ====\n")
    print("1. Ancient Elements")
    print("2. 1800-1899")
    print("3. 1900-1999")
    print("4. 2000 onwards")

    #taking input from user
    choice = int(input("Enter the choice (1-4): "))

    #displaying discovery timeline table
    print("Atomic No.\tYear\tName")
    print("-"*30)

    for atomic_number in elements: #looping through all element
        year = elements[atomic_number]["year"]

        #handling choice
        if year == "Ancient":
            if choice == 1:
                print(atomic_number,"   ",elements[atomic_number]["year"],"   ",elements[atomic_number]["name"])

        if year != "Ancient":
            year = int(year)
            if choice == 2: 
                if 1800 <= year <=1899:
                    print(atomic_number,"   ",elements[atomic_number]["year"],"   ",elements[atomic_number]["name"])

            if choice == 3:  
                if 1900 <= year <=1999:
                    print(atomic_number,"   ",elements[atomic_number]["year"],"   ",elements[atomic_number]["name"])

            if choice == 4:   
                if 2000 <= year :
                    print(atomic_number,"   ",elements[atomic_number]["year"],"   ",elements[atomic_number]["name"])
#discovery_timeline(elements)

#defining the function for quiz
def quiz(elements):
    score = 0 #Initializing the score

    for question in range(1,6):
        number = random.randint(1, 118)
        element = elements[number]

        #question 1: What is the symbol of element
        print("\nQuestion",question)
        print("What is the symbol of",element["name"],"?")
        answer = input("Answer: ").strip().lower()

        if answer == element["symbol"].lower():
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")
            print("Correct answer:",element["symbol"])

    #quiz finish and calculating the score        
    print("\nQuiz Finished!")
    print("Your score:",score,"/5")

    #storing user score
    name = input("Enter  your name: ")
    
    file = open("scores.txt","a")
    file.write(name +"|"+ str(score)+"\n")
    file.close()
#quiz(elements)

def highest_scores():
    file = open("scores.txt","r")

    for line in file:
        data = line.strip().split("|")
        print(data[0], "-", data[1])

    file.close()
#highest_scores()