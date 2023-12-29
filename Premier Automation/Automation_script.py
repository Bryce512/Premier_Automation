import csv
from pywinauto.application import Application
from pywinauto.timings import Timings

csv_path = 'Practice_file.csv'
Database_name = 'BYU SDC 2022'

"""
Change ^^^ these file names BEFORE running
    csv_path = name of raw csv file exported from google sheets
    Database_name = the name of the .mdb database you're using
        do NOT include the .mdb in your title
"""

Cleaned_csv = 'Cleaned.csv'
application_path = 'Premier.exe'
Timings.fast()
Timings.after_clickinput_wait = 0.05  # Set the time to wait after clicking
Timings.after_editsetedittext_wait = 0

def clean_database():
# Read names from CSV
    with open(csv_path, 'r') as file:
        row = csv.reader(file)
        headers = next(row)
        output = open(Cleaned_csv, 'w')
        for names in row:
            Mfirst = names[1]
            Mlast = names[0]
            LFirst = names[3]
            LLast = names[2]
            # teacher = names[4]
            for index in range(5, 8):
                if names[index] != '':
                    cls = names[index]
            if '180' in cls:
                cls = 'BYU Dance 180  (CC)'
            elif '184' in cls:
                cls = 'BYU Dance 184  (Q)'
            elif '185' in cls:
                cls = 'BYU Dance 185  (S)'
            elif '280' in cls:
                cls = 'BYU Dance 280  (SW)'
            elif '284' in cls:
                cls = 'BYU Dance 284  (W)'
            elif '285' in cls:
                cls = 'BYU Dance 285  (R)'
            elif '380' in cls:
                cls = 'BYU Dance 382  (T)'
            elif '382' in cls:
                cls = 'BYU Dance 382  (T)'
            elif '383' in cls:
                cls = 'BYU Dance 383  (PD)'
            output.write(f'{Mfirst},{Mlast},{LFirst},{LLast},{cls}\n')
        output.close()
        
def set_up(comp_title,comp_window_name):
    try:
        Comp_setup = Application(backend='uia').connect(title = comp_window_name, auto_id="frmTopLevel")
        Comp_setup[f'{comp_title}'].set_focus()
        return Comp_setup
    except:
        app = Application(backend='uia').start(application_path)
        # Get the main window
        main_window = app.window(title_re = "PREMIER WELCOME SCREEN")
        # Wait for some time to switch to the .exe program
        # window = main_window.wait('exists visible enabled ready active',timeout=5)
        Run_button = main_window.child_window(title_re='RUN PROGRAM')
        Run_button.click_input()
        Application(backend='uia').connect(title='PREMIER SETUP',timeout=3)
        input("Press ENTER when on name Input Screen: ")
        Comp_setup = Application(backend='uia').connect(title = comp_window_name, auto_id ="frmTopLevel")
        Comp_setup[f'{comp_title}'].set_focus()
        return Comp_setup

def type_names(comp_title,Comp_setup):
    entry_form = Comp_setup[f'{comp_title}'].child_window(title = 'ADD A NEW COUPLE', auto_id="frmAddCouples")
    entry_form.child_window(title="Couple Information", control_type="TabItem").click_input()
    # Read names from CSV
    with open(Cleaned_csv, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            Mfirst,Mlast,LFirst,LLast,cls = get_data(row)
            entry_form.child_window(title="Last Name:", auto_id="txtBoxSearchLeaderLast", control_type="Edit").set_text(f'{Mlast}')
            entry_form.child_window(title="First Name:", auto_id="txtBoxSearchLeaderFirst", control_type="Edit").set_text(f'{Mfirst}')
            entry_form.child_window(auto_id="txtBoxSearchFollowerLast", control_type="Edit").set_text(f'{LLast}')
            entry_form.child_window(auto_id="txtBoxSearchFollowerFirst", control_type="Edit").set_text(f'{LFirst}')
            entry_form.child_window(title="Add Event Entries", control_type="TabItem").click_input()
            # entry_form.print_control_identifiers()
            entry_form.child_window(title=f'{cls}',control_type="ListItem").click_input(double=True)
            entry_form.child_window(title="Biographical Data", control_type="TabItem").click_input()
            # entry_form.StudioEdit2.set_text(f'{Teacher}')
            # entry_form.child_window(title="SAVE CURRENT ENTRIES", auto_id="btnSaveCouple", control_type="Button").click_input()
            entry_form.child_window(title="Couple Information", control_type="TabItem").click_input()
                

def get_data(names):
    return names[0], names[1], names[2], names[3], names[4]

def close_program(setup):
    setup.PremierSetup.set_focus()
    setup = setup["Dialog"]
    setup['DATABASE'].select()
    #  setup.print_control_identifiers()
# Click the Close MenuItem
    submenu= ['']
    setup['Close Premier'].click_input()
    # setup.print_control_identifiers()
# Switch window and Click Close Button
    # Close = setup.PremierSetup.child_window(title="QUESTION", control_type="Window")
    close_button = setup.child_window(title="Yes", auto_id="6", control_type="Button")
    close_button.click_input()

def get_Shortened_Title(title):
    shortened_title = ''
    title = title.lower().split()
    for word in title:
        i=0
        for letter in word:
            if i != 0 and letter.isalpha():
                shortened_title += letter
            elif i == 0 and letter.isalpha():
                shortened_title += letter.upper()
            else:
                pass
            i += 1
    return shortened_title

def main():
    clean_database()
    input("Hit ENTER once you checked the \'Cleaned.csv\' file looks okay: ")
    comp_window_name = f"NDCA DANCE COMPETITION SETUP:            DATABASE =  {Database_name}"
    comp_title = get_Shortened_Title(comp_window_name)
    Comp_setup = set_up(comp_title,comp_window_name)   
    type_names(comp_title,Comp_setup)
    
if __name__ == '__main__':
    main()