import csv

# csv_path = input("What is the name of your file? ")
csv_path = "USADC2024.csv"
# csv_path = "Practice_file.csv"
csv_temp = csv_path.split(".")
Cleaned_csv = csv_temp[0]+ "_cleaned.csv"


# *** -------> Clean Database <-------- ***
def clean_database():
# Read info from CSV
    names_index = get_names_index()
    skipped_columns = get_skipped()
    danceList = getDanceList()
    with open(csv_path,'r') as file:
        row = csv.reader(file)
        headers = next(row)
        output = open(Cleaned_csv,'w')
        for info in row: # go through each line in csv file
            for i in names_index: # Capitalize the first letter of the first 4 elements(First and Last names)
                name = info[i]
                info[i] = name[0].upper() + name[1:].lower()
            c = 0
            for j in danceList: # Find the class code within the bronze, silver, & gold columns
                if info[j] != '':
                    cls = info[j]
                    cls_num = ''
                    for k in cls:
                        if k.isdigit():
                            cls_num += k # strip the class code out (ex. 180)
                    # print("cls_num:", cls_num)  # Debugging print
                    if classDict[cls_num]:
                        info[j] = classDict.get(cls_num) # change the class to the official class code the DB expects (ex BYU Dance 180 - Bronze American (CC))
                else: 
                    c+=1
            if c < 3:
                for i in range(0,len(info)): # Print out all the info in each line in CSV format
                    if i in skipped_columns:
                        pass
                    else:
                        if i != len(info) - 1:
                            output.write(f"{info[i]},")
                        else: 
                            output.write(f"{info[i]}")
                output.write("\n")
    output.close()

# *** -----------> Create TXT from Cleaned CSV <----------- ***
def createTXT():
    temp = Cleaned_csv.split("_")
    txt_file = temp[0] + ".txt"
    with open(txt_file, "w") as my_output_file:
        with open(Cleaned_csv, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
        my_input_file.close()

    print(f"File Done! Your TXT file is called {txt_file}")
    print()
    print()




# *** -----------> Class Dictionary <----------- ***
classDict = {
    "180":"BYU Dance 180 - Bronze American (CC)",
    "181":"BYU Dance 181 - Bronze Country Western (TS)",
    "184":"BYU Dance 184 - Bronze Ballroom (Q)",
    "185":"BYU Dance 185 - Bronze Latin (S)",
    "280":"BYU Dance 280 - Silver American (SW)",
    "281":"BYU Dance 281 - Silver Country Western (PO)",
    "284":"BYU Dance 284 - Silver Ballroom (W)",
    "285":"BYU Dance 285 - Silver Latin (R)",
    "380":"BYU Dance 380 - Gold American (F)",
    "382":"BYU Dance 382 - Gold I Ballroom (T)",
    "383":"BYU Dance 383 - Gold I Latin (PD)",
    "384":"BYU Dance 384 - Gold II Ballrom (W)",
    "385":"BYU Dance 385 - Gold II Latin (S)",
    "480":"BYU Dance 480 - Gold Bar American (M)",
    "484":"BYU Dance 484 - Gold Bar Ballroom (F)",
    "485":"BYU Dance 485 - Gold Bar Latin (PD)",
  };

alphaDict = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7,
    "I" : 8,
    "J" : 9,
    "K" : 10,
    "L" : 11,
    "M" : 12,
    "N" : 13,
    "O" : 14,
    "P" : 15,
    "Q" : 16,
    "R" : 17,
    "S" : 18,
    "T" : 19,
    "U" : 20,
    "V" : 21,
    "W" : 22,
    "X" : 23,
    "Y" : 24,
    "Z" : 25,
};

#*** -----------> Get Names Index <------------- ***

def get_names_index():
    print("Please type the letter of the columns containing first or last names.")
    printInstructions()
    names_index = []
    getInput("Enter a name column. If done, hit 'Enter': ",names_index)
    return names_index
    
#*** -----------> Get Skipped List <------------- ***

def get_skipped():
    skipped = []
    skip = input("Would you like to skip any columns? y/n : ")
    if skip.upper() == "N":
        print()
        print()
        pass 
    elif skip.upper() == "Y":
        print()
        print("Great!")
        getInput("What column(s) would you like to skip? ",skipped)
    else:
        print("Invalid entry. Type y or n")
        print()
        print()
        pass
    print()
    print()
    return skipped

#*** -----------> Get Dance Columns <------------- ***
def getDanceList():
    DanceList = []
    # printInstructions()
    getInput("What columns are the Dance levels in? ",DanceList)
    return DanceList



#*** -----------> printInstructions() <------------- ***
def printInstructions():
    print("Type just one letter or a range")
    print("Example: 'a' or 'a-d'")
    print("Do not include quotes.")
    print()
    print("When done, hit 'Enter'")
    print()


#*** -----------> processRange() <------------- ***
def processRange(input, lst):
    if len(input) != 3:
        print("Please submit like this 'a-d' with no quotes.")
        pass
    else:
        input = input.split("-")
        a = input[0]
        b = input[1]
        if a in alphaDict and b in alphaDict:
            for i in range(alphaDict.get(a),alphaDict.get(b)+1):
                lst.append(i)
            print("Success!")
        else:
            print("One of those values is invalid. Please type a letter between A-Z")
            pass


#*** -----------> getInput() <------------- ***
def getInput(prompt, lst):
    while True:
        ans = input(prompt).upper()
        if ans == "":
            print()
            print()
            break
        if "-" in ans:
            processRange(ans,lst)
        if ans in alphaDict:
                lst.append(alphaDict.get(ans))
                print("Success!")
        elif ans not in alphaDict and not "-" in ans:
            print("Invalid entry. Input must be A-Z, please try again.")
            pass
        else:
            pass
        

#*** -----------> Main<------------- ***
def main():
    print()
    print("***************************************")
    print()
    print("Welcome to the Dance Competition Database Tool!")
    print()
    print("***************************************")
    print()
    clean_database()
    createTXT()


#*** -----------> Run begins below <------------- ***
main()

