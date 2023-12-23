import csv
import pyautogui
import time
from pywinauto.application import Application


# Read names from CSV
with open('Practice_file.csv', 'r') as file:
    reader = csv.reader(file)
    names = [row[0] for row in reader]

# Start your .exe program
app = Application().start("Premier.exe")

# Get the main window
main_window = app.window(title_re="PREMIER SETUP")

# Wait for some time to switch to the .exe program
window = main_window.wait('exists visible enabled ready active')

input("Press ENTER when on name Input Screen: ")

# Find the button (replace "Button Name" with the actual text or control name)
text_box = main_window.child_window(title="Man's Name", control_type="edit")

# Wait for the text box to become ready
text_box.wait('ready', timeout=10)
# Focus on the text box
text_box.set_focus()

# Get the coordinates of the button within the window
button_rect = text_box.rectangle()

# Calculate a point relative to the button
relative_point = ((button_rect.left + button_rect.right) // 2, (button_rect.top + button_rect.bottom) // 2)

# Click at the calculated relative point
text_box.click_input(coords=relative_point)

# Automate the insertion
for name in names:
    # Move mouse to textbox
    pyautogui.click(x=your_x_coordinate, y=your_y_coordinate)

    # Type the name
    pyautogui.typewrite(name)

    # You might need to add more automation steps (e.g., pressing Enter) depending on the program

    # Wait for a moment before moving to the next name
    time.sleep(1)
