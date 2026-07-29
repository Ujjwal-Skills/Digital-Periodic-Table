import random

# defining the function for the main menu
def main_menu(elements):
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

        try:
            choice = int(input("Enter your choice (1-9): ")) #taking input from user
            #chaking valid range
            if choice < 1 or choice > 9:
                print("Please select between 1 and 9.")

        except ValueError:
            print("❌ Invalid choice. Enter a number from 1 to 9.")
            continue
        print("") #too print empty line

        #handling the choices made by player
        if choice == 1:
            #print("\nView Periodic Table feature coming soon.")
            show_collection(elements)

        elif choice == 2:
            #print("\nsearch element feature coming soon.")
            search_element(elements)
        
        elif choice == 3:
            #print("\nCompare Elements feature coming soon.")
            compare_elements(elements)
        
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
            #print("\nAbout feature coming soon.")
            about()

        elif choice == 9:
            print("\nThank you for using the Digital Periodic Table!.\n")
            break

        else:
            print("Invalid choice. Please try again.")

#defining the function for reading the elements file 
def load_elements():

    elements = {} #empty dictionary which later updated by each element dictionary

    #handling missing file crash
    try:
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
    except FileNotFoundError:
        print("elements.txt was not found.")
        return {}
elements = load_elements()

#defining function to display elements info
def info(number):
    if number in elements:
        element = elements[number] #assigning specific element dictionary data into element

        #displaying element info
        print("+"+"="*50+"+")
        print("|               ⚛️ ELEMENT INFORMATION              |")
        print("+"+"="*50+"+")
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

        print("+"+"="*50+"+")
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
        try:
            number = int(input("Enter atomic number: "))
            #chaking valid range
            if number < 1 or number > 118:
                print("Atomic number must be between 1 and 118.")
                return 
            info(number)
        except ValueError:
            print("❌ Please enter a valid atomic number.")
            return

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
    #to give clean output look
    input("\nPress Enter to return to the Main Menu...")
#search_element(elements)

#defining function to campare two elements
def compare_elements(elements):
    try:
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

    except ValueError:
        print("❌ Please enter a valid atomic number.")

    #to give clean output look
    input("\nPress Enter to return to the Main Menu...")
#campore_elements(elements)

#defining function to search by categories
def categories(elements):
    #displaying category menu
    print("+"+"="*40+"+")
    print("|           ELEMENT CATEGORIES           |")
    print("+"+"="*40+"+")
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

    try:
        choice = int(input("Enter the choice (1-10): "))
        #chaking valid range
        if choice < 1 or choice > 10:
            print("Please select between 1 and 10.")

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

    except ValueError:
        print("❌ Invalid choice. Enter a number from 1 to 10.")

    #to give clean output look
    input("\nPress Enter to return to the Main Menu...")
#categories(elements)

#defining the discovery timeline function
def discovery_timeline(elements):

    #displaying the discovery timeline menu
    print("+"+"="*40+"+")
    print("|           DISCOVERY TIMELINE           |")
    print("+"+"="*40+"+")
    print("|","1. Ancient Elements"," "*18,"|")
    print("2. 1800-1899")
    print("3. 1900-1999")
    print("4. 2000 onwards")

    #taking input from user
    try:
        choice = int(input("Enter the choice (1-4): "))
        #chaking valid range
        if choice < 1 or choice > 4:
            print("Please select between 1 and 4.")

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

    except ValueError:
        print("❌ Invalid choice. Enter a number from 1 to 4.")

    #to give clean output look
    input("\nPress Enter to return to the Main Menu...")
#discovery_timeline(elements)

#defining the function for quiz
def quiz(elements):
    score = 0 #Initializing the score

    print("+"+"="*50+"+")
    print("|                  QUIZ CHALLENGE                  |")
    print("+"+"="*50+"+")

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

    #congratulation display
    if score == 5:
        print("Excellent! Perfect score!")
    elif score >= 3:
        print("Well done!")
    else:
        print("Keep practicing!")

    #storing user score
    name = input("Enter  your name: ")
    
    file = open("scores.txt","a")
    file.write(name +"|"+ str(score)+"\n")
    file.close()

    #to give clean output look
    input("\nPress Enter to return to the Main Menu...")
#quiz(elements)

#defining the function for highest scores
def highest_scores():
    try: #handling missing file crash
        file = open("scores.txt","r")
    
        print("+"+"="*40,"HIGHEST SCORES","="*40+"+")
        print("|","Name\t\tScore"," "*74,"|")
        print("+"+"-"*96+"+")

        found = False

        for line in file:
            found = True
            data = line.strip().split("|")
            print("|",data[0], "\t\t", data[1]," "*77,"|")

        if not found: #handling empty score file
            print("|","No scores available yet."," "*69,"|")

        print("+"+"="*96+"+")
        file.close()

        #to give clean output look
        input("\nPress Enter to return to the Main Menu...")

    except FileNotFoundError:
        print("scores.txt was not found.")
        return{}
#highest_scores()

#defining the function for about
def about():
    try: #handling missing file crash
        file = open("README.txt","r")

        for line in file:
            print(line,end="")
        file.close()

        #to give clean output look
        input("\nPress Enter to return to the Main Menu...")

    except FileNotFoundError:
        print("README.txt was not found.")
        return{}
#about()



#functions for displaying periodic table in ASCII art for good UX
#defining function for what should appear inside each cell of the periodic table
def get_symbol(number,elements):
    if number in elements:
        return elements[number]["symbol"].center(2)
    else:
        return "??"
#print(get_symbol(1,elements))

#defining function so that each symbol will be placed inside a bordered ASCII “tile” 
def make_cell(text):
    top = "+----+"
    middle = "|"+text.center(4)+"|"
    bottom = "+----+"
    return top,middle,bottom

#defining function to display table row layout
def row_layout(row):
    top_line = ""
    middle_line = ""
    bottom_line = ""

    for symbol in row:
        if symbol == " ":
            top_line += "      "
            middle_line += "      "
            bottom_line += "      "
        else:
            top,middle,bottom = make_cell(symbol)
            top_line += top
            middle_line += middle
            bottom_line += bottom

    print(top_line)
    print(middle_line)
    print(bottom_line)
#row_layout(row)

#defining function to get 1st row of table layout
def show_period_1 (elements):
    row = [" "]*18

    row[0] = get_symbol(1,elements) #group 1
    row[17] = get_symbol(2,elements) #group 18

    row_layout(row)    
#show_period_1(elements)

#defining function to get 2nd row of table layout
def show_period_2 (elements):
    row = [" "]*18
    row[0] = get_symbol(3,elements) #group 1
    row[1] = get_symbol(4,elements) #group 2
    for i in range(5,11):
        j = i + 7
        row[j] = get_symbol(i,elements) #group from 13 to 18
    
    row_layout(row)

#defining function to get 3rd row of table layout
def show_period_3 (elements):
    row = [" "]*18
    row[0] = get_symbol(11,elements) #group 1
    row[1] = get_symbol(12,elements) #group 2
    for i in range(13,19):
        j = i - 1
        row[j] = get_symbol(i,elements) #group from 13 to 18
    
    row_layout(row)

#defining function to get 4th row of table layout
def show_period_4 (elements):
    row = [" "]*18
    for i in range(19,37):
        j = i - 19
        row[j] = get_symbol(i,elements) #group from 1 to 18
        
    row_layout(row)

#defining function to get 5th row of table layout
def show_period_5 (elements):
    row = [" "]*18
    for i in range(37,55):
        j = i - 37
        row[j] = get_symbol(i,elements) #group from 1 to 18

    row_layout(row)

#defining function to get 6th row of table layout
def show_period_6 (elements):
    row = [" "]*18
    row[0] = get_symbol(55,elements) #group 1
    row[1] = get_symbol(56,elements) #group 2
    row[2] = get_symbol(57,elements) #group 3
    for i in range(72,87):
        j = (i+3) - 72
        row[j] = get_symbol(i,elements) #group from 4 to 18
    
    row_layout(row)

#defining function to get 7th row of table layout
def show_period_7 (elements):
    row = [" "]*18
    row[0] = get_symbol(87,elements) #group 1
    row[1] = get_symbol(88,elements) #group 2
    row[2] = get_symbol(89,elements) #group 3
    for i in range(104,119):
        j = (i+3) - 104
        row[j] = get_symbol(i,elements) #group from 4 to 18
    
    row_layout(row)

#defining function to get lanthanides row of table layout
def show_lanthanides (elements):
    row = [" "]*18

    for i in range(58,72):
        j = (i+3) - 58
        row[j] = get_symbol(i,elements) #group from 4 to 18

    row_layout(row)

#defining function to get actinides row of table layout
def show_actinides (elements):
    row = [" "]*18

    for i in range(90,104):
        j = (i+3) - 90
        row[j] = get_symbol(i,elements) #group from 4 to 18
    
    row_layout(row)

#defining function to display my elements in proper layout
def show_collection(elements):
    print("="*110)
    print("|"," "*37,"🧪", " DIGITAL PERIODIC TABLE ","🧪"," "*37,"|")
    print("="*110,"\n")
    show_period_1(elements)
    show_period_2(elements)
    show_period_3(elements)
    show_period_4(elements)
    show_period_5(elements)
    show_period_6(elements)
    show_period_7(elements)
    show_lanthanides(elements)
    show_actinides(elements)

    #to give clean output look
    input("\nPress Enter to return to the Main Menu...")
#show_collection(elements)

main_menu(elements)