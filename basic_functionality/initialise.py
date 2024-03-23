# Configuration
csv_log_path = 'inventory_log.csv'
caonfig_path = 'config.csv'

# Initialize empty structures for dynamic population
houses = []
rooms_by_house = {}
categories = []
subcategories = {}

def load_configuration():
    with open(config_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type'] == 'House':
                houses.append(row['Value'])
            elif row['Type'] == 'Room':
                if row['Key'] not in rooms_by_house:
                    rooms_by_house[row['Key']] = []
                rooms_by_house[row['Key']].append(row['Value'])
            elif row['Type'] == 'Category':
                categories.append(row['Value'])
            elif row['Type'] == 'Subcategory':
                if row['Key'] not in subcategories:
                    subcategories[row['Key']] = []
                subcategories[row['Key']].append(row['Value'])