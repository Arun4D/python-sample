import pandas as pd
import csv

from . import helpers

class InputExcelData:
    def __init__(self, Source, Destination, Port):
        self.Source = Source
        self.Destination = Destination
        self.Port = Port
    
    # This function will be used to convert the class object into a dictionary for CSV export
    def to_dict(self):
        return {
            'Source': self.Source,
            'Destination': self.Destination,
            'Port': self.Port
        }

class OutputCSVData:
    def __init__(self, Source, Destination, Port):
        self.Source = Source
        self.Destination = Destination
        self.Port = Port
    
    # This function will be used to convert the class object into a dictionary for CSV export
    def to_dict(self):
        return {
            'Source': self.Source,
            'Destination': self.Destination,
            'Port': self.Port
        }

FIELD_MAPPING = {
    'Source': 'Source Criteria',
    'Destination': 'Destination Criteria',
    'Port': 'Port Criteria'
}

# Step 2: Read Excel and store data into class objects
def read_excel_into_objects(file_path, columns):
    # Read the specific columns from Excel
    df = pd.read_excel(file_path, usecols=columns)
    
    # Store each row into a list of InputExcelData class objects
    data_objects = []
    for _, row in df.iterrows():
        # Create an instance of InputExcelData for each row
        data_obj = InputExcelData(row[columns[0]], row[columns[1]], row[columns[2]])
        data_objects.append(data_obj)
    
    return data_objects

# Step 3: Convert class objects to CSV
def write_objects_to_csv(data_objects, output_csv_path):

    # Get fieldnames from mapping
    fieldnames = [FIELD_MAPPING[attr] for attr in FIELD_MAPPING]

    # Open the CSV file for writing
    with open(output_csv_path, mode='w', newline='') as csv_file:
        # Define the fieldnames for CSV
        #fieldnames = ['Source Criteria', 'Destination Criteria', 'Servicess Criteria']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write the header (column names)
        writer.writeheader()
        
        # Write data rows
        for obj in data_objects:
            row = {FIELD_MAPPING[attr]: getattr(obj, attr) for attr in FIELD_MAPPING}
            writer.writerow(row)

# Step 4: Main function to call the operations
if __name__ == "__main__":
    # File paths and columns to read from the Excel file
    # Specify the input Excel template file path and output CSV template file path
    input_excel_path = helpers.get_input_excel_name()
    output_csv_path =  helpers.get_output_csv_name()

    input_excel_columns_to_read = ['Source', 'Destination', 'Port']  # Replace with your actual column names


    # Read data from Excel into class objects
    data_objects = read_excel_into_objects(input_excel_path, input_excel_columns_to_read)
    
    # Convert the class objects into CSV format
    write_objects_to_csv(data_objects, output_csv_path)
    
    print(f"Data has been successfully written to {output_csv_path}")