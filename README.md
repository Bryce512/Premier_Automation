# Premier Automation
*Currently only works with BYU Dance class entries that were uploaded to a Google Sheets and exported as a CSV*

Before Running for the first time:
    1. Download code and move into the folder with Premier.exe
    2. Download Pywinauto by running 'pip(or pip3) install pywinauto' in the terminal

Do before each new Competition:
    1. Export BYU Class Entries Google Sheet as a CSV and save to the same folder with Premier.exe
    2. In your terminal, change to the folder with Premier.exe by using the command "cd " you can tab until you find the right folder(AKA Directory)
        - if you need to go back use "cd .."
        - hit ENTER to select Directory
    3. Ensure that the Events in the Clean_Database() function are what will be included in the current competition.
    4. Change CSV_Path on line 6 to name of CSV file.
    5. Change Database_name on line 7 to name of Databse File.
