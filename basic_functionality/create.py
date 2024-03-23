import csv
import os
from datetime import datetime
from tkinter import Tk, filedialog
import uuid
import shutil

# Configuration
csv_log_path = 'inventory_log.csv'

# Predefined options for houses and their respective rooms
houses = ['House1', 'House2', 'House3']
rooms_by_house = {
    'House1': ['Kitchen', 'Living Room', 'Bedroom'],
    'House2': ['Dining Room', 'Guest Room', 'Bathroom'],
    'House3': ['Study', 'Library', 'Sun Room']
}

# Categories and subcategories
categories = ['Furniture', 'Appliances', 'Decor']
subcategories = {
    'Furniture': ['Chair', 'Table', 'Sofa'],
    'Appliances': ['Refrigerator', 'Microwave', 'Washing Machine'],
    'Decor': ['Lamp', 'Rug', 'Curtain']
}

def initialize_csv():
    if not os.path.exists(csv_log_path):
        with open(csv_log_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'House', 'Room', 'Category', 'Subcategory', 'Quantity', 'Image Path', 'Action', 'Timestamp'])

def get_unique_id():
    return str(uuid.uuid4())

def log_item_action(id, house, room, category, subcategory, quantity, image_path, action):
    with open(csv_log_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([id, house, room, category, subcategory, quantity, image_path, action, timestamp])

def select_option(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("Choose an option: ")
    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return options[int(choice) - 1]
    else:
        print("Invalid option, please try again.")
        return select_option(prompt, options)  # Recursively call until a valid input is received

def classify_new_item():
    Tk().withdraw()
    filename = filedialog.askopenfilename(title="Select an image of the item")
    if filename:
        id = get_unique_id()
        new_filename = f"{os.path.dirname(filename)}/{id}{os.path.splitext(filename)[1]}"
        shutil.move(filename, new_filename)
        
        house = select_option("Select the house:", houses)
        room = select_option(f"Select the room in {house}:", rooms_by_house[house])
        category = select_option("Select the category:", categories)
        subcategory = select_option("Select the subcategory:", subcategories[category])
        quantity = input("Enter the quantity of the item: ")
        
        log_item_action(id, house, room, category, subcategory, quantity, new_filename, "Classify")

def move_item():
    id = input("Enter the item ID to move: ")
    new_house = select_option("Select the new house:", houses)
    new_room = select_option(f"Select the new room in {new_house}:", rooms_by_house[new_house])
    # For simplicity, category and subcategory are not changed here. Modify as needed.
    category = "N/A"  # Placeholder, assuming category and subcategory don't change on move
    subcategory = "N/A"  # Placeholder
    quantity = "N/A"  # Placeholder, assuming quantity doesn't change on move
    image_path = "N/A"  # Placeholder, assuming the image path doesn't change on move
    log_item_action(id, new_house, new_room, category, subcategory, quantity, image_path, "Move")